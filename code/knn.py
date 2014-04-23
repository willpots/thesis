import sqlite3
import random
import numpy
import pylab

# Don't clutter the damn namespace
from lib import *
from labels import *
from metrics import *
from features import *

from db import DataManager

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB

DATABASE = "us_twitter.db"

split = 0.8

train_tweets = []
train_labels = []
test_tweets = []
test_labels = []
centers = []
unique_labels = {}
db_mgr = DataManager(DATABASE)
train_tweets, train_labels, test_tweets, test_labels = db_mgr.select_tweets(limit=10000, state_fips=True, table="us_tweets", split=0.8, label=state_fips)
print "Train Size:", len(train_tweets)
print "Test Size:", len(test_tweets)

results = get("knn_results.json")

vectorizer = get_vectorizer("count", min_df=1)

classifiers = {
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
  # "GaussianNB": GaussianNB(),
  # "BernoulliNB": BernoulliNB(),
  # "MultinomialNB": MultinomialNB()}



total_labels = 0
for i,v in enumerate(unique_labels):
  total_labels += 1
print "Unique Training Labels", total_labels

print "Vectorizing Training Data..."
train_data = vectorizer.fit_transform(train_tweets)
print "Vectorizing Testing Data..."
test_data = vectorizer.transform(test_tweets)
maj_label, maj_count = majority_label(train_labels)
maj_acc = majority_accuracy(maj_label, test_labels)
print "Majority Label:", maj_label
print "Majority Accuracy:", maj_acc
print("K\t, Train  , Test   , Tr Imp , Te Imp")

for k in sorted(classifiers):
  knn = classifiers[k]
  knn.fit(train_data, train_labels) 
  train_acc = accuracy(knn.predict(train_data), train_labels)
  test_acc = accuracy(knn.predict(test_data), test_labels)
  results = ensure_structure_and_append(results,["knn","state_label",str(k),"train_improvement"],train_acc - maj_acc)
  results = ensure_structure_and_append(results,["knn","state_label",str(k),"test_improvement"],test_acc - maj_acc)
  print k,"\t,","%.4f" % train_acc,", %.4f" % test_acc, ", %.4f" % (train_acc - maj_acc), ", %.4f" % (test_acc - maj_acc)

put(results,"knn_results.json")
