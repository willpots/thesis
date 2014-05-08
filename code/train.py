import pickle

from lib import *
from labels import *
from metrics import *
from features import *

from db import DataManager
from classifiers import Classifier

DATABASE = "us_twitter.db"
db_mgr = DataManager(DATABASE)
train_data, train_labels = db_mgr.select_wikipedia_train()

vectorizers = {
  "count":get_vectorizer("tfidf", min_df=1),
  "tfidf":get_vectorizer("count", min_df=1)
}

print "Vectorizing Training Data..."
count_data = vectorizers["count"].fit_transform(train_data)
tf_idf_data = vectorizers["tfidf"].fit_transform(train_data)

classifiers = {
  "BernoulliNB": {
    "count":Classifier(classifier="bnb"),
    "tfidf":Classifier(classifier="bnb")
  },
  "MultinomialNB": {
    "count":Classifier(classifier="nb"),
    "tfidf":Classifier(classifier="nb")
  }
}

for c in classifiers:
  print "Training", c, "count"
  classifiers[c]["count"].fit(count_data, train_labels)
  pickle.dump( classifiers[c]["count"], open( "classifier-"+str(c)+"-count.p", "wb" ) )
  print "Training", c, "tfidf"
  classifiers[c]["tfidf"].fit(tf_idf_data, train_labels)
  pickle.dump( classifiers[c]["tfidf"], open( "classifier-"+str(c)+"-tfidf.p", "wb" ) )

