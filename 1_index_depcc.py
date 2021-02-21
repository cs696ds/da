#pysolr-3.9.0
import pysolr
import json
solr = pysolr.Solr('http://localhost:8983/solr/depcc', always_commit=True)
print(solr.ping())

# solr.add([
#     {
#         "url" : "https://foo.bar",
#         "s3"  : "s3://foo",
#         "text": "Foo Bar is a great researcher."
#     }
# ])


# json_lines = []
# with open('data/part-19100-small.jsonl', 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         j = json.loads(line)
#         solr.add(j)


results = solr.search('friends')
print("Saw {0} result(s).".format(len(results)))
for result in results:
    print(result["_src_"])
