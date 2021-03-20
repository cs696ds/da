import pdb
import json
import time
import math
import sys
import os
from allennlp.data.tokenizers.word_tokenizer import WordTokenizer


wt = WordTokenizer()

LIMIT = 10
for i in range(int(sys.argv[1]), int(sys.argv[1]) + LIMIT):
    with open('../../../depcc_uncompressed/part-%05d' % i, 'r') as f:
        data = f.read().split('\n')

    data = [x for x in data if len(x.strip()) > 0]
    start = time.time()
    docs = [] 
    val_url  = ""
    val_s3   = ""
    val_text = ""
    k = 0  # The number of documents
    for j, d in enumerate(data):
        # if k == 10:
        #     break
#        print('%d / %d' % (j, len(data)))
        if d.startswith("# newdoc"):
            pos = d.find('s3 =')
            val_url = d[14:pos].strip()
            val_s3  = d[pos + 4:].strip()
            if len(val_text.strip()) > 0:
                dict = {"url" : val_url,
                        "s3"  : val_s3,
                        "text": val_text
                }
                docs.append(json.dumps(dict))
                val_url = ""
                val_text = ""
                k += 1
        else:
            tokenized_str = wt.tokenize(d)
            line = ' '.join(w.text for w in tokenized_str)
            line += ' '
            val_text += line

    with open('../../data/99-depcc/etc/part-%05d.jsonl' % i, 'w') as f:
        for doc in docs:
            f.write(doc);
            f.write('\n')
            
    print("%.4f seconds for %d" % (time.time() - start, i))

#    final_data = [' '.join([y.text for y in x]) for x in tokenized_strs]

    # with open('depcc.%05d-of-19101' % i, 'w') as f:
    #     f.write('\n'.join(final_data))

#    os.remove('part-%05d' % i)
