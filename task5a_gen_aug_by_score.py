import sys
import json
dataset_name  = 'rct-sample'
in_file       = 'task5a/rct-sample_sorted_dedup.jsonl'
out_file_path = 'task5a/rct-sample_aug/'
seen = set()
with open(in_file) as f:
    json_lines = []
    for line in f:
        json_line = json.loads(line)
        json_lines.append(json_line)

    NUM_LINES = len(json_lines)
    print(NUM_LINES)

    scores = [24, 26, 28, 30, 32, 34, 36]
    scores_str = [str(s) for s in scores]
    print(scores)
    print(scores_str)
    jsons = {}
    for s in scores_str:
        jsons[s] = []

    for json_line in json_lines:
        for s in scores_str:
            if float(json_line['score']) < float(s):
                jsons[s].append(json_line)

    for s in jsons.keys():
        print(len(jsons[s]))

for s in scores_str:
    with open(out_file_path + dataset_name + '_' + s + '.jsonl', 'w') as f:
        for json_line in jsons[s]:
            f.write('%s\n' % json.dumps(json_line))
    
