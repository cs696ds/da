#!/bin/bash
python ../DPR/generate_dense_embeddings.py \
       --out_file part-19100 \
       --model_file ../DPR/checkpoint/retriever/multiset/bert-base-encoder.cp \
       --ctx_file=part-19100.tsv


