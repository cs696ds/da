#!/bin/bash

# mkdir data/aug/citation_intent/

# mkdir data/aug/citation_intent/score_max24/
# mkdir data/aug/citation_intent/score_max26/
# mkdir data/aug/citation_intent/score_max28/
# mkdir data/aug/citation_intent/score_max30/
# mkdir data/aug/citation_intent/score_max32/
# mkdir data/aug/citation_intent/score_max34/
mkdir data/aug/citation_intent/score_max36/

# cp task5a/citation_intent_aug/citation_intent_24.jsonl data/aug/citation_intent/score_max24/train.jsonl
# cp task5a/citation_intent_aug/citation_intent_26.jsonl data/aug/citation_intent/score_max26/train.jsonl
# cp task5a/citation_intent_aug/citation_intent_28.jsonl data/aug/citation_intent/score_max28/train.jsonl
# cp task5a/citation_intent_aug/citation_intent_30.jsonl data/aug/citation_intent/score_max30/train.jsonl
# cp task5a/citation_intent_aug/citation_intent_32.jsonl data/aug/citation_intent/score_max32/train.jsonl
# cp task5a/citation_intent_aug/citation_intent_34.jsonl data/aug/citation_intent/score_max34/train.jsonl
cp task5a/citation_intent_aug/citation_intent_36.jsonl data/aug/citation_intent/score_max36/train.jsonl

# cat data/citation_intent/train.jsonl >> data/aug/citation_intent/score_max24/train.jsonl
# cat data/citation_intent/train.jsonl >> data/aug/citation_intent/score_max26/train.jsonl
# cat data/citation_intent/train.jsonl >> data/aug/citation_intent/score_max28/train.jsonl
# cat data/citation_intent/train.jsonl >> data/aug/citation_intent/score_max30/train.jsonl
# cat data/citation_intent/train.jsonl >> data/aug/citation_intent/score_max32/train.jsonl
# cat data/citation_intent/train.jsonl >> data/aug/citation_intent/score_max34/train.jsonl
cat data/citation_intent/train.jsonl >> data/aug/citation_intent/score_max36/train.jsonl


# cp data/citation_intent/test.jsonl data/aug/citation_intent/score_max24/test.jsonl
# cp data/citation_intent/test.jsonl data/aug/citation_intent/score_max26/test.jsonl
# cp data/citation_intent/test.jsonl data/aug/citation_intent/score_max28/test.jsonl
# cp data/citation_intent/test.jsonl data/aug/citation_intent/score_max30/test.jsonl
# cp data/citation_intent/test.jsonl data/aug/citation_intent/score_max32/test.jsonl
# cp data/citation_intent/test.jsonl data/aug/citation_intent/score_max34/test.jsonl
cp data/citation_intent/test.jsonl data/aug/citation_intent/score_max36/test.jsonl

# cp data/citation_intent/dev.jsonl data/aug/citation_intent/score_max24/dev.jsonl
# cp data/citation_intent/dev.jsonl data/aug/citation_intent/score_max26/dev.jsonl
# cp data/citation_intent/dev.jsonl data/aug/citation_intent/score_max28/dev.jsonl
# cp data/citation_intent/dev.jsonl data/aug/citation_intent/score_max30/dev.jsonl
# cp data/citation_intent/dev.jsonl data/aug/citation_intent/score_max32/dev.jsonl
# cp data/citation_intent/dev.jsonl data/aug/citation_intent/score_max34/dev.jsonl
cp data/citation_intent/dev.jsonl data/aug/citation_intent/score_max36/dev.jsonl
