from tqdm import tqdm
import os
import json
import glob

tasks = ['hyperpartisan_news']

query_file    = "data/hyperpartisan_news/train.jsonl"
aug_unlabeled = "aug_sorted"
annotation    = "same_label"
out_dir       = 'task5a'

for task in tasks:
    print("Processing task: ",task)
    aug_unlabeled_files = glob.glob(os.path.join(os.getcwd(), aug_unlabeled, task, "*.jsonl"))
    query_path_fileptr = open(query_file)
    query_path_data = query_path_fileptr.readlines()
    #count = 0
    #total = 0
    empty_same_aug_list = []
    for i in tqdm(range(len(query_path_data))):
        if os.path.join(os.getcwd(), aug_unlabeled, task, '%05d.jsonl'%i) in aug_unlabeled_files:
            query_json = eval(query_path_data[i])
            for temp_item in open(os.path.join(os.getcwd(), aug_unlabeled, task, '%05d.jsonl'%i)).readlines():
                empty_dict = {}
                empty_dict["text"] = eval(temp_item)["text"]
                empty_dict["score"] = eval(temp_item)["score"]                
                empty_dict["label"] = query_json["label"]
                if json.dumps(empty_dict) in empty_same_aug_list:
                    continue
                else:
                    empty_same_aug_list.append(json.dumps(empty_dict))
#                    print("Length of augmented data for ",task," is ",len(empty_same_aug_list))
    with open(os.path.join(out_dir, annotation + "_" + task + ".jsonl"), 'w') as filewriter:
        for item in empty_same_aug_list:
            filewriter.write('%s\n' % item)
