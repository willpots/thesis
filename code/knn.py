import sqlite3
import random
import numpy
import pylab
import lib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans


DB = "twitter.db"


# calculate document frequencies on whole data
# pick the majority
# pick based off the distributions

def rand_lat():
  return random.random() * 180 - 90

def rand_lng():
  return random.random() * 360 - 180


def get_label(lat, lng):
  # 0 to 36
  newlng = round((lng + 180) / 2)
  # 0 to 18
  newlat = round((lat + 90) / 2)
  return str(int(newlat))+"_"+str(int(newlng))


def majority_accuracy(majority, labels):
  total = 0.0
  correct = 0.0
  for i,v in enumerate(labels):
    if majority == v:
      correct += 1
    total += 1
  return correct / total

def accuracy(results, labels):
  total = 0.0
  correct = 0.0
  for i,v in enumerate(results):
    if results[i] == labels[i]:
      correct += 1
    total += 1
  return correct / total

def majority_label(labels):
  counts = {}
  for label in labels:
    if label in counts:
      counts[label] += 1
    else:
      counts[label] = 1
  max_label = None
  max_value = -1
  for label in counts:
    if counts[label] > max_value:
      max_value = counts[label]
      max_label = label
  return max_label, max_value

K = 10

split = 0.8

# new_york = lib.BoundingBox(-74.259088,40.495996,-73.700272,40.915256)
train_tweets = []
train_labels = []
test_tweets = []
test_labels = []
centers = []
unique_labels = {}
# conn = sqlite3.connect('twitter.db')
conn = sqlite3.connect(DB)

c = conn.cursor()
for row in c.execute("SELECT * FROM tweets ORDER BY RANDOM() LIMIT 10000"):
# for row in c.execute("SELECT * FROM tweets LIMIT 100"):
  if row[3] != None and row[4] != None:
    num = random.random()
    if num < split:
      train_tweets.append(row[1])
      train_labels.append(get_label(row[3], row[4]))
      unique_labels[get_label(row[3], row[4])] = 1
    else:
      test_tweets.append(row[1])
      test_labels.append(get_label(row[3], row[4]))
print "Train Size:", len(train_tweets)
print "Test Size:", len(test_tweets)


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
print "Unique Training Labels", total_labels

print "Vectorizing Training Data..."
train_data = vectorizer.fit_transform(train_tweets)
print "Vectorizing Testing Data..."
test_data = vectorizer.transform(test_tweets)
maj_label, maj_count = majority_label(train_labels)
print "Majority Label:", maj_label
print "Majority Accuracy:", majority_accuracy(maj_label, test_labels)
for k,knn in knns.items():
  print "Testing",k,"neighbor model..."
  knn.fit(train_data, train_labels) 

  results = knn.predict(train_data)
  print "Train Accuracy:", accuracy(results, train_labels)

  results = knn.predict(test_data)
  print "Test Accuracy:", accuracy(results, test_labels)
