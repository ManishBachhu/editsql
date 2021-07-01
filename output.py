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
    #print(q['input_seq'])  
    #print(q['probability'])
    #print(q['prediction'])
    #print("=======================================")
    json.dump(str(i) + '. ', json_file)
    json.dump(' '.join(q['input_seq']), json_file)
    json_file.write('\n')
    json.dump(q['probability'], json_file)
    json_file.write('\n')
    json.dump(' '.join(q['prediction']), json_file)
    json_file.write('\n')
    json.dump("===============================================================", json_file)
    json_file.write('\n')