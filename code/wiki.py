from HTMLParser import HTMLParser
from bs4 import BeautifulSoup
import requests
import re

lines = open( "geo_coordinates_en.ttl", "r" )
array = []
count = 0
for line in lines:
  if "<http://www.georss.org/georss/point>" in line:
    count += 1
    line = line.replace("<http://dbpedia.org/resource/", "")
    line = line.replace("> <http://www.georss.org/georss/point>", "")
    line = line.replace("@en .\n", "")
    line = line.replace("\"", "")
    terms = line.split(" ")
    terms = {"title":terms[0], "lat":terms[1], "lng":terms[2]}
    r = requests.get('http://en.wikipedia.org/wiki/%s' % (terms["title"]))
    soup = BeautifulSoup(r.text)
    response = soup.find(id='bodyContent').get_text()
    response = re.sub(r'\s{2,}', ' ', response)
    response = re.sub(r'\n', ' ', response)
    print response
    if count > 1:
      break
lines.close()