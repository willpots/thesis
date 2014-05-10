from lib import *
from labels import *
from metrics import *
from features import *
from classifiers import Classifier
from db import DataManager
import pickle
import os.path

class StateWikiClassifier():
  DATABASE = "us_twitter.db"
  def __init__(self):
    db_mgr = DataManager(self.DATABASE)
    self.train_tweets, self.train_labels = db_mgr.select_wikipedia_train()
    self.vectorizer = get_vectorizer("tfidf", min_df=1)
    self.nb = Classifier(classifier="nb")
    self.train_data = self.vectorizer.fit_transform(self.train_tweets)
    self.nb.fit(self.train_data, self.train_labels)

  def predict(self, text):
    text = text.lower()
    results = self.nb.predict(self.vectorizer.transform([text]))
    return results[0], FIPS_DEFINITIONS[results[0]]

if os.path.isfile("wikiclassifier.p") == False:
  print "instantiating classifier"
  w = StateWikiClassifier()
  print "saving classifier"
  pickle.dump(w, open( "wikiclassifier.p", "wb" ))
else:
  print "loading file"
  w = pickle.load(open( "wikiclassifier.p", "rb" ) )
  print "loaded file"


string = "Boston Weston Wellesley"
print string
print w.predict(string)
string = "Skiing Hiking Fishing Boulder"
print string
print w.predict(string)
string = "Beaches"
print string
print w.predict(string)
string = "Trees"
print string
print w.predict(string)
string = "Oil"
print string
print w.predict(string)
string = "Corn"
print string
print w.predict(string)
string = "Corn"
print string
print w.predict(string)
string = "Corruption"
print string
print w.predict(string)