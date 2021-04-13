import os
import json
import glob


task = 'hyperpartisan_news'
aug_unlabeled = 'aug_unlabeled'

aug_unlabeled_files = glob.glob(os.path.join(os.getcwd(), aug_unlabeled, task, "*.jsonl"))

empty_same_aug_list = []

for aug_file in aug_unlabeled_files:
	for temp_item in open(aug_file).readlines():
		temp_dict = eval(temp_item)
		#if temp_dict["text"] in empty_same_aug_list:
			#continue
		#else:
			#empty_same_aug_list.append(temp_dict["text"])
		empty_same_aug_list.append(temp_dict["text"])


print("Length of union of files is: ",len(empty_same_aug_list))
