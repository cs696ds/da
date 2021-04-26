import sys
import json
in_file = 'task5a/hyper_all.jsonl'
out_file = 'task5a/hyper_sorted_dedup.jsonl'
seen = set()

json_lines = []
out_json_lines = []            
with open(in_file) as f:
    for line in f:
        json_line = json.loads(line)
        json_lines.append(json_line)

NUM_LINES = len(json_lines)
for i in range(NUM_LINES):
    if json_lines[i]['text'] not in seen:
        seen.add(json_lines[i]['text'])
        out_json_lines.append(json_lines[i])

sorted_out = sorted(out_json_lines, key = lambda k: float(k['score']))

with open(out_file, 'w') as f:
    for item in sorted_out:
        f.write('%s\n' % json.dumps(item))
    
