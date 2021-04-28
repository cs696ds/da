import sys
import json
# dataset_name  = 'citation_intent'
# in_file       = 'task5a/citation_intent_aug/aug_citation_intent_all_sorted_and_rm_dups.jsonl'
# out_file_path = 'task5a/'
# NUM_LINES = 1688

# dataset_name  = 'hyperpartisan_news'
# in_file       = 'task5a/hyper_aug/hyper_sorted_dedup.jsonl'
# out_file_path = 'task5a/'
# NUM_LINES = 516

dataset_name  = 'rct-sample'
in_file       = 'task5a/rct-sample_aug/rct-sample_sorted_dedup.jsonl'
out_file_path = 'task5a/'
NUM_LINES = 500


with open(in_file) as f:
    json_lines = []
    for line in f:
        json_line = json.loads(line)
        json_lines.append(json_line)


    print(NUM_LINES)

    ratios = [0,3,6,9,12,15,18,21,24,27,30]
    print(ratios)
    jsons = {}

    for i in range(len(ratios)-1):
        startIdx = NUM_LINES // 100 * ratios[i]
        endIdx   = NUM_LINES // 100 * ratios[i+1]
        jsons[str(ratios[i]) + '-' + str(ratios[i+1])] = json_lines[startIdx:endIdx]

    for s in jsons.keys():
        print(len(jsons[s]))

for i in range(len(ratios)-1):
    with open(out_file_path + dataset_name + '_' + str(i) + '.jsonl', 'w') as f:
        for json_line in jsons[str(ratios[i]) + '-' + str(ratios[i+1])]:
            f.write('%s\n' % json.dumps(json_line))
    
