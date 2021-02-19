#!/bin/bash
python generate_dense_embeddings.py \
       --out_file part-19100.out \
       --model_file checkpoint/retriever/multiset/bert-base-encoder.cp \
       --ctx_file=part-19100.tsv
