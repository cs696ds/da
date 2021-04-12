#!/bin/bash
# Index data files
# bin/post -c <core name> <file name>
#../../../solr-8.8.0/bin/post -c depcc ../../data/98-depcc-20/*
#../../../solr-8.8.0/bin/post -c depcc-small ../../data/99-depcc/01000-01999/


for i in $(seq -f "%05g" 06000 06999)
do
  ../../../solr-8.8.0/bin/post -c depcc-large ../../data/99-depcc/06000-06999/part-${i}.jsonl
done

for i in $(seq -f "%05g" 08000 08999)
do
  ../../../solr-8.8.0/bin/post -c depcc-large ../../data/99-depcc/08000-08999/part-${i}.jsonl
done

for i in $(seq -f "%05g" 09000 09999)
do
  ../../../solr-8.8.0/bin/post -c depcc-large ../../data/99-depcc/09000-09999/part-${i}.jsonl
done

for i in $(seq -f "%05g" 10000 10999)
do
  ../../../solr-8.8.0/bin/post -c depcc-large ../../data/99-depcc/10000-10999/part-${i}.jsonl
done

for i in $(seq -f "%05g" 11000 11999)
do
  ../../../solr-8.8.0/bin/post -c depcc-large ../../data/99-depcc/11000-11999/part-${i}.jsonl
done

for i in $(seq -f "%05g" 12000 12999)
do
  ../../../solr-8.8.0/bin/post -c depcc-large ../../data/99-depcc/12000-12999/part-${i}.jsonl
done

for i in $(seq -f "%05g" 13000 13999)
do
  ../../../solr-8.8.0/bin/post -c depcc-large ../../data/99-depcc/13000-13999/part-${i}.jsonl
done

for i in $(seq -f "%05g" 14000 14999)
do
  ../../../solr-8.8.0/bin/post -c depcc-large ../../data/99-depcc/14000-14999/part-${i}.jsonl
done

for i in $(seq -f "%05g" 15000 15999)
do
  ../../../solr-8.8.0/bin/post -c depcc-large ../../data/99-depcc/15000-15999/part-${i}.jsonl
done

for i in $(seq -f "%05g" 16000 16999)
do
  ../../../solr-8.8.0/bin/post -c depcc-large ../../data/99-depcc/16000-16999/part-${i}.jsonl
done

for i in $(seq -f "%05g" 17000 17999)
do
  ../../../solr-8.8.0/bin/post -c depcc-large ../../data/99-depcc/17000-17999/part-${i}.jsonl
done

for i in $(seq -f "%05g" 18000 18999)
do
  ../../../solr-8.8.0/bin/post -c depcc-large ../../data/99-depcc/18000-18999/part-${i}.jsonl
done

for i in $(seq -f "%05g" 19000 19100)
do
  ../../../solr-8.8.0/bin/post -c depcc-large ../../data/99-depcc/19000-19100/part-${i}.jsonl
done


