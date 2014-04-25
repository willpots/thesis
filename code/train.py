import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

from lib import *
from labels import *
from metrics import *
from features import *

from db import DataManager

DATABASE = "us_twitter.db"
db_mgr = DataManager(DATABASE)
train_tweets, train_labels = db_mgr.select_wikipedia_train()

count_vectorizer = get_vectorizer("tfidf", min_df=1)
tf_idf_vectorizer = get_vectorizer("count", min_df=1)

print "Vectorizing Training Data..."
count_data = count_vectorizer.fit_transform(train_tweets)
tf_idf_data = tf_idf_vectorizer.fit_transform(train_tweets)

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
  2000: KNeighborsClassifier(n_neighbors=2000)
}