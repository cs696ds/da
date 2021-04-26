#!/bin/bash

mkdir data/aug/rct-sample/

mkdir data/aug/rct-sample/score_max24/
mkdir data/aug/rct-sample/score_max26/
mkdir data/aug/rct-sample/score_max28/
mkdir data/aug/rct-sample/score_max30/
mkdir data/aug/rct-sample/score_max32/
mkdir data/aug/rct-sample/score_max34/
mkdir data/aug/rct-sample/score_max36/

cp task5a/rct-sample_aug/rct-sample_24.jsonl data/aug/rct-sample/score_max24/train.jsonl
cp task5a/rct-sample_aug/rct-sample_26.jsonl data/aug/rct-sample/score_max26/train.jsonl
cp task5a/rct-sample_aug/rct-sample_28.jsonl data/aug/rct-sample/score_max28/train.jsonl
cp task5a/rct-sample_aug/rct-sample_30.jsonl data/aug/rct-sample/score_max30/train.jsonl
cp task5a/rct-sample_aug/rct-sample_32.jsonl data/aug/rct-sample/score_max32/train.jsonl
cp task5a/rct-sample_aug/rct-sample_34.jsonl data/aug/rct-sample/score_max34/train.jsonl
cp task5a/rct-sample_aug/rct-sample_36.jsonl data/aug/rct-sample/score_max36/train.jsonl

cat data/rct-sample/train.jsonl >> data/aug/rct-sample/score_max24/train.jsonl
cat data/rct-sample/train.jsonl >> data/aug/rct-sample/score_max26/train.jsonl
cat data/rct-sample/train.jsonl >> data/aug/rct-sample/score_max28/train.jsonl
cat data/rct-sample/train.jsonl >> data/aug/rct-sample/score_max30/train.jsonl
cat data/rct-sample/train.jsonl >> data/aug/rct-sample/score_max32/train.jsonl
cat data/rct-sample/train.jsonl >> data/aug/rct-sample/score_max34/train.jsonl
cat data/rct-sample/train.jsonl >> data/aug/rct-sample/score_max36/train.jsonl

cp data/rct-sample/test.jsonl data/aug/rct-sample/score_max24/test.jsonl
cp data/rct-sample/test.jsonl data/aug/rct-sample/score_max26/test.jsonl
cp data/rct-sample/test.jsonl data/aug/rct-sample/score_max28/test.jsonl
cp data/rct-sample/test.jsonl data/aug/rct-sample/score_max30/test.jsonl
cp data/rct-sample/test.jsonl data/aug/rct-sample/score_max32/test.jsonl
cp data/rct-sample/test.jsonl data/aug/rct-sample/score_max34/test.jsonl
cp data/rct-sample/test.jsonl data/aug/rct-sample/score_max36/test.jsonl

cp data/rct-sample/dev.jsonl data/aug/rct-sample/score_max24/dev.jsonl
cp data/rct-sample/dev.jsonl data/aug/rct-sample/score_max26/dev.jsonl
cp data/rct-sample/dev.jsonl data/aug/rct-sample/score_max28/dev.jsonl
cp data/rct-sample/dev.jsonl data/aug/rct-sample/score_max30/dev.jsonl
cp data/rct-sample/dev.jsonl data/aug/rct-sample/score_max32/dev.jsonl
cp data/rct-sample/dev.jsonl data/aug/rct-sample/score_max34/dev.jsonl
cp data/rct-sample/dev.jsonl data/aug/rct-sample/score_max36/dev.jsonl
