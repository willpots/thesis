import simplejson
import json
 
def put(data, filename):
  try:
    jsondata = simplejson.dumps(data, indent=2, skipkeys=True, sort_keys=True)
    fd = open(filename, 'w')
    fd.write(jsondata)
    fd.close()
  except:
    print 'ERROR writing', filename
    pass
 
def get(filename):

  with open(filename, 'r') as fd:
    return json.load(fd)
 
def ensure_results(k,obj):
  if k not in obj:
    obj[k] = {}
  if "train_improvement" not in obj[k]:
    obj[k]["train_improvement"] = []
  if "test_improvement" not in obj[k]:
    obj[k]["test_improvement"] = []
  return obj

def ensure_structure_and_append(obj,keys,value):
  tmp = obj
  for k in keys:
    if k not in tmp:
      tmp[k] = {}
    tmp = tmp[k]
  if isinstance(tmp, list):
    tmp.append(value)
  else:
    tmp = obj
    for i in range(0,len(keys)-1):
      tmp = tmp[keys[i]]
    last_key = keys[len(keys)-1]
    tmp[last_key] = [value]
  return obj