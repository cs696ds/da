import os
import json
import glob

tasks = ['hyperpartisan_news', 'citation_intent', 'imdb']

failed_tests_path_dir = "failed_tests_by_base_models"
aug_unlabeled = "aug_unlabeled"
same_label = "same_label"


for task in tasks:
	print("Processing task: ",task)

	aug_unlabeled_files = glob.glob(os.path.join(os.getcwd(), aug_unlabeled, task, "*.jsonl"))
	failed_test_path = os.path.join(os.getcwd(), failed_tests_path_dir, "failed_"+task+".jsonl")

	failed_test_path_fileptr = open(failed_test_path)
	failed_test_path_data = failed_test_path_fileptr.readlines()

	#count = 0
	#total = 0

	empty_same_aug_list = []

	for i in range(len(failed_test_path_data)):
		if os.path.join(os.getcwd(), aug_unlabeled, task, '%05d.jsonl'%i) in aug_unlabeled_files:
			temp_dict = eval(failed_test_path_data[i])
			for temp_item in open(os.path.join(os.getcwd(), aug_unlabeled, task, '%05d.jsonl'%i)).readlines():
				empty_dict = {}
				empty_dict["text"] = eval(temp_item)["text"]
				empty_dict["label"] = temp_dict["label"]
				empty_same_aug_list.append(json.dumps(empty_dict))

	print("Length of augmented data for ",task," is ",len(empty_same_aug_list))

	with open(os.path.join(same_label, task, same_label + "_" + task + ".jsonl"), 'w') as filewriter:
		for item in empty_same_aug_list:
			filewriter.write('%s\n' % item)
			#count = count + 1
		#total = total + 1
	#print("Counted ",count," for failed ",task)
	#print("Out of ",total)