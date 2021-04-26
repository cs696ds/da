#!/bin/bash

# mkdir data/aug/hyperpartisan_news/

# mkdir data/aug/hyperpartisan_news/hyper_24/
# mkdir data/aug/hyperpartisan_news/hyper_26/
# mkdir data/aug/hyperpartisan_news/hyper_28/
# mkdir data/aug/hyperpartisan_news/hyper_30/
# mkdir data/aug/hyperpartisan_news/hyper_32/
# mkdir data/aug/hyperpartisan_news/hyper_34/
# mkdir data/aug/hyperpartisan_news/hyper_36/

cp task5a/hyper_aug/hyper_24.jsonl data/aug/hyperpartisan_news/hyper_24/train.jsonl
cp task5a/hyper_aug/hyper_26.jsonl data/aug/hyperpartisan_news/hyper_26/train.jsonl
cp task5a/hyper_aug/hyper_28.jsonl data/aug/hyperpartisan_news/hyper_28/train.jsonl
cp task5a/hyper_aug/hyper_30.jsonl data/aug/hyperpartisan_news/hyper_30/train.jsonl
cp task5a/hyper_aug/hyper_32.jsonl data/aug/hyperpartisan_news/hyper_32/train.jsonl
cp task5a/hyper_aug/hyper_34.jsonl data/aug/hyperpartisan_news/hyper_34/train.jsonl
cp task5a/hyper_aug/hyper_36.jsonl data/aug/hyperpartisan_news/hyper_36/train.jsonl

cp data/hyperpartisan_news/test.jsonl data/aug/hyperpartisan_news/hyper_24/test.jsonl
cp data/hyperpartisan_news/test.jsonl data/aug/hyperpartisan_news/hyper_26/test.jsonl
cp data/hyperpartisan_news/test.jsonl data/aug/hyperpartisan_news/hyper_28/test.jsonl
cp data/hyperpartisan_news/test.jsonl data/aug/hyperpartisan_news/hyper_30/test.jsonl
cp data/hyperpartisan_news/test.jsonl data/aug/hyperpartisan_news/hyper_32/test.jsonl
cp data/hyperpartisan_news/test.jsonl data/aug/hyperpartisan_news/hyper_34/test.jsonl
cp data/hyperpartisan_news/test.jsonl data/aug/hyperpartisan_news/hyper_36/test.jsonl

cp data/hyperpartisan_news/dev.jsonl data/aug/hyperpartisan_news/hyper_24/dev.jsonl
cp data/hyperpartisan_news/dev.jsonl data/aug/hyperpartisan_news/hyper_26/dev.jsonl
cp data/hyperpartisan_news/dev.jsonl data/aug/hyperpartisan_news/hyper_28/dev.jsonl
cp data/hyperpartisan_news/dev.jsonl data/aug/hyperpartisan_news/hyper_30/dev.jsonl
cp data/hyperpartisan_news/dev.jsonl data/aug/hyperpartisan_news/hyper_32/dev.jsonl
cp data/hyperpartisan_news/dev.jsonl data/aug/hyperpartisan_news/hyper_34/dev.jsonl
cp data/hyperpartisan_news/dev.jsonl data/aug/hyperpartisan_news/hyper_36/dev.jsonl
