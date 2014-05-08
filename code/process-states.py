import sqlite3
from labels import *
import time

count = 0
new_count = 0
conn = sqlite3.connect('us_twitter.db')
c = conn.cursor()

# BAD_FIPS = [60,03,81,07,64,14,66,84,86,67,89,68,71,76,69,95,43,72,74,52,78,79]


start = time.time()
found = 0
for row in c.execute("SELECT * FROM raw_tweets"):
  e = conn.cursor()
  exists = 0
  for r in e.execute("SELECT count(*) FROM us_tweets WHERE tweet_id = ?", (row[6],)):
    exists = r[0]
  if exists == 0:
    count += 1
    if row[3] != None and row[4] != None:
      # fips = 0
      fips = state_label(row)
      if fips != -1 and fips not in BAD_FIPS:
        elapsed = (time.time() - start)
        print "Migrated "+str(new_count) + " of "+str(count)+" tweets", ("%.2fs elapsed" % (elapsed)), ("%.2f percent" % (100 * count / float(1681776 - found))), ("%.2f" % (elapsed / (count / float(1681776 - found)) - elapsed)), "seconds remaining"
        new_count += 1
        d = conn.cursor()
        d.execute("INSERT INTO us_tweets VALUES (NULL,?,?,?,?,?,?,?,?)", (row[1], row[2], row[3], row[4], row[5], row[6], row[7], fips))
        conn.commit()
  else:
    found += 1

