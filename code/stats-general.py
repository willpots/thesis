import sqlite3



# Declare variables
tweets = []
stats = {}
stats["total_count"] = 0
stats["min_time"] = 1000000000000
stats["max_time"] = 0

tweets_by_user = {}
regions = {}

# Connect to Database
conn = sqlite3.connect('us_twitter.db')
c = conn.cursor()

print "Pulling tweets..."
# id, body, lang, lat, lng, user_id, tweet_id, raw, time
stats["articles_count"] = 0
stats["articles_word_count"] = 0
wiki_words = {}
for row in c.execute("SELECT * FROM wiki_articles"):
  stats["articles_count"] += 1
  for w in row[4].split(" "):
    stats["articles_word_count"] += 1
    if w not in wiki_words:
      wiki_words[w] = 1
    else:
      wiki_words[w] += 1
stats["wiki_unique_words"] = len(wiki_words)
for w in sorted(wiki_words, key=wiki_words.get, reverse=False):
  print w, wiki_words[w]

for row in c.execute("SELECT * FROM raw_tweets"):
  stats["total_count"] += 1
  if row[2] != None and row[3] != None:
    tweet_row = [row[0],row[1],row[2],row[3],row[4],row[5], row[6], row[7]]
    tweets.append(tweet_row)
    if row[5] not in tweets_by_user:
      tweets_by_user[row[5]] = []
    tweets_by_user[row[5]].append(tweet_row)
    time = False
    try:
      time = row[7]
    except IndexError:
      print "no time found"
    if(time and time < stats["min_time"]):
      stats["min_time"] = time
    if(time and time > stats["max_time"]):
      stats["max_time"] = time


# User-based statistics
stats["unique_users"] = len(tweets_by_user)
stats["average_tweets_per_user"] = stats["total_count"] / len(tweets_by_user)
stats["min_tweets"] = stats["total_count"]
stats["max_tweets"] = 0
stats["max_tweeter_id"] = -1
for user,row in tweets_by_user.items():
  count = len(row)

  if(count < stats["min_tweets"]):
    stats["min_tweets"] = count
  if(count > stats["max_tweets"]):
    stats["max_tweets"] = count
    stats["max_tweeter_id"] = user


#EvenSizedBuckets
#Kmeans

for k,v in sorted(stats.items()):
  print k, ":", v

conn.close()