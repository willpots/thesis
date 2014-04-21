import sqlite3
from labels import *
import time

count = 0
new_count = 0
conn = sqlite3.connect('us_twitter.db')
c = conn.cursor()

# CREATE TABLE "raw_tweets" (id integer primary key not null, body text, lang text, lat real, lng real, user_id integer, tweet_id integer, time integer);
# CREATE TABLE "tweets" (id integer primary key not null, body text, lang text, lat real, lng real, user_id integer, tweet_id integer, raw text, time integer);
# CREATE TABLE "us_tweets" (id integer primary key not null, body text, lang text, lat real, lng real, user_id integer, tweet_id integer, time integer, fips integer);

# (tweets)
# (0  , 1    , 2    , 3   , 4   , 5       , 6        , 7   , 8    )
# (id , body , lang , lat , lng , user_id , tweet_id , raw , time );
# 
# (raw_tweets)
# (0  , 1    , 2    , 3   , 4   , 5       , 6        , 7    )
# (id , body , lang , lat , lng , user_id , tweet_id , time );
# 
# (us_tweets)
# (0  , 1    , 2    , 3   , 4   , 5       , 6        , 7    , 8    )
# (id , body , lang , lat , lng , user_id , tweet_id , time , fips );

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
      if fips != -1:
        elapsed = (time.time() - start)
        print "Migrated "+str(new_count) + " of "+str(count)+" tweets", ("%.2fs elapsed" % (elapsed)), ("%.2f percent" % (100 * count / float(1681776 - found))), ("%.2f" % (elapsed / (count / float(1681776 - found)) - elapsed)), "seconds remaining"
        new_count += 1
        d = conn.cursor()
        # d.execute("INSERT INTO raw_tweets VALUES (NULL,?,?,?,?,?,?,?)", (row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        d.execute("INSERT INTO us_tweets VALUES (NULL,?,?,?,?,?,?,?,?)", (row[1], row[2], row[3], row[4], row[5], row[6], row[7], fips))
        conn.commit()
  else:
    found += 1
    print "Found", found, "tweet", row[6], "exists in db"
  # print chr(27) + "[2J"

