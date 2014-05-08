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
    textwords = text.lower().split(" ")
    textwords = [n for n in textwords if n != ""]
    for w in words["words"]:
      textwords = [n for n in textwords if n != w]
    return " ".join(map(str, textwords))

def remove_links(text):
  # return re.sub(r'http[s]{0,1}\:\/\/',' ',text)
  return text

def preprocess(text):
  text=text.lower()
  text = re.sub(r'(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z0-9]+[A-Za-z0-9\_]+)'," ",text)
  text = re.sub(r'(http[s]{0,1}\:\/\/){0,1}[a-zA-Z0-9\-\_]\.[a-zA-Z]{2,5}\/[A-Za-z0-9\/\-\_]*',"",text)
  text = re.sub(u'[^a-zA-Z0-9\ ]', "", text)
  text = re.sub(r'[\"\_\#\:\?\!\-\(\)\.]',"",text)
  text = re.sub(r'[\W]+'," ",text)
  text = re.sub(r'^[\W]|[\W]$',"",text)
  text = remove_stopwords(text) 
  return text

def ensure_results(k,obj):
  if k not in obj:
    obj[k] = {}
  if "train_improvement" not in obj[k]:
    obj[k]["train_improvement"] = []
  if "test_improvement" not in obj[k]:
    obj[k]["test_improvement"] = []
  return obj

def pull_results_array(keys):
  obj = get("results.json")
  for k in keys:
    try:
      obj = obj[k]
    except:
      print "KeyError"
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

FIPS_DEFINITIONS={1:"AL",2:"AK",4:"AZ",5:"AR",6:"CA",8:"CO",9:"CT",10:"DE",11:"DC",12:"FL",13:"GA",15:"HI",16:"ID",17:"IL",18:"IN",19:"IA",20:"KS",21:"KY",22:"LA",23:"ME",24:"MD",25:"MA",26:"MI",27:"MN",28:"MS",29:"MO",30:"MT",31:"NE",32:"NV",33:"NH",34:"NJ",35:"NM",36:"NY",37:"NC",38:"ND",39:"OH",40:"OK",41:"OR",42:"PA",44:"RI",45:"SC",46:"SD",47:"TN",48:"TX",49:"UT",50:"VT",51:"VA",53:"WA",54:"WV",55:"WI",56:"WY"}