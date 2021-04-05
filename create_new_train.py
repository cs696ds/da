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
	train_data.extend(same_label_data)
	print("Length of new train set is: ",len(train_data))

	with open(os.path.join(new_train_same_label, task, "same_label_newtrain.jsonl"), 'w') as filewriter:
		for item in train_data:
			filewriter.write('%s\n' % item)