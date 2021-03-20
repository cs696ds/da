#!/bin/bash
#/home/heeh/Projects/da/emb

#PROJ_HOME="/home/heeh/Projects"
PROJ_HOME="/mnt/nfs/work1/696ds-s21/hhwang"

python ${PROJ_HOME}/DPR/generate_dense_embeddings.py \
       --out_file "${PROJ_HOME}/da/emb/${1}" \
       --model_file "${PROJ_HOME}/DPR/data/checkpoint/retriever/multiset/bert-base-encoder.cp" \
       --ctx_file="${PROJ_HOME}/da/emb/${1}.tsv"
