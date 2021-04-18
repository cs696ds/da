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
#from sklearn.feature_extraction.text import Tfidf5Vectorizer

def encode_sparse(X):
    encoder = TfidfVectorizer(stop_words='english', ngram_range=(1, 2), max_df=0.3)
    encoder.fit(X)
    print("Dimension: ", len(encoder.vocabulary_))
    embedding = encoder.transform(X).toarray()
    return embedding

def main(args):
#    pretty = lambda x : json.dumps(x, indent=2, sort_keys=True)
    print('Read Query Files from %s' % args.train_file)
    with open(args.train_file, 'r') as train_file:
        json_lines = []
        lines = train_file.readlines()
        for line in lines:
            j = json.loads(line)
            json_lines.append(j)

    print('Start Querying')
    #cc_psgs_jsonl = []

    print("Measure Average Token Length")
    doc_input_len_arr = []
    for i in tqdm(range(len(json_lines))):
        nlp = spacy.load("en_core_web_sm", exclude=["parser"])
        nlp.enable_pipe("senter")
        line = json_lines[i]        
        doc_input = nlp(line['text'])
        doc_input_len = 0
        for sent in doc_input.sents:
            doc_input_len += len(sent)
        doc_input_len_arr.append(doc_input_len)
    AVG_TOK_LEN = np.rint(np.mean(doc_input_len_arr))
    print('Average Token Length: %d' % AVG_TOK_LEN )
    sys.exit()


    # Process input
    solr_select = 'http://localhost:8983/solr/depcc-small/select?q='
    for i in tqdm(range(len(json_lines))):
        cc_psgs_jsonl = []
        line = json_lines[i]

        nlp = spacy.load("en_core_web_sm", exclude=["parser"])
        nlp.enable_pipe("senter")
        query_doc = nlp(line['text'])
        queries = []
        query = ""
        num_tokens = 0
        
        for sent in query_doc.sents:
            if num_tokens < 100:
                query += sent.text
                num_tokens += len(sent)
            else:
                queries.append(query)
                num_tokens = 0
                query = ""

        # QUERY PROCESSING
        cc_doc10 = ""
        for q in queries:
            q = q.replace(' ', '+')
            print(textwrap.fill(q,80))
            rp_retrieval = requests.get(solr_select + q).json()
            if 'response' not in rp_retrieval:
                continue
            cc_docs = (rp_retrieval['response']['docs'])
            if len(cc_docs) == 0:
                continue
            print('Number of retrieved documents: %d' % len(cc_docs))
            for j in range(args.max_doc):
                try:
                    cc_doc10 += json.loads(cc_docs[j]['_src_'])['text']
                except ValueError:
                    continue
                #        print("--- %s seconds ---" % (time.time() - start_time))
        if len(cc_doc10) > 1000000 or len(cc_doc10) == 0:
            continue
        nlp = spacy.load("en_core_web_sm", exclude=["parser"])
        nlp.enable_pipe("senter")
        doc = nlp(cc_doc10)
        cc_psgs = []
        psg = ''
        num_tokens = 0

        # RETRIEVAL PROCESSING
        for sent in doc.sents:
            # if num_tokens < 100:
            if num_tokens < AVG_TOK_LEN:
                psg += sent.text
                num_tokens += len(sent)
            else:
                cc_psgs.append({'doc_id' : '', 'doc_text'  : psg,  'title': ''  })
                num_tokens = 0
                psg = ''
        num_train = len(json_lines)
        train_psgs = []
        for j in range(num_train):
            train_dict = {'doc_id': str(i), 'doc_text': json_lines[i]['text'], 'title': ''}
            train_psgs.append(train_dict)
        for psg in cc_psgs:
            d = {"text" : psg['doc_text'],
                 "label"  : "",
                 "metadata": {}
            }
            cc_psgs_jsonl.append(json.dumps(d))
