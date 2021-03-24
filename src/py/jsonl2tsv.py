import pdb
import sys
import json
import csv
LIMIT = 1


def jsonl2tsv_load(f_in) -> list():

    json_lines = []
    with open(f_in, 'r') as f:
        lines = f.readlines()
        for line in lines:
            j = json.loads(line)
            json_lines.append(j)
    return json_lines

def jsonl2tsv_write(json_lines, f_out) -> None:
    with open(f_out, 'w') as output_file:
        dw = csv.DictWriter(output_file, json_lines[0].keys(), delimiter='\t')
        dw.writeheader()
        for j in json_lines:
            dw.writerow(j)
    
def jsonl2tsv():
    #for i in range(int(sys.argv[1]), int(sys.argv[1]) + LIMIT):
    json_lines = jsonl2tsv_load('sample.jsonl')
    jsovl2tsv_write(json_lines, 'sample.tsv')
