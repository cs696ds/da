# Start solr
../solr-8.8.0/bin/solr start

# Create core (collections)
# solr create -c <core name> -d <config name>
#../solr-8.8.0/bin/solr create -c depcc -d sample_techproducts_configs

# Index data files
# bin/post -c <core name> <file name>
#../solr-8.8.0/bin/post -c depcc part-00000.jsonl



