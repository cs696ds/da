#!/bin/bash

#mkdir data/aug/rct-sample/

mkdir data/aug/rct-sample/ratio0/
mkdir data/aug/rct-sample/ratio1/
mkdir data/aug/rct-sample/ratio2/
mkdir data/aug/rct-sample/ratio3/
mkdir data/aug/rct-sample/ratio4/
mkdir data/aug/rct-sample/ratio5/
mkdir data/aug/rct-sample/ratio6/
mkdir data/aug/rct-sample/ratio7/
mkdir data/aug/rct-sample/ratio8/
mkdir data/aug/rct-sample/ratio9/

cp task5a/rct-sample_0.jsonl data/aug/rct-sample/ratio0/train.jsonl
cp task5a/rct-sample_1.jsonl data/aug/rct-sample/ratio1/train.jsonl
cp task5a/rct-sample_2.jsonl data/aug/rct-sample/ratio2/train.jsonl
cp task5a/rct-sample_3.jsonl data/aug/rct-sample/ratio3/train.jsonl
cp task5a/rct-sample_4.jsonl data/aug/rct-sample/ratio4/train.jsonl
cp task5a/rct-sample_5.jsonl data/aug/rct-sample/ratio5/train.jsonl
cp task5a/rct-sample_6.jsonl data/aug/rct-sample/ratio6/train.jsonl
cp task5a/rct-sample_7.jsonl data/aug/rct-sample/ratio7/train.jsonl
cp task5a/rct-sample_8.jsonl data/aug/rct-sample/ratio8/train.jsonl
cp task5a/rct-sample_9.jsonl data/aug/rct-sample/ratio9/train.jsonl

cat data/rct-sample/train.jsonl >> data/aug/rct-sample/ratio0/train.jsonl
cat data/rct-sample/train.jsonl >> data/aug/rct-sample/ratio1/train.jsonl
cat data/rct-sample/train.jsonl >> data/aug/rct-sample/ratio2/train.jsonl
cat data/rct-sample/train.jsonl >> data/aug/rct-sample/ratio3/train.jsonl
cat data/rct-sample/train.jsonl >> data/aug/rct-sample/ratio4/train.jsonl
cat data/rct-sample/train.jsonl >> data/aug/rct-sample/ratio5/train.jsonl
cat data/rct-sample/train.jsonl >> data/aug/rct-sample/ratio6/train.jsonl
cat data/rct-sample/train.jsonl >> data/aug/rct-sample/ratio7/train.jsonl
cat data/rct-sample/train.jsonl >> data/aug/rct-sample/ratio8/train.jsonl
cat data/rct-sample/train.jsonl >> data/aug/rct-sample/ratio9/train.jsonl


cp data/rct-sample/test.jsonl data/aug/rct-sample/ratio0/test.jsonl
cp data/rct-sample/test.jsonl data/aug/rct-sample/ratio1/test.jsonl
cp data/rct-sample/test.jsonl data/aug/rct-sample/ratio2/test.jsonl
cp data/rct-sample/test.jsonl data/aug/rct-sample/ratio3/test.jsonl
cp data/rct-sample/test.jsonl data/aug/rct-sample/ratio4/test.jsonl
cp data/rct-sample/test.jsonl data/aug/rct-sample/ratio5/test.jsonl
cp data/rct-sample/test.jsonl data/aug/rct-sample/ratio6/test.jsonl
cp data/rct-sample/test.jsonl data/aug/rct-sample/ratio7/test.jsonl
cp data/rct-sample/test.jsonl data/aug/rct-sample/ratio8/test.jsonl
cp data/rct-sample/test.jsonl data/aug/rct-sample/ratio9/test.jsonl

cp data/rct-sample/dev.jsonl data/aug/rct-sample/ratio0/dev.jsonl
cp data/rct-sample/dev.jsonl data/aug/rct-sample/ratio1/dev.jsonl
cp data/rct-sample/dev.jsonl data/aug/rct-sample/ratio2/dev.jsonl
cp data/rct-sample/dev.jsonl data/aug/rct-sample/ratio3/dev.jsonl
cp data/rct-sample/dev.jsonl data/aug/rct-sample/ratio4/dev.jsonl
cp data/rct-sample/dev.jsonl data/aug/rct-sample/ratio5/dev.jsonl
cp data/rct-sample/dev.jsonl data/aug/rct-sample/ratio6/dev.jsonl
cp data/rct-sample/dev.jsonl data/aug/rct-sample/ratio7/dev.jsonl
cp data/rct-sample/dev.jsonl data/aug/rct-sample/ratio8/dev.jsonl
cp data/rct-sample/dev.jsonl data/aug/rct-sample/ratio9/dev.jsonl
