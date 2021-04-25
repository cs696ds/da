import sys
import json
input_file_path = 'aug_citation_intent_all_sorted_and_rm_dups.jsonl'
output_file_path = 'bm25/citation_intent_bm25_'
seen = set()
with open(input_file_path) as f:
    json_lines = []
    for line in f:
        json_line = json.loads(line)
        json_lines.append(json_line)

    NUM_LINES = len(json_lines)
    print(NUM_LINES)



    scores = [24, 26, 28, 30, 32, 34]
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
    with open(output_file_path + s + '.jsonl', 'w') as f:
        for json_line in jsons[s]:
            f.write('%s\n' % json.dumps(json_line))
    
