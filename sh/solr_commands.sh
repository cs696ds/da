# Start solr
bin/solr start

# Create core (collections)
# solr create -c <core name> -d <config name>
bin/solr create -c depcc -d sample_techproducts_configs

# Index data files
# bin/post -c <core name> <file name>
bin/post -c techproducts example/exampledocs/*
