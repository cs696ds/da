import time
import math
import sys
import os
from allennlp.data.tokenizers.word_tokenizer import WordTokenizer


wt = WordTokenizer()

LIMIT = 1
for i in range(int(sys.argv[1]), int(sys.argv[1]) + LIMIT):
    tokenized_strs = []
    with open('part-%05d' % i, 'r') as f:
        data = f.read().split('\n')

    data = [x for x in data if len(x.strip()) > 0 and x.startswith("# newdoc") is False]

    start = time.time()
    for i, d in enumerate(data):
        if i == 295013:
            continue
        print('%d / %d' % (i, len(data)))
        tokenized_strs.append(wt.tokenize(d))
    print("%.4f seconds for %d" % (time.time() - start, i))

    final_data = [' '.join([y.text for y in x]) for x in tokenized_strs]

    with open('depcc.%05d-of-19101' % i, 'w') as f:
        f.write('\n'.join(final_data))

    os.remove('part-%05d' % i)
