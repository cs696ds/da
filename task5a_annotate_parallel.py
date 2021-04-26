import os
import json
import glob
import multiprocessing
from tqdm import tqdm




tasks      = ['hyperpartisan_news']
query_dir  = "data/hyperpartisan_news/train.jsonl"
aug_dir    = "aug_sorted"
annotation = "same_label"
output_dir = 'task5a'

def annotate_same_label(startIdx, endIdx):
    for task in tasks:
        print("Processing task: ",task)
        aug_dir_files = glob.glob(os.path.join(os.getcwd(), aug_dir, task, "*.jsonl"))
        query_path = os.path.join(os.getcwd(), query_dir)
        query_path_fileptr = open(query_path)
        query_path_data = query_path_fileptr.readlines()
        #count = 0
        #total = 0
        empty_same_aug_list = []
        json_length = endIdx - startIdx
        for i in tqdm(range(startIdx, endIdx)):
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
        with open(output_dir + "/" + task + str(startIdx) + ".jsonl", 'w') as filewriter:
            for item in empty_same_aug_list:
                filewriter.write('%s\n' % item)

def main():
    NUM_QUERIES = 516
    p = [None] * 10
    unit = NUM_QUERIES // 10
    for i in range(10):
        startIdx = i * unit
        endIdx   = startIdx + unit
        print(startIdx, endIdx)
        p[i] = multiprocessing.Process(target=annotate_same_label, args=(startIdx,endIdx, ))
        p[i].start()
    p_last = multiprocessing.Process(target=annotate_same_label, args=(unit * 10, NUM_QUERIES, ))
    p_last.start()
    print(unit * 10, NUM_QUERIES)
    for i in range(10):
        p[i].join()
    p_last.join()
    print("Done!")
main()

                        

