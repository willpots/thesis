import simplejson
import json
import re
import math
from scipy.stats import ttest_1samp
from math import radians, cos, sin, asin, sqrt

def distance(lat1, lon1, lat2, lon2):
  """
  Calculate the great circle distance between two points 
  on the earth (specified in decimal degrees)
  """
  # convert decimal degrees to radians 
  lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

  # haversine formula 
  dlon = lon2 - lon1 
  dlat = lat2 - lat1 
  a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
  c = 2 * asin(sqrt(a)) 

  # 6367 km is the radius of the Earth
  km = 6367 * c
  return km 

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

def remove_stopwords(text):
    words = get("stopwords.json")

    for w in words["words"]:
      text = text.replace(" "+w+" ", " ")
    return text

def remove_links(text):
  # return re.sub(r'http[s]{0,1}\:\/\/',' ',text)
  return text

def preprocess(text):
  text=text.lower()
  text=remove_links(text)
  text=remove_stopwords(text)
  return text
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

