from sklearn.feature_extraction.text import TfidfVectorizer
from tqdm import tqdm
import pdb
import argparse
import sys
import json
import requests
import time
import spacy
import csv
import subprocess
import numpy as np
import faiss
import textwrap

def encode_sparse(X):
    encoder = TfidfVectorizer(stop_words='english', ngram_range=(1, 2), max_df=0.3)
    encoder.fit(X)
    print("Dimension: ", len(encoder.vocabulary_))
    embedding = encoder.transform(X).toarray()
    return embedding

def sent_tokenize(doc):
    nlp = spacy.load("en_core_web_sm", exclude=["parser"])
    nlp.enable_pipe("senter")
    return nlp(doc)
        
def main(args):
    ################################################################################
    # Read Queries
    ################################################################################
    print('Read Query Files from %s' % args.query_files)
    with open(args.query_files, 'r') as query_files:
        json_lines = []
        lines = query_files.readlines()
        for line in lines:
            j = json.loads(line)
            json_lines.append(j)

    NUM_RAW_QUERIES = len(json_lines)
#    NUM_RAW_QUERIES = 10
    print('NUM_RAW_QUERIES: %d' % NUM_RAW_QUERIES)
    
    ################################################################################
    # Tokenize Queries and Measure Average Token Length
    ################################################################################
    print("Tokenize Queries and Measure Average Token Length")
    qlen_vec   = [0] * NUM_RAW_QUERIES
    query_docs = [None] * NUM_RAW_QUERIES
    for i in tqdm(range(NUM_RAW_QUERIES)):
        cur_len       = 0
        qlen_vec[i]   = len(json_lines[i]['text'].split())
    AVG_TOK_LEN = np.rint(np.mean(qlen_vec))
    print('Average Token Length: %d' % AVG_TOK_LEN )

    ################################################################################
    # Encode Queries
    ################################################################################
    print("Encode Queries")
    TR = 'tr_' + args.dataset_name
    TR_TSV  = 'emb/' + TR + '.tsv' 
    with open(TR_TSV, 'w') as q_csv_file:
        keys = ['doc_id', 'doc_text', 'title']
        q_dw = csv.DictWriter(q_csv_file, keys, delimiter='\t')
        for i in range(NUM_RAW_QUERIES):
            q_dw.writerow({'doc_id': str(i), 'doc_text': json_lines[i]['text'], 'title': ''})
    if args.emb=='dense':
        subprocess.call(['emb/generate_embedding.sh', TR])
    query_embeddings = np.load('emb/' + TR + '_0.pkl', allow_pickle=True)
    print(len(query_embeddings))
    ################################################################################
    # Segment Raw Queries
    ################################################################################
    startIdx = 0
    endIdx = NUM_RAW_QUERIES

    for i in tqdm(range(startIdx, endIdx)):
        # Error skip
        if args.dataset_name == 'hyperpartisan_news' and i == 116:
            continue
        query_docs[i] = sent_tokenize(json_lines[i]['text'])
        seg_queries = []
        if len(query_docs[i]) < 100:
            temp = ''
            for sent in query_docs[i].sents:
                temp += sent.text
            seg_queries.append(temp)
        else:
            temp = ''
            num_tokens = 0
            for sent in query_docs[i].sents:
                if num_tokens < 100:
                    temp += sent.text
                    num_tokens += len(sent)
                else:
                    seg_queries.append(temp)
                    temp = ''
                    num_tokens = 0
            if temp != '':
                    seg_queries.append(temp)
                    temp = ''
                    num_tokens = 0                
        NUM_SEG_QUERIES = len(seg_queries)

        ################################################################################
        # Retrieve CC documents
        ################################################################################
        #solr_select = 'http://localhost:8983/solr/depcc-large/select?q='
        solr_select = 'http://localhost:8983/solr/depcc-small/select?q='
        # solr_select = 'http://localhost:8983/solr/depcc-large/select?q='
        # solr_select = 'http://localhost:8983/solr/depcc-small/select?fl=score%2C*&q='
        cc_psgs = []
        print('Process NUM_SEG_QUERIES: %d' % NUM_SEG_QUERIES)
        for j in range(NUM_SEG_QUERIES):
            q = seg_queries[j].replace(' ', '+')
            retrieved = requests.get(solr_select + q).json()
            if 'response' not in retrieved:
                continue
            retrieved_docs = (retrieved['response']['docs'])
            NUM_RETRIEVED_DOCS = args.max_doc
            if args.max_doc > len(retrieved_docs):
                NUM_RETRIEVED_DOCS = len(retrieved_docs)
            if NUM_RETRIEVED_DOCS == 0:
                continue
            cc_docs_raw = ""
            for k in range(NUM_RETRIEVED_DOCS):
                try:
                    cur = json.loads(retrieved_docs[k]['_src_'])['text']
                    if len(cc_docs_raw) + len(cur) > 1000000:
                        break
                    else:
                        cc_docs_raw += cur
                except ValueError:
                    continue
            if len(cc_docs_raw) == 0:
                continue
            ################################################################################
            # Segmented Retrieved Documents into CC passages
            ################################################################################
            cc_docs_tok = sent_tokenize(cc_docs_raw)
            if len(cc_docs_tok) < 100:
                cc_psgs.append({'doc_id' : '', 'doc_text'  : cc_docs_raw,  'title': ''  })
            else:
                temp = ''
                num_tokens = 0
                for sent in cc_docs_tok.sents:
                    if num_tokens < AVG_TOK_LEN:
                        temp += sent.text
                        num_tokens += len(sent)
                    else:
                        cc_psgs.append({'doc_id' : '', 'doc_text'  : temp,  'title': ''  })
                        temp = ''
                        num_tokens = 0
                if temp != '':
                    cc_psgs.append({'doc_id' : '', 'doc_text'  : temp,  'title': ''  })
                    temp = ''
                    num_tokens = 0
        if len(cc_psgs) == 0:  # Handle exception
            continue
        ################################################################################
        # Prepare Train and CC passages for sorting
        ################################################################################


        CC = 'cc_' + args.dataset_name
        CC_TSV  = 'emb/' + CC + '.tsv'
        with open(CC_TSV, 'w') as cc_csv_file:
            cc_dw = csv.DictWriter(cc_csv_file, cc_psgs[0].keys(), delimiter='\t')
            for cc_psg in cc_psgs:
                cc_dw.writerow(cc_psg)
        MAX_CC_PSGS = len(cc_psgs)
        print('MAX_CC_PSGS')
        print(MAX_CC_PSGS)
        nq = 1
        nb = len(cc_psgs) # database size
        # Dense Passage Representation(DPR)
        if args.emb=='dense':
            subprocess.call(['emb/generate_embedding.sh', CC])
            # FAISS Preparation

            cc_embeddings = np.load('emb/' + CC + '_0.pkl', allow_pickle=True)
            if nb != len(cc_embeddings):
                print('CC Embedding generation failed.')
                continue
            d = query_embeddings[0][1].size
            xq = np.zeros((nq,d), dtype='float32')
            xq[0] = query_embeddings[i][1]
            xb = np.zeros((nb,d), dtype='float32')
            for l in range(nb):
                xb[l] = cc_embeddings[l][1]
        # if args.emb=='sparse':
        #     texts = []
        #     for dict_tr in query_psgs:
        #         texts.append(dict_tr['doc_text'])
        #     for dict_cc in cc_psgs:
        #         texts.append(dict_cc['doc_text'])
        #     emb = encode_sparse(texts)
        #     _, d = emb.shape
        #     print(emb.shape)
        #     query_embeddings = emb[:MAX_TR_PSGS]
        #     cc_embeddings = emb[MAX_TR_PSGS:]
        #     print(query_embeddings.shape)
        #     print(cc_embeddings.shape)
        #     xq = np.array(query_embeddings, dtype='float32')
        #     xb = np.array(cc_embeddings, dtype='float32')
        index = faiss.IndexFlatL2(d)   # build the index
        index.add(xb)                  # add vectors to the index
        k = nb                         # K is equal to the size of the database
        D, I = index.search(xq, k)     # actual search
        ################################################################################
        # Write Augmented Passages
        ################################################################################
        knn_indices = I[0].astype(int)
        LEN_CC_PSGS = len(knn_indices)
        sorted_cc_psgs_jsonl = []

        for j in range(LEN_CC_PSGS):
            d = {"text" : cc_psgs[knn_indices[j]]['doc_text'],
                 "label"  : "",
                 "metadata": {},
                 "score": str(D[0][j])
                 }
            sorted_cc_psgs_jsonl.append(json.dumps(d))
        with open('aug_sorted/' + args.dataset_name + '/%05d.jsonl' % i, 'w') as f:
            for j in range(len(sorted_cc_psgs_jsonl)):
                f.write(sorted_cc_psgs_jsonl[j]);
                f.write('\n')
        print('Wrote aug_sorted/%s/%05d.jsonl' % (args.dataset_name,i))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='DA')
    parser.add_argument("--max_doc", default=10, type=int, help="")
    parser.add_argument("--emb"         , default="dense" , type=str, help="")
   # parser.add_argument("--dataset_name", default="citation_intent", type=str, help="")
   # parser.add_argument("--query_files"  , default="data/citation_intent/train.jsonl", type=str, help="")
    # parser.add_argument("--dataset_name", default="hyperpartisan_news", type=str, help="")
    # parser.add_argument("--query_files"  , default="data/hyperpartisan_news/train.jsonl", type=str, help="")
    parser.add_argument("--dataset_name", default="rct-sample", type=str, help="")
    parser.add_argument("--query_files"  , default="data/rct-sample/train.jsonl", type=str, help="")
    print(parser.parse_args())
    main(parser.parse_args())
