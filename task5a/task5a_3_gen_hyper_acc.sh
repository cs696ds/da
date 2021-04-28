#!/bin/bash

#mkdir data/aug/hyperpartisan_news/

mkdir ../data/aug/hyperpartisan_news/ratio_acc0/
mkdir ../data/aug/hyperpartisan_news/ratio_acc1/
mkdir ../data/aug/hyperpartisan_news/ratio_acc2/
mkdir ../data/aug/hyperpartisan_news/ratio_acc3/
mkdir ../data/aug/hyperpartisan_news/ratio_acc4/
mkdir ../data/aug/hyperpartisan_news/ratio_acc5/
mkdir ../data/aug/hyperpartisan_news/ratio_acc6/
mkdir ../data/aug/hyperpartisan_news/ratio_acc7/
mkdir ../data/aug/hyperpartisan_news/ratio_acc8/
mkdir ../data/aug/hyperpartisan_news/ratio_acc9/

cp ratio/acc/hyper_acc0.jsonl ../data/aug/hyperpartisan_news/ratio_acc0/train.jsonl
cp ratio/acc/hyper_acc1.jsonl ../data/aug/hyperpartisan_news/ratio_acc1/train.jsonl
cp ratio/acc/hyper_acc2.jsonl ../data/aug/hyperpartisan_news/ratio_acc2/train.jsonl
cp ratio/acc/hyper_acc3.jsonl ../data/aug/hyperpartisan_news/ratio_acc3/train.jsonl
cp ratio/acc/hyper_acc4.jsonl ../data/aug/hyperpartisan_news/ratio_acc4/train.jsonl
cp ratio/acc/hyper_acc5.jsonl ../data/aug/hyperpartisan_news/ratio_acc5/train.jsonl
cp ratio/acc/hyper_acc6.jsonl ../data/aug/hyperpartisan_news/ratio_acc6/train.jsonl
cp ratio/acc/hyper_acc7.jsonl ../data/aug/hyperpartisan_news/ratio_acc7/train.jsonl
cp ratio/acc/hyper_acc8.jsonl ../data/aug/hyperpartisan_news/ratio_acc8/train.jsonl
cp ratio/acc/hyper_acc9.jsonl ../data/aug/hyperpartisan_news/ratio_acc9/train.jsonl

cat ../data/hyperpartisan_news/train.jsonl >> ../data/aug/hyperpartisan_news/ratio_acc0/train.jsonl
cat ../data/hyperpartisan_news/train.jsonl >> ../data/aug/hyperpartisan_news/ratio_acc1/train.jsonl
cat ../data/hyperpartisan_news/train.jsonl >> ../data/aug/hyperpartisan_news/ratio_acc2/train.jsonl
cat ../data/hyperpartisan_news/train.jsonl >> ../data/aug/hyperpartisan_news/ratio_acc3/train.jsonl
cat ../data/hyperpartisan_news/train.jsonl >> ../data/aug/hyperpartisan_news/ratio_acc4/train.jsonl
cat ../data/hyperpartisan_news/train.jsonl >> ../data/aug/hyperpartisan_news/ratio_acc5/train.jsonl
cat ../data/hyperpartisan_news/train.jsonl >> ../data/aug/hyperpartisan_news/ratio_acc6/train.jsonl
cat ../data/hyperpartisan_news/train.jsonl >> ../data/aug/hyperpartisan_news/ratio_acc7/train.jsonl
cat ../data/hyperpartisan_news/train.jsonl >> ../data/aug/hyperpartisan_news/ratio_acc8/train.jsonl
cat ../data/hyperpartisan_news/train.jsonl >> ../data/aug/hyperpartisan_news/ratio_acc9/train.jsonl


cp ../data/hyperpartisan_news/test.jsonl ../data/aug/hyperpartisan_news/ratio_acc0/test.jsonl
cp ../data/hyperpartisan_news/test.jsonl ../data/aug/hyperpartisan_news/ratio_acc1/test.jsonl
cp ../data/hyperpartisan_news/test.jsonl ../data/aug/hyperpartisan_news/ratio_acc2/test.jsonl
cp ../data/hyperpartisan_news/test.jsonl ../data/aug/hyperpartisan_news/ratio_acc3/test.jsonl
cp ../data/hyperpartisan_news/test.jsonl ../data/aug/hyperpartisan_news/ratio_acc4/test.jsonl
cp ../data/hyperpartisan_news/test.jsonl ../data/aug/hyperpartisan_news/ratio_acc5/test.jsonl
cp ../data/hyperpartisan_news/test.jsonl ../data/aug/hyperpartisan_news/ratio_acc6/test.jsonl
cp ../data/hyperpartisan_news/test.jsonl ../data/aug/hyperpartisan_news/ratio_acc7/test.jsonl
cp ../data/hyperpartisan_news/test.jsonl ../data/aug/hyperpartisan_news/ratio_acc8/test.jsonl
cp ../data/hyperpartisan_news/test.jsonl ../data/aug/hyperpartisan_news/ratio_acc9/test.jsonl

cp ../data/hyperpartisan_news/dev.jsonl ../data/aug/hyperpartisan_news/ratio_acc0/dev.jsonl
cp ../data/hyperpartisan_news/dev.jsonl ../data/aug/hyperpartisan_news/ratio_acc1/dev.jsonl
cp ../data/hyperpartisan_news/dev.jsonl ../data/aug/hyperpartisan_news/ratio_acc2/dev.jsonl
cp ../data/hyperpartisan_news/dev.jsonl ../data/aug/hyperpartisan_news/ratio_acc3/dev.jsonl
cp ../data/hyperpartisan_news/dev.jsonl ../data/aug/hyperpartisan_news/ratio_acc4/dev.jsonl
cp ../data/hyperpartisan_news/dev.jsonl ../data/aug/hyperpartisan_news/ratio_acc5/dev.jsonl
cp ../data/hyperpartisan_news/dev.jsonl ../data/aug/hyperpartisan_news/ratio_acc6/dev.jsonl
cp ../data/hyperpartisan_news/dev.jsonl ../data/aug/hyperpartisan_news/ratio_acc7/dev.jsonl
cp ../data/hyperpartisan_news/dev.jsonl ../data/aug/hyperpartisan_news/ratio_acc8/dev.jsonl
cp ../data/hyperpartisan_news/dev.jsonl ../data/aug/hyperpartisan_news/ratio_acc9/dev.jsonl
