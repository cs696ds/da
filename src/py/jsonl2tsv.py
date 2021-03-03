import pdb
import sys
import json
import csv
LIMIT = 1


def jsonl2tsv():
    for i in range(int(sys.argv[1]), int(sys.argv[1]) + LIMIT):
        json_lines = []
        with open('part-%05d.jsonl' % i, 'r') as f:
            lines = f.readlines()
            for line in lines:
                j = json.loads(line)
                json_lines.append(j)
        with open('part-%05d.tsv'   % i, 'w') as output_file:
            dw = csv.DictWriter(output_file, json_lines[0].keys(), delimiter='\t')
            dw.writeheader()
            for j in json_lines:
                dw.writerow(j)
                
json2tsv()
