from HTMLParser import HTMLParser
from bs4 import BeautifulSoup, Comment
import requests
import bleach
import re
import sqlite3
from lib import *
from labels import *
import csv


conn = sqlite3.connect('us_twitter.db')
c = conn.cursor()

lines = open( "geo_coordinates_en.ttl", "r" )
array = []
count = 0
# csvfile = open('wikiarticles.csv', 'wb')
# wikiwriter = csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_NONE)



# for line in lines:
  # if "<http://www.georss.org/georss/point>" in line:
    # count += 1
    # line = line.replace("<http://dbpedia.org/resource/", "")
    # line = line.replace("> <http://www.georss.org/georss/point>", "")
    # line = line.replace("@en .\n", "")
    # line = line.replace("\"", "")
    # terms = line.split(" ")
with open('wikiarticles.csv', 'rb') as f:
  reader = csv.reader(f, delimiter='|', quoting=csv.QUOTE_NONE)
  for row in reader:
    count += 1
    title = row[0]
    state_fips = row[3]
    terms = {"title":unicode(row[0], "UTF-8"), "lat":row[1], "lng":row[2]}


    e = conn.cursor()
    exists = 0
    for r in e.execute("SELECT count(*) FROM wiki_articles WHERE title = ?", (terms["title"],)):
      exists = r[0]
    if exists == 0:
      # PULL DATA
      r = requests.get('http://en.wikipedia.org/wiki/%s' % (terms["title"]))

      soup = BeautifulSoup(r.text)

      REMOVE_ATTRIBUTES = ['lang','language','onmouseover','onmouseout','script','style','font',
                          'dir','face','size','color','style','class','width','height','hspace',
                          'border','valign','align','background','bgcolor','text','link','vlink',
                          'alink','cellpadding','cellspacing']
      # PROCESS DATA
      [s.extract() for s in soup('img')]
      [s.extract() for s in soup('noscript')]
      [s.extract() for s in soup('script')]
      [s.extract() for s in soup('sup')]
      body = soup.find(id='mw-content-text')
      paragraphs = soup.find_all("p")
      text = ""

      for p in paragraphs:
          text += p.get_text()
      text = text.lower()

      text = re.sub(r'[\.\,\"\;\:]', ' ', text)
      text = re.sub(r'\s{2,}', ' ', text)
      text = re.sub(r'\n', ' ', text)
      text = remove_stopwords(text)

      d = conn.cursor()
      # CREATE TABLE "wiki_articles" (id, title, lat, lng, body, state, county)
      d.execute("INSERT INTO wiki_articles VALUES (NULL,?,?,?,?,?,NULL)", (terms["title"], terms["lat"], terms["lng"], text, state_fips))
      conn.commit()
      print "[X]", count, terms["title"]
      # print text
    else:
      print "[E]", count, terms["title"]
# lines.close()
conn.close()