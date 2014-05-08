import sqlite3
import re
from labels import *
from lib import *

count = 0
conn = sqlite3.connect('us_twitter.db')
c = conn.cursor()

for row in c.execute("SELECT * FROM us_tweets limit 200"):
  body = row[1]
  body = body.lower()
  body = re.sub(r'(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z0-9]+[A-Za-z0-9\_]+)'," ",body)
  body = re.sub(r'(http[s]{0,1}\:\/\/){0,1}[a-zA-Z0-9\-\_]\.[a-zA-Z]{2,5}\/[A-Za-z0-9\/\-\_]*',"",body)
  body = re.sub(u'[^a-zA-Z0-9\ ]', "", body)
  body = re.sub(r'[\"\_\#\:\?\!\-\(\)\.]',"",body)
  body = re.sub(r'[\W]+'," ",body)
  body = re.sub(r'^[\W]|[\W]$',"",body)
  body = remove_stopwords(body) 

  print body


  # d = conn.cursor()
  # d.execute("UPDATE us_tweets SET body = ? WHERE id = ?", (body))
  # conn.commit()


conn.close()
