import sqlite3
from labels import *
import time

count = 0
conn = sqlite3.connect('us_twitter.db')
c = conn.cursor()

counts = {}
start = time.time()
for row in c.execute("SELECT * FROM wiki_articles"):
  body = row[4]
  words = body.split(" ")
  for w in words:
    w = w.lower()
    if w not in counts:
      counts[w] = 1
    else:
      counts[w] += 1
  # print body

for w in sorted(counts, key=counts.get, reverse=False):
    print w, counts[w]

print len(counts), "total items"
print "completed in ", time.time() - start, "seconds"
conn.close()
