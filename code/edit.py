
import sqlite3
import json
import time

conn = sqlite3.connect('twitter.db')
c = conn.cursor()
count = 0
for row in c.execute("SELECT * FROM tweets"):
  d = conn.cursor()
  count += 1
  obj = json.loads(row[6])
  a_time = time.mktime(time.strptime(obj["created_at"], "%a %b %d %H:%M:%S +0000 %Y"))
  seconds = int(a_time)
  d.execute("INSERT INTO new_tweets VALUES (NULL,?,?,?,?,?,?,?,?)", (row[0], row[1], row[2], row[3], row[4], row[5], row[6], seconds))
  conn.commit()
  print "Migrated "+str(count)+" tweets"