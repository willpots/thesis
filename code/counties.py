import sqlite3
from labels import *

count = 0
conn = sqlite3.connect('us_twitter.db')
c = conn.cursor()

for row in c.execute("SELECT * FROM us_tweets WHERE fips_county IS NULL"):
  count += 1
  if row[3] != None and row[4] != None:
    # fips = 0
    fips = county_fips(row)
    if fips != -1:
      print count, "finished"
      d = conn.cursor()
      print fips
      d.execute("UPDATE us_tweets SET fips_county = ? WHERE id = ?", (fips, row[0]))
      conn.commit()
conn.close()
