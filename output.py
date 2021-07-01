import json
qlist=[]
with open('logs/logs_sparc_editsql/valid_use_predicted_queries_predictions.json') as f:
  for obj in f:
    data = json.loads(obj)
    qlist.append(data)
i=0
with open('output.txt', 'w') as json_file:
  for q in qlist:
    i=i+1
    json.dump(' '.join(q['prediction']), json_file)
    