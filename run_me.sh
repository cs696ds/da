#!/bin/bash
# python main.py --emb=dense  --dataset_name=02_acl   --train_file=data/02-acl-arc/train.jsonl > 02_acl_dense.txt
# python main.py --emb=sparse --dataset_name=02_acl   --train_file=data/02-acl-arc/train.jsonl > 02_acl_sparse.txt
# python main.py --emb=dense  --dataset_name=04_hyper --train_file=data/04-hyper/train.jsonl   > 04_hyper_dense.txt
# python main.py --emb=sparse --dataset_name=04_hyper --train_file=data/04-hyper/train.jsonl   > 04_hyper_sparse.txt
# python main.py --emb=dense  --dataset_name=07_imdb  --train_file=data/07-imdb/train.jsonl    > 07_imdb_dense.txt
# python main.py --emb=sparse --dataset_name=07_imdb  --train_file=data/07-imdb/train.jsonl    > 07_imdb_sparse.txt

python main.py --emb=dense  --dataset_name=02_acl   
python main.py --emb=sparse --dataset_name=02_acl   
python main.py --emb=dense  --dataset_name=04_hyper 
python main.py --emb=sparse --dataset_name=04_hyper 
python main.py --emb=dense  --dataset_name=07_imdb  
python main.py --emb=sparse --dataset_name=07_imdb  

