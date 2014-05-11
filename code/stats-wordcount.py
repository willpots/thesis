import sqlite3
from lib import *
from labels import *
import time

count = 0
conn = sqlite3.connect('us_twitter.db')
c = conn.cursor()

counts = {}
start = time.time()
for row in c.execute("SELECT * FROM us_tweets"):
  body = preprocess(row[1])
  words = body.split(" ")
  for w in words:
    w = w.lower()
    if w not in counts:
      counts[w] = 1
    else:
      counts[w] += 1
  # print body
place = len(counts)
for w in sorted(counts, key=counts.get, reverse=False):
    print place, w, counts[w]
    place -= 1

print len(counts), "total items"
print "completed in ", time.time() - start, "seconds"
conn.close()
