from TwitterAPI import TwitterAPI
import sqlite3
import json
import time

conn = sqlite3.connect('twitter.db')

api = TwitterAPI("iokZ57Ny54BEySHgmESw", "gfh2kYfU2m4QpqCiBoG6WXyUHcyqpPE8hTw6dJYCs", "114476085-bmsz96mDcyvrGrKHL69VXdZqwIxyqw1nLUWogrDu", "MLDro8JlXk4al5WOof2ms9J4vI0IZP5JeAYQSXvpNIWVS")

# CREATE TABLE tweets (body text, lang text, lat real, lng real, user_id integer, tweet_id integer, raw text);

r = api.request('statuses/filter', {'locations':'-180,-90,180,90'})
geofence, no_geofence = 0, 0
counted = 0
start = time.time()
try:
  for item in r.get_iterator():
      if 'id' in item:
        c = conn.cursor()
        lat, lng = None, None
        body = item['text']
        tweet_id = item['id']
        user_id = -1
        lang = item['lang']
        if lang == "en":
          counted += 1
          raw = str(json.dumps(item))
          if 'user' in item:
            user_id = item['user']['id']
          if item['coordinates']:
            lat = item['coordinates']['coordinates'][1] or None
            lng = item['coordinates']['coordinates'][0] or None
            no_geofence += 1
          elif 'place' in item:
            lat = 0
            lng = 0
            count = 0
            geofence += 1
            for x in item['place']['bounding_box']['coordinates'][0]:
              # print x
              lat += x[1]
              lng += x[0]
              count += 1
            lat /= count
            lng /= count
          print ("%.2fs" % (time.time() - start)), ("Lang: "+lang), ("Count: " + str(counted)), (str(geofence) +" vs. " + str(no_geofence)),"\n", lat, lng, "\n", body
          c.execute("INSERT INTO tweets VALUES (?, ?, ?, ?, ?, ?, ?)", (body, lang, lat, lng, user_id, tweet_id, raw, ))
          conn.commit()
except KeyboardInterrupt:
  print "\n"
  print "-"*25
  print "Downloading stopped by user after "+str(("%.2fs" % (time.time() - start)))
  print "-"*25
  print "\n"