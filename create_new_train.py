import os
import json
import glob

tasks = ['hyperpartisan_news', 'citation_intent', 'imdb']

train = "data"
same_label = "same_label"
new_train_same_label = "new_train_same_label"

for task in tasks:
	print("Processing task: ",task)
	train_data = open(os.path.join(train, task, "train.jsonl")).readlines()
	same_label_data = open(os.path.join(same_label, task, same_label + "_" + task + ".jsonl")).readlines()
	
	temp_new_train = []
	for data_coll in [train_data, same_label_data]:
		for item in data_coll:
			temp_new_train.append(json.dumps(eval(item)))

	print("Length of new train set is: ",len(temp_new_train))

	with open(os.path.join(new_train_same_label, task, "same_label_newtrain.jsonl"), 'w') as filewriter:
		for item in temp_new_train:
			filewriter.write('%s\n' % item)