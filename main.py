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
    print('NUM_RAW_QUERIES: %d' % NUM_RAW_QUERIES)
    
    ################################################################################
    # Measure Average Token Length
    ################################################################################
    print("Measure Average Token Length")
    qlen_vec   = []
    query_docs = []
    query_raws  = []
#    NUM_RAW_QUERIES = 10
    for i in tqdm(range(NUM_RAW_QUERIES)):
        cur_len = 0
        q_tok = sent_tokenize(json_lines[i]['text'])
        qlen_vec.append(len(q_tok))
        query_docs.append(q_tok)
    AVG_TOK_LEN = np.rint(np.mean(qlen_vec))
    print('Average Token Length: %d' % AVG_TOK_LEN )
    ################################################################################
    # Segment Raw Queries
    ################################################################################
    for i in tqdm(range(NUM_RAW_QUERIES)):
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
        solr_select = 'http://localhost:8983/solr/depcc-large/select?q='
        # solr_select = 'http://localhost:8983/solr/depcc-small/select?q='
        # solr_select = 'http://localhost:8983/solr/depcc-large/select?q='
        #    solr_select = 'http://localhost:8983/solr/depcc-small/select?fl=score%2C*&q='
        cc_psgs = []
        print('Process NUM_SEG_QUERIES: %d' % NUM_SEG_QUERIES)
        for j in range(NUM_SEG_QUERIES):
            q = seg_queries[j].replace(' ', '+')
            retrieved = requests.get(solr_select + q).json()
            if 'response' not in retrieved:
                continue
            retrieved_docs = (retrieved['response']['docs'])
            if len(retrieved_docs) == 0:
                continue
            cc_docs_raw = ""
            for k in range(args.max_doc):
                try:
                    cur = json.loads(retrieved_docs[k]['_src_'])['text']
                    #print(retrieved_docs[k]['_src_'])
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
            # print(cc_docs_raw)
            # print(cc_docs_tok)
            # print(len(cc_docs_tok))
            if len(cc_docs_tok) < 100:
                cc_psgs.append({'doc_id' : '', 'doc_text'  : cc_docs_raw,  'title': ''  })
            else:
                temp = ''
                num_tokens = 0
                for sent in cc_docs_tok.sents:
                    #print(sent.text)
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

        # END of for j in tqdm(range(NUM_SEG_QUERIES)):
        #print('Length of cc_psgs')
        #print(len(cc_psgs))
        # for c in cc_psgs:
        #     print(c)
        #     print()
        ################################################################################
        # Prepare Train and CC passages for sorting
        ################################################################################

        # Per raw query
        query_psgs = []
        query_dict = {'doc_id': str(i), 'doc_text': json_lines[i]['text'], 'title': ''}
        query_psgs.append(query_dict)

        # print(query_psgs[0]['doc_text'][:50])
        # print(cc_psgs[0]['doc_text'][:50])

        TR = 'tr_' + args.dataset_name
        CC = 'cc_' + args.dataset_name
        TR_TSV  = 'emb/' + TR + '.tsv' 
        CC_TSV  = 'emb/' + CC + '.tsv'
        #print(TR)
        #print(textwrap.fill(query_psgs[0]['doc_text'], 80))
        #print()
        with open(TR_TSV, 'w') as q_csv_file:
            q_dw = csv.DictWriter(q_csv_file, query_psgs[0].keys(), delimiter='\t')
            for q_psg in query_psgs:
                q_dw.writerow(q_psg)
        with open(CC_TSV, 'w') as cc_csv_file:
            cc_dw = csv.DictWriter(cc_csv_file, cc_psgs[0].keys(), delimiter='\t')
            for cc_psg in cc_psgs:
                cc_dw.writerow(cc_psg)
        MAX_TR_PSGS = len(query_psgs)
        MAX_CC_PSGS = len(cc_psgs)
        print('MAX_TR_PSGS')
        print(MAX_TR_PSGS)
        print('MAX_CC_PSGS')
        print(MAX_CC_PSGS)
        nq = len(query_psgs)  # query size
        nb = len(cc_psgs) # database size
        
        if args.emb=='dense':
            subprocess.call(['emb/generate_embedding.sh', TR])
            subprocess.call(['emb/generate_embedding.sh', CC])
            train_embeddings = np.load('emb/' + TR + '_0.pkl', allow_pickle=True)
            cc_embeddings = np.load('emb/' + CC + '_0.pkl', allow_pickle=True)
            d = train_embeddings[0][1].size
            xq = np.zeros((nq,d), dtype='float32')
            for l in range(nq):
                xq[l] = train_embeddings[l][1]
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
        #     train_embeddings = emb[:MAX_TR_PSGS]
        #     cc_embeddings = emb[MAX_TR_PSGS:]
        #     print(train_embeddings.shape)
        #     print(cc_embeddings.shape)
        #     xq = np.array(train_embeddings, dtype='float32')
        #     xb = np.array(cc_embeddings, dtype='float32')
        # print('Number of query passages: %d' % nq)
        # print(xq)
        index = faiss.IndexFlatL2(d)   # build the index
        # print('trained? %r' % index.is_trained)
        index.add(xb)                  # add vectors to the index

        # print('Total number of indexed CC passages: ', index.ntotal)
        # print()
        # print('Using an indentical CC set')
        # k = nb                          # we want to see 4 nearest neighbors
        # D, I = index.search(xb[:5], k) # sanity check
        # print('================================================================')
        # print('4 nearest neighbors(sanity check)')
        # print(I)
        # print()
        # print('distances(sanity check)')
        # print(D)
        # print()
        
        # print('===============================================================')
        # print('Using the query')
        k = nb
        D, I = index.search(xq, k)     # actual search
        # print('Nearest neighbors for query')
        # print(I)                 
        # print('\ndistances')
        # print(D)
        # print()
        # print('Train passage')
        # print(textwrap.fill(query_psgs[0]['doc_text'],80))
        # print()
        
        # print('CLOSEST passages in CC:')
        # for l in range(4):
        #     print('-------------------------------------------------------------')
        #     print('Closest %d' % i)
        #     closest = I[0][l]
        #     print(textwrap.fill(cc_psgs[closest]['doc_text'], 80))
        #     print('------------------------------------------------------------')
        # print('...')
        # for l in range(MAX_CC_PSGS-4, MAX_CC_PSGS):
        #     print('-------------------------------------------------------------')
        #     print('Farthest %d' % i)
        #     closest = I[0][l]
        #     print(textwrap.fill(cc_psgs[closest]['doc_text'],80))


        ################################################################################
        # Write Augmented Passages
        ################################################################################
        knn_indices = I[0].astype(int)
        #        print(knn_indices)
        cc_psgs_jsonl = []
        for psg in cc_psgs:
            d = {"text" : psg['doc_text'],
                 "label"  : "",
                 "metadata": {}
                 }
            cc_psgs_jsonl.append(json.dumps(d))
        with open('aug_sorted/' + args.dataset_name + '/%05d.jsonl' % i, 'w') as f:
            for k in knn_indices:
                f.write(cc_psgs_jsonl[k]);
                f.write('\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='DA')
    parser.add_argument("--max_doc", default=1, type=int, help="")    
    parser.add_argument("--dataset_name", default="citation_intent", type=str, help="")
#    parser.add_argument("--dataset_name", default="hyperpartisan_news"                     , type=str, help="")
    #    parser.add_argument("--dataset_name", default="imdb"                     , type=str, help="")
#    parser.add_argument("--query_files"  , default="data/citation_intent/train.jsonl", type=str, help="")
#parser.add_argument("--query_files"  , default="failed_tests_by_base_models/failed_citation_intent.jsonl", type=str, help="")
    # parser.add_argument("--query_files"  , default="failed_tests_by_base_models/failed_hyperpartisan_news.jsonl", type=str, help="")
    parser.add_argument("--query_files"  , default="data/citation_intent/train.jsonl", type=str, help="")
    #    parser.add_argument("--query_files"  , default="failed_tests_by_base_models/failed_imdb.jsonl", type=str, help="")
    # parser.add_argument("--aug_unlabeled"  , default="aug_unlabeled/citation_intent", type=str, help="")
    # parser.add_argument("--aug_sorted"  , default="aug_sorted/citation_intent", type=str, help="")
    parser.add_argument("--emb"         , default="dense" , type=str, help="")
    print(parser.parse_args())
    main(parser.parse_args())
