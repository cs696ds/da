#!/bin/bash

#mkdir data/aug/hyperpartisan_news/

mkdir data/aug/hyperpartisan_news/ratio0/
mkdir data/aug/hyperpartisan_news/ratio1/
mkdir data/aug/hyperpartisan_news/ratio2/
mkdir data/aug/hyperpartisan_news/ratio3/
mkdir data/aug/hyperpartisan_news/ratio4/
mkdir data/aug/hyperpartisan_news/ratio5/
mkdir data/aug/hyperpartisan_news/ratio6/
mkdir data/aug/hyperpartisan_news/ratio7/
mkdir data/aug/hyperpartisan_news/ratio8/
mkdir data/aug/hyperpartisan_news/ratio9/

cp task5a/hyperpartisan_news_0.jsonl data/aug/hyperpartisan_news/ratio0/train.jsonl
cp task5a/hyperpartisan_news_1.jsonl data/aug/hyperpartisan_news/ratio1/train.jsonl
cp task5a/hyperpartisan_news_2.jsonl data/aug/hyperpartisan_news/ratio2/train.jsonl
cp task5a/hyperpartisan_news_3.jsonl data/aug/hyperpartisan_news/ratio3/train.jsonl
cp task5a/hyperpartisan_news_4.jsonl data/aug/hyperpartisan_news/ratio4/train.jsonl
cp task5a/hyperpartisan_news_5.jsonl data/aug/hyperpartisan_news/ratio5/train.jsonl
cp task5a/hyperpartisan_news_6.jsonl data/aug/hyperpartisan_news/ratio6/train.jsonl
cp task5a/hyperpartisan_news_7.jsonl data/aug/hyperpartisan_news/ratio7/train.jsonl
cp task5a/hyperpartisan_news_8.jsonl data/aug/hyperpartisan_news/ratio8/train.jsonl
cp task5a/hyperpartisan_news_9.jsonl data/aug/hyperpartisan_news/ratio9/train.jsonl

cat data/hyperpartisan_news/train.jsonl >> data/aug/hyperpartisan_news/ratio0/train.jsonl
cat data/hyperpartisan_news/train.jsonl >> data/aug/hyperpartisan_news/ratio1/train.jsonl
cat data/hyperpartisan_news/train.jsonl >> data/aug/hyperpartisan_news/ratio2/train.jsonl
cat data/hyperpartisan_news/train.jsonl >> data/aug/hyperpartisan_news/ratio3/train.jsonl
cat data/hyperpartisan_news/train.jsonl >> data/aug/hyperpartisan_news/ratio4/train.jsonl
cat data/hyperpartisan_news/train.jsonl >> data/aug/hyperpartisan_news/ratio5/train.jsonl
cat data/hyperpartisan_news/train.jsonl >> data/aug/hyperpartisan_news/ratio6/train.jsonl
cat data/hyperpartisan_news/train.jsonl >> data/aug/hyperpartisan_news/ratio7/train.jsonl
cat data/hyperpartisan_news/train.jsonl >> data/aug/hyperpartisan_news/ratio8/train.jsonl
cat data/hyperpartisan_news/train.jsonl >> data/aug/hyperpartisan_news/ratio9/train.jsonl


cp data/hyperpartisan_news/test.jsonl data/aug/hyperpartisan_news/ratio0/test.jsonl
cp data/hyperpartisan_news/test.jsonl data/aug/hyperpartisan_news/ratio1/test.jsonl
cp data/hyperpartisan_news/test.jsonl data/aug/hyperpartisan_news/ratio2/test.jsonl
cp data/hyperpartisan_news/test.jsonl data/aug/hyperpartisan_news/ratio3/test.jsonl
cp data/hyperpartisan_news/test.jsonl data/aug/hyperpartisan_news/ratio4/test.jsonl
cp data/hyperpartisan_news/test.jsonl data/aug/hyperpartisan_news/ratio5/test.jsonl
cp data/hyperpartisan_news/test.jsonl data/aug/hyperpartisan_news/ratio6/test.jsonl
cp data/hyperpartisan_news/test.jsonl data/aug/hyperpartisan_news/ratio7/test.jsonl
cp data/hyperpartisan_news/test.jsonl data/aug/hyperpartisan_news/ratio8/test.jsonl
cp data/hyperpartisan_news/test.jsonl data/aug/hyperpartisan_news/ratio9/test.jsonl

cp data/hyperpartisan_news/dev.jsonl data/aug/hyperpartisan_news/ratio0/dev.jsonl
cp data/hyperpartisan_news/dev.jsonl data/aug/hyperpartisan_news/ratio1/dev.jsonl
cp data/hyperpartisan_news/dev.jsonl data/aug/hyperpartisan_news/ratio2/dev.jsonl
cp data/hyperpartisan_news/dev.jsonl data/aug/hyperpartisan_news/ratio3/dev.jsonl
cp data/hyperpartisan_news/dev.jsonl data/aug/hyperpartisan_news/ratio4/dev.jsonl
cp data/hyperpartisan_news/dev.jsonl data/aug/hyperpartisan_news/ratio5/dev.jsonl
cp data/hyperpartisan_news/dev.jsonl data/aug/hyperpartisan_news/ratio6/dev.jsonl
cp data/hyperpartisan_news/dev.jsonl data/aug/hyperpartisan_news/ratio7/dev.jsonl
cp data/hyperpartisan_news/dev.jsonl data/aug/hyperpartisan_news/ratio8/dev.jsonl
cp data/hyperpartisan_news/dev.jsonl data/aug/hyperpartisan_news/ratio9/dev.jsonl
