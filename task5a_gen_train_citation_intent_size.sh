#!/bin/bash

#mkdir data/aug/citation_intent/

mkdir data/aug/citation_intent/ratio0/
mkdir data/aug/citation_intent/ratio1/
mkdir data/aug/citation_intent/ratio2/
mkdir data/aug/citation_intent/ratio3/
mkdir data/aug/citation_intent/ratio4/
mkdir data/aug/citation_intent/ratio5/
mkdir data/aug/citation_intent/ratio6/
mkdir data/aug/citation_intent/ratio7/
mkdir data/aug/citation_intent/ratio8/
mkdir data/aug/citation_intent/ratio9/

cp task5a/citation_intent_size/citation_intent_0.jsonl data/aug/citation_intent/ratio0/train.jsonl
cp task5a/citation_intent_size/citation_intent_1.jsonl data/aug/citation_intent/ratio1/train.jsonl
cp task5a/citation_intent_size/citation_intent_2.jsonl data/aug/citation_intent/ratio2/train.jsonl
cp task5a/citation_intent_size/citation_intent_3.jsonl data/aug/citation_intent/ratio3/train.jsonl
cp task5a/citation_intent_size/citation_intent_4.jsonl data/aug/citation_intent/ratio4/train.jsonl
cp task5a/citation_intent_size/citation_intent_5.jsonl data/aug/citation_intent/ratio5/train.jsonl
cp task5a/citation_intent_size/citation_intent_6.jsonl data/aug/citation_intent/ratio6/train.jsonl
cp task5a/citation_intent_size/citation_intent_7.jsonl data/aug/citation_intent/ratio7/train.jsonl
cp task5a/citation_intent_size/citation_intent_8.jsonl data/aug/citation_intent/ratio8/train.jsonl
cp task5a/citation_intent_size/citation_intent_9.jsonl data/aug/citation_intent/ratio9/train.jsonl

cat data/citation_intent/train.jsonl >> data/aug/citation_intent/ratio0/train.jsonl
cat data/citation_intent/train.jsonl >> data/aug/citation_intent/ratio1/train.jsonl
cat data/citation_intent/train.jsonl >> data/aug/citation_intent/ratio2/train.jsonl
cat data/citation_intent/train.jsonl >> data/aug/citation_intent/ratio3/train.jsonl
cat data/citation_intent/train.jsonl >> data/aug/citation_intent/ratio4/train.jsonl
cat data/citation_intent/train.jsonl >> data/aug/citation_intent/ratio5/train.jsonl
cat data/citation_intent/train.jsonl >> data/aug/citation_intent/ratio6/train.jsonl
cat data/citation_intent/train.jsonl >> data/aug/citation_intent/ratio7/train.jsonl
cat data/citation_intent/train.jsonl >> data/aug/citation_intent/ratio8/train.jsonl
cat data/citation_intent/train.jsonl >> data/aug/citation_intent/ratio9/train.jsonl


cp data/citation_intent/test.jsonl data/aug/citation_intent/ratio0/test.jsonl
cp data/citation_intent/test.jsonl data/aug/citation_intent/ratio1/test.jsonl
cp data/citation_intent/test.jsonl data/aug/citation_intent/ratio2/test.jsonl
cp data/citation_intent/test.jsonl data/aug/citation_intent/ratio3/test.jsonl
cp data/citation_intent/test.jsonl data/aug/citation_intent/ratio4/test.jsonl
cp data/citation_intent/test.jsonl data/aug/citation_intent/ratio5/test.jsonl
cp data/citation_intent/test.jsonl data/aug/citation_intent/ratio6/test.jsonl
cp data/citation_intent/test.jsonl data/aug/citation_intent/ratio7/test.jsonl
cp data/citation_intent/test.jsonl data/aug/citation_intent/ratio8/test.jsonl
cp data/citation_intent/test.jsonl data/aug/citation_intent/ratio9/test.jsonl

cp data/citation_intent/dev.jsonl data/aug/citation_intent/ratio0/dev.jsonl
cp data/citation_intent/dev.jsonl data/aug/citation_intent/ratio1/dev.jsonl
cp data/citation_intent/dev.jsonl data/aug/citation_intent/ratio2/dev.jsonl
cp data/citation_intent/dev.jsonl data/aug/citation_intent/ratio3/dev.jsonl
cp data/citation_intent/dev.jsonl data/aug/citation_intent/ratio4/dev.jsonl
cp data/citation_intent/dev.jsonl data/aug/citation_intent/ratio5/dev.jsonl
cp data/citation_intent/dev.jsonl data/aug/citation_intent/ratio6/dev.jsonl
cp data/citation_intent/dev.jsonl data/aug/citation_intent/ratio7/dev.jsonl
cp data/citation_intent/dev.jsonl data/aug/citation_intent/ratio8/dev.jsonl
cp data/citation_intent/dev.jsonl data/aug/citation_intent/ratio9/dev.jsonl
