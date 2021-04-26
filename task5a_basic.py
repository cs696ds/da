import os
import json
import glob
from tqdm import tqdm



tasks = ['citation_intent']
query_dir = "data/citation_intent/train.jsonl"
aug_dir = "aug_sorted"
annotation = "same_label"
output_dir = 'output_task5a'
for task in tasks:
    print("Processing task: ",task)
    aug_dir_files = glob.glob(os.path.join(os.getcwd(), aug_dir, task, "*.jsonl"))
    query_path = os.path.join(os.getcwd(), query_dir)
    query_path_fileptr = open(query_path)
    query_path_data = query_path_fileptr.readlines()
    #count = 0
    #total = 0
    empty_same_aug_list = []
    for i in tqdm(range(len(query_path_data))):
        if os.path.join(os.getcwd(), aug_dir, task, '%05d.jsonl'%i) in aug_dir_files:
            query_dict = eval(query_path_data[i])
            for temp_item in open(os.path.join(os.getcwd(), aug_dir, task, '%05d.jsonl'%i)).readlines():
                empty_dict = {}
                empty_dict["text"]  = eval(temp_item)["text"]
                empty_dict["score"] = eval(temp_item)["score"]
                empty_dict["label"] = query_dict["label"]

                if json.dumps(empty_dict) in empty_same_aug_list:
                    continue
                else:
                    empty_same_aug_list.append(json.dumps(empty_dict))
    print("Length of augmented data for ",task," is ",len(empty_same_aug_list))
    with open(os.path.join(output_dir, task, annotation + "_" + task + ".jsonl"), 'w') as filewriter:
        for item in empty_same_aug_list:
            filewriter.write('%s\n' % item)
