import pdb
import sys
import json
import csv
LIMIT = 1

full_path  = sys.argv[1]
print(full_path)

file_name = str(full_path.split('/')[-1])
print(file_name)

data_dir = '/'.join(full_path.split('/')[:-1])
print(data_dir)
                   
input_name = file_name.split('.')[0]
print(input_name)


with open(full_path, 'r') as input_file:
    json_lines = []
    lines = input_file.readlines()
    for line in lines:
        j = json.loads(line)
        json_lines.append(j)

N = len(json_lines)


for i in range(N):
    print(i)
    # if i != 0:
    #     sys.exit(0)
    with open(data_dir + '/txt/' + input_name + '-%05d.txt'   % i, 'w') as output_file:
        output_file.write(json_lines[i]['text'])



