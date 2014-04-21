import sqlite3
import random
import numpy
import pylab

# Don't clutter the damn namespace
from lib import *
from labels import *
from metrics import *
from db import DataManager

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans

DATABASE = "us_twitter.db"

# calculate document frequencies on whole data
# pick the majority
# pick based off the distributions




split = 0.8

# new_york = lib.BoundingBox(-74.259088,40.495996,-73.700272,40.915256)
train_tweets = []
train_labels = []
test_tweets = []
test_labels = []
centers = []
unique_labels = {}
db_mgr = DataManager(DATABASE)
train_tweets, train_labels, test_tweets, test_labels = db_mgr.select_tweets(limit=10000, table="us_tweets", split=0.8, label=fips_label)
print "Train Size:", len(train_tweets)
print "Test Size:", len(test_tweets)


# vectorizer = CountVectorizer(min_df=1)
vectorizer = TfidfVectorizer(min_df=1)

knns = {
  2: KNeighborsClassifier(n_neighbors=2),
  4: KNeighborsClassifier(n_neighbors=4),
  8: KNeighborsClassifier(n_neighbors=8),
  20: KNeighborsClassifier(n_neighbors=20),
  40: KNeighborsClassifier(n_neighbors=40),
  80: KNeighborsClassifier(n_neighbors=80),
  200: KNeighborsClassifier(n_neighbors=200),
  400: KNeighborsClassifier(n_neighbors=400),
  600: KNeighborsClassifier(n_neighbors=600),
  800: KNeighborsClassifier(n_neighbors=800),
  1000: KNeighborsClassifier(n_neighbors=1000),
  2000: KNeighborsClassifier(n_neighbors=2000)}

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
print("K\t, Train, Test")
for k in sorted(knns):
  knn = knns[k]
  knn.fit(train_data, train_labels) 
  print k,"\t,","%.4f" % accuracy(knn.predict(train_data), train_labels),",", "%.4f" % accuracy(knn.predict(test_data), test_labels)

