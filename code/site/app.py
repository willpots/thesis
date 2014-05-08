from flask import Flask, render_template
from flask import request

import sqlite3
app = Flask(__name__)

def rm_lines(input):
  results = []
  for row in input:
    results.append([row[0], row[1].replace("\n",""), row[2], row[3], row[4], row[5], row[6]])
  return results

@app.route("/")
def index():

  count = request.args.get('count', '') or 20
  max_lat = request.args.get('max_lat', '') or 56.897003921272606
  max_lng = request.args.get('max_lng', '') or -5.537109374999999
  min_lat = request.args.get('min_lat', '') or 12.297068292853805
  min_lng = request.args.get('min_lng', '') or -174.375
   
  results = []
  conn = sqlite3.connect('../us_twitter.db')
  c = conn.cursor()
  found = 0
  for row in c.execute("SELECT * FROM us_tweets WHERE (lng <= ? AND lng >= ? AND lat <= ? AND lat >= ?) LIMIT ?", (max_lng, min_lng, max_lat, min_lat, count)):
    if row[2] != None and row[3] != None:
      found += 1
      results.append(row)
  results = rm_lines(results)
  return render_template('index.html', results=results, count=count, max_lat=max_lat, max_lng=max_lng, min_lat=min_lat, min_lng=min_lng, found=found)

if __name__ == "__main__":
  app.debug = True
  app.run()

