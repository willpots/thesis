import sqlite3
import re
from labels import *
from lib import *

count = 0
conn = sqlite3.connect('us_twitter.db')
c = conn.cursor()

for row in c.execute("SELECT * FROM wiki_articles"):
  body = row[4]
  body = body.lower()
  body = re.sub(u'[^a-zA-Z0-9\ ]', "", body)

  print body


  # d = conn.cursor()
  # d.execute("UPDATE us_tweets SET body = ? WHERE id = ?", (body))
  # conn.commit()


conn.close()
