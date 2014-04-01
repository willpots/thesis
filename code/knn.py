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
  # 0 to 36
  newlng = round((lng + 180) / 10)
  # 0 to 18
  newlat = round((lat + 90) / 10)
  return str(int(newlat))+"-"+str(int(newlng))

def accuracy(results, labels):
  total = 0.0
  correct = 0.0
  for i,v in enumerate(results):
    if results[i] == labels[i]:
      correct += 1
    total += 1
  return correct / total

K = 10

print "KNN Classification"
print "Train Size:", 10000
print "Test Size:", 2000
train_tweets = []
train_labels = []
test_tweets = []
test_labels = []
centers = []
unique_labels = {}
conn = sqlite3.connect('twitter.db')
c = conn.cursor()
for row in c.execute("SELECT * FROM tweets LIMIT 10000"):
# for row in c.execute("SELECT * FROM tweets LIMIT 100"):
  if row[3] != None and row[4] != None:
    train_tweets.append(row[1])
    train_labels.append(get_label(row[3], row[4]))
    unique_labels[get_label(row[3], row[4])] = 1
for row in c.execute("SELECT * FROM tweets LIMIT 2000 OFFSET 10000"):
# for row in c.execute("SELECT * FROM tweets LIMIT 100 OFFSET 100"):
  if row[3] != None and row[4] != None:
    test_tweets.append(row[1])
    test_labels.append(get_label(row[3], row[4]))

# vectorizer = CountVectorizer(min_df=1)
vectorizer = TfidfVectorizer(min_df=1)
knns = {
  "2": KNeighborsClassifier(n_neighbors=2),
  "4": KNeighborsClassifier(n_neighbors=4),
  "8": KNeighborsClassifier(n_neighbors=8),
  "16": KNeighborsClassifier(n_neighbors=16),
  "32": KNeighborsClassifier(n_neighbors=32),
  "64": KNeighborsClassifier(n_neighbors=64),
  "128": KNeighborsClassifier(n_neighbors=128)}

total_labels = 0
for i,v in enumerate(unique_labels):
  total_labels += 1
print "Unique Labels", total_labels

print "Vectorizing Training Data..."
train_data = vectorizer.fit_transform(train_tweets)
print "Vectorizing Testing Data..."
test_data = vectorizer.transform(test_tweets)
for k,knn in knns.items():
  print "Testing",k,"neighbor model..."
  knn.fit(train_data, train_labels) 

  results = knn.predict(train_data)
  print "Train Accuracy:", accuracy(results, train_labels)

  results = knn.predict(test_data)
  print "Test Accuracy:", accuracy(results, test_labels)
