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

def main(args):
    TR = 'tr_' + args.dataset_name
    CC = 'cc_' + args.dataset_name
    TRAIN_PATH  = args.train_file
    TR_TSV  = 'emb/' + TR + '.tsv' 
    CC_TSV  = 'emb/' + CC + '.tsv'
    
    start_time = time.time()
    pretty = lambda x : json.dumps(x, indent=2, sort_keys=True)
    solr_select = 'http://localhost:8983/solr/depcc-small/select?q='
    with open(TRAIN_PATH, 'r') as train_file:
        json_lines = []
        lines = train_file.readlines()
        for line in lines:
            j = json.loads(line)
            json_lines.append(j)
            N = len(json_lines)
    j = json_lines[0]
    query = j['text'].replace(' ', '+')
    print(query)
    rp_retrieval = requests.get(solr_select + query).json()
    cc_docs = (rp_retrieval['response']['docs'])
    print('Number of retrieved documents: %d' % len(cc_docs))
    cc_doc0 = json.loads(cc_docs[0]['_src_'])
    cc_doc100 = ""
    for i in range(10):
        cc_doc100 += json.loads(cc_docs[i]['_src_'])['text']
    print("--- %s seconds ---" % (time.time() - start_time))
    nlp = spacy.load("en_core_web_sm", exclude=["parser"])
    nlp.enable_pipe("senter")
    doc = nlp(cc_doc100)
    cc_psgs = []
    psg = ''
    num_tokens = 0
    for sent in doc.sents:
        if num_tokens < 100:
            psg += sent.text
            num_tokens += len(sent)
        else:
            cc_psgs.append({'doc_id' : '', 'doc_text'  : psg,  'title': ''  })
            num_tokens = 0
            psg = ''
    num_train = len(json_lines)
    train_psgs = []
    for i in range(num_train):
        train_dict = {'doc_id': str(i), 'doc_text': json_lines[i]['text'], 'title': ''}
        train_psgs.append(train_dict)
    print(TR)
    print(train_psgs[0]['doc_text'])
    print()
    with open(TR_TSV, 'w') as output_file:
        dw = csv.DictWriter(output_file, train_psgs[0].keys(), delimiter='\t')
        for tp in train_psgs:
            dw.writerow(tp)
    with open(CC_TSV, 'w') as output_file:
        dw = csv.DictWriter(output_file, cc_psgs[0].keys(), delimiter='\t')
        for psg in cc_psgs:
            dw.writerow(psg)
#            print(CC)
#            print(cc_psgs[0]['doc_text'])

    
    subprocess.call(['emb/generate_embedding.sh', TR])
    subprocess.call(['emb/generate_embedding.sh', CC]) 

    MAX_TR_PSGS = len(train_psgs)
    MAX_CC_PSGS = len(cc_psgs)
    print(MAX_TR_PSGS)
    print(MAX_CC_PSGS)
    cc_embeddings = np.load('emb/' + CC + '_0.pkl', allow_pickle=True)
    print(cc_embeddings[0][1].shape)  # Dimension of the embedding
    nb = len(cc_embeddings) # database size
    d = cc_embeddings[0][1].size
    print(nb,d)
    xb = np.zeros((nb,d), dtype='float32')
    for i in range(nb):
        xb[i] = cc_embeddings[i][1]
    train_embeddings = np.load('emb/' + TR + '_0.pkl', allow_pickle=True)
    print(train_embeddings[0][1].shape)  # Dimension of the embedding
    nq = len(train_embeddings)
    d = train_embeddings[0][1].size
    print(nq,d)
    xq = np.zeros((nq,d), dtype='float32')
    for i in range(nq):
        xq[i] = train_embeddings[i][1]
    print('Number of train passages: %d' % nq)
    print(xq)
    index = faiss.IndexFlatL2(d)   # build the index
    print('trained? %r' % index.is_trained)
    index.add(xb)                  # add vectors to the index
    print('Total number of indexed CC passages: ', index.ntotal)
    print()
    print('Using an indentical CC set')
    k = nb                          # we want to see 4 nearest neighbors
    D, I = index.search(xb[:5], k) # sanity check
    print('================================================================')
    print('4 nearest neighbors')
    print(I)
    print()
    print('distances(sanity check)')
    print(D)
    print()
    print('===============================================================')
    print('Using the query(train set)')
    D, I = index.search(xq, k)     # actual search
    print('4 nearest neighbors')
    print(I[:5])                   # neighbors of the 5 first queries
    print('\ndistances')
    print(D)
    print()
    print('Train passage')
    print(train_psgs[300]['doc_text'])
    print()
    print('CLOSEST passages in CC:')
    for i in range(4):
        print('-------------------------------------------------------------')
        print('Closest %d' % i)
        closest = I[300][i]
        print(textwrap.fill(cc_psgs[closest]['doc_text'], 80))
        print('------------------------------------------------------------')
        print('...')
    for i in range(MAX_CC_PSGS-4, MAX_CC_PSGS):
        print('-------------------------------------------------------------')
        print('Farthest %d' % i)
        closest = I[300][i]
        print(textwrap.fill(cc_psgs[closest]['doc_text'],80))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Data Augmentation Pipeline')
    parser.add_argument("--dataset_name", default="02_acl"                     , type=str, help="")
    parser.add_argument("--train_file"  , default="data/02-acl-arc/train.jsonl", type=str, help="")
    parser.add_argument("--dev_file"    , default="data/02-acl-arc/dev.jsonl"  , type=str, help="")
    parser.add_argument("--test_file"   , default="data/02-acl-arc/test.jsonl" , type=str, help="")    
    print(parser.parse_args())
    main(parser.parse_args())
