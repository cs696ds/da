import os
import json
import glob

tasks = ['hyperpartisan_news', 'citation_intent', 'imdb']
aug_unlabeled = 'aug_unlabeled'
s2_data = 's2_data'

for task in tasks:
	aug_unlabeled_files = glob.glob(os.path.join(os.getcwd(), aug_unlabeled, task, "*.jsonl"))
	empty_same_aug_list = []

	output_file = os.path.join(os.getcwd(), s2_data, task, "aug_"+task+".jsonl")

	for aug_file in aug_unlabeled_files:
		for temp_item in open(aug_file).readlines():
			temp_dict = eval(temp_item)
			temp1_dict = {}
			temp1_dict["text"] = temp_dict["text"]
			temp1_dict["label"] = temp_dict["label"]
			if json.dumps(temp1_dict) in empty_same_aug_list:
				continue
			else:
				empty_same_aug_list.append(json.dumps(temp1_dict))

	print("Length of union of files for %s is %d"%(task, len(empty_same_aug_list)))

	with open(output_file, 'w') as filewriter:
		for item in empty_same_aug_list:
			filewriter.write('%s\n' % item)
