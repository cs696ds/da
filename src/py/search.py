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


# NOT WORKING
# json_lines = []
# with open('data/part-19100.jsonl', 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         j = json.loads(line)
#         json_lines.append(j)
#         solr.add(j)
# print(len(json_lines))

sample_text = "These observations and this line of reasoning has not escaped the attention of theoretical linguists ."
#sample_text = "friends"

results = solr.search(sample_text, rows=9999)
#results = solr.search(sample_text)

print("Saw {0} result(s).".format(len(results)))
for result in results:
    print(result["_src_"])