#        print('Start writing to ' + args.aug_file)

        with open('aug_unlabeled/' + args.dataset_name + '/%05d.jsonl' % i, 'w') as f:
            for k in tqdm(range(len(cc_psgs_jsonl))):
                f.write(cc_psgs_jsonl[k]);
                f.write('\n')
        
        # with open(args.aug_file, 'a+') as f:
        #     for i in tqdm(range(len(cc_psgs_jsonl))):
        #         f.write(cc_psgs_jsonl[i]);
        #         f.write('\n')
            
    # print('Start writing to ' + args.aug_file)
    # with open(args.aug_file, 'w') as f:
    #     for i in tqdm(range(len(cc_psgs_jsonl))):
    #         f.write(cc_psgs_jsonl[i]);
    #         f.write('\n')
    print('Done.')
    # TR = 'tr_' + args.dataset_name
    # CC = 'cc_' + args.dataset_name
    # TR_TSV  = 'emb/' + TR + '.tsv' 
    # CC_TSV  = 'emb/' + CC + '.tsv'
    # print(TR)
    # print(textwrap.fill(train_psgs[0]['doc_text'], 80))
    # print()
    # with open(TR_TSV, 'w') as output_file:
    #     dw = csv.DictWriter(output_file, train_psgs[0].keys(), delimiter='\t')
    #     for tp in train_psgs:
    #         dw.writerow(tp)
    # with open(CC_TSV, 'w') as output_file:
    #     dw = csv.DictWriter(output_file, cc_psgs[0].keys(), delimiter='\t')
    #     for psg in cc_psgs:
    #         dw.writerow(psg)
    # MAX_TR_PSGS = len(train_psgs)
    # MAX_CC_PSGS = len(cc_psgs)
    # print(MAX_TR_PSGS)
    # print(MAX_CC_PSGS)
    # nq = len(train_psgs)
    # nb = len(cc_psgs) # database size
    # if args.emb=='dense':
    #     subprocess.call(['emb/generate_embedding.sh', TR])
    #     subprocess.call(['emb/generate_embedding.sh', CC])
    #     train_embeddings = np.load('emb/' + TR + '_0.pkl', allow_pickle=True)
    #     cc_embeddings = np.load('emb/' + CC + '_0.pkl', allow_pickle=True)
    #     d = train_embeddings[0][1].size
    #     xq = np.zeros((nq,d), dtype='float32')
    #     for i in range(nq):
    #         xq[i] = train_embeddings[i][1]
    #     xb = np.zeros((nb,d), dtype='float32')
    #     for i in range(nb):
    #         xb[i] = cc_embeddings[i][1]
    # if args.emb=='sparse':
    #     texts = []
    #     for dict_tr in train_psgs:
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
    # print('Number of train passages: %d' % nq)
    # print(xq)
    # index = faiss.IndexFlatL2(d)   # build the index
    # print('trained? %r' % index.is_trained)
    # index.add(xb)                  # add vectors to the index
    # print('Total number of indexed CC passages: ', index.ntotal)
    # print()
    # print('Using an indentical CC set')
    # k = nb                          # we want to see 4 nearest neighbors
    # D, I = index.search(xb[:5], k) # sanity check
    # print('================================================================')
    # print('4 nearest neighbors')
    # print(I)
    # print()
    # print('distances(sanity check)')
    # print(D)
    # print()
    # print('===============================================================')
    # print('Using the query(train set)')
    # D, I = index.search(xq, k)     # actual search
    # print('4 nearest neighbors')
    # print(I[:5])                   # neighbors of the 5 first queries
    # print('\ndistances')
    # print(D)
    # print()
    # print('Train passage')
    # print(textwrap.fill(train_psgs[300]['doc_text'],80))
    # print()
    # print('CLOSEST passages in CC:')
    # for i in range(4):
    #     print('-------------------------------------------------------------')
    #     print('Closest %d' % i)
    #     closest = I[300][i]
    #     print(textwrap.fill(cc_psgs[closest]['doc_text'], 80))
    #     print('------------------------------------------------------------')
    # print('...')
    # for i in range(MAX_CC_PSGS-4, MAX_CC_PSGS):
    #     print('-------------------------------------------------------------')
    #     print('Farthest %d' % i)
    #     closest = I[300][i]
    #     print(textwrap.fill(cc_psgs[closest]['doc_text'],80))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='DA')
    parser.add_argument("--max_doc", default=1, type=int, help="")    
    #    parser.add_argument("--dataset_name", default="02_acl"                     , type=str, help="")
    parser.add_argument("--dataset_name", default="04_hyper"                     , type=str, help="")
    #    parser.add_argument("--dataset_name", default="07_imdb"                     , type=str, help="")
    #    parser.add_argument("--train_file"  , default="data/02-acl-arc/train.jsonl", type=str, help="")
    #    parser.add_argument("--train_file"  , default="failed_tests_by_base_models/failed_citation_intent.jsonl", type=str, help="")
    parser.add_argument("--train_file"  , default="failed_tests_by_base_models/failed_hyperpartisan_news.jsonl", type=str, help="")
    #    parser.add_argument("--train_file"  , default="failed_tests_by_base_models/failed_imdb.jsonl", type=str, help="")
    #    parser.add_argument("--aug_file"    , default="aug_unlabeled/aug_unlabeled_citation_intent.jsonl", type=str, help="")
    #    parser.add_argument("--aug_file"    , default="aug_unlabeled/aug_hyperpartisan_news.jsonl", type=str, help="")
    #    parser.add_argument("--aug_file"    , default="aug_unlabeled/aug_imdb.jsonl", type=str, help="")
    #    parser.add_argument("--emb"         , default="dense" , type=str, help="")
    print(parser.parse_args())
    main(parser.parse_args())
