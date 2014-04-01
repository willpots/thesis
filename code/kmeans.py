import sqlite3
import random
import numpy as np
import pylab as pl

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans

def rand_lat():
  return random.random() * 180 - 90

def rand_lng():
  return random.random() * 360 - 180


def get_label(lat, lng):
  # 0 to 72
  newlng = round((lng + 180) / 5)
  # 0 to 36
  newlat = round((lat + 90) / 5)
  return str(int(newlat))+"-"+str(int(newlng))
K = 10

train_tweets = []
train_labels = []
test_tweets = []
test_labels = []
centers = []
conn = sqlite3.connect('twitter.db')
c = conn.cursor()
# for row in c.execute("SELECT * FROM tweets LIMIT 10000"):
for row in c.execute("SELECT * FROM tweets LIMIT 100"):
  if row[3] != None and row[4] != None:
    train_tweets.append(row[1])
    train_labels.append(get_label(row[3], row[4]))
# for row in c.execute("SELECT * FROM tweets LIMIT 2000 OFFSET 10000"):
for row in c.execute("SELECT * FROM tweets LIMIT 100 OFFSET 100"):
  if row[3] != None and row[4] != None:
    test_tweets.append(row[1])
    print get_label(row[3], row[4])
    test_labels.append(get_label(row[3], row[4]))

# vectorizer = CountVectorizer(min_df=1)
vectorizer = TfidfVectorizer(min_df=1)
knn = KNeighborsClassifier(n_neighbors=3)
clusters = {"2":KMeans(n_clusters=2),
            "4":KMeans(n_clusters=4),
            "8":KMeans(n_clusters=8),
            "16":KMeans(n_clusters=16),
            "32":KMeans(n_clusters=32),
            "64":KMeans(n_clusters=64)}

print "Vectorizing Training Data..."
train_data = vectorizer.fit_transform(train_tweets)
print "Vectorizing Testing Data..."
test_data = vectorizer.transform(test_tweets)
for k,cluster in clusters.items():
  print "Testing",k,"clusters..."
  print "Training Cluster Data..."
  cluster.fit(train_data) 
  print "Testing Cluster Data..."
  results = cluster.predict(test_data)
  # for i,v in enumerate(results):
    # print results[i], test_labels[i]
  print cluster.labels_