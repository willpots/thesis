import pickle
# Don't clutter the damn namespace
from lib import *
from labels import *
from metrics import *
from features import *
from classifiers import Classifier

from db import DataManager

N_TIMES = 1

for i in range(0,N_TIMES):
  print i+1, "times"
  DATABASE = "us_twitter.db"

  split = 0.8

  db_mgr = DataManager(DATABASE)

  train_tweets, train_labels = db_mgr.select_wikipedia_train()
  test_tweets, test_labels, dummy1, dummy2 = db_mgr.select_tweets(limit=10, state_fips=True, table="us_tweets", label=state_fips)

  results = get("results.json")

  vectorizer = get_vectorizer("tfidf", min_df=1)

  classifiers = {
    "BernoulliNB": Classifier(classifier="bnb"),
    "MultinomialNB": Classifier(classifier="nb"),
    "KNN-1000": Classifier(classifier="knn", k=1000),
    "KNN-2000": Classifier(classifier="knn", k=2000),
    # "SVC": Classifier(classifier="svm", params={"C" : 1.0,"kernel" : 'linear','verbose':True})
    "SVC": Classifier(load="classifier-SVC")
  }

  # Vectorizing Training Data
  train_data = vectorizer.fit_transform(train_tweets)
  # Vectorizing Testing Data
  test_data = vectorizer.transform(test_tweets)
  maj_label, maj_count = majority_label(train_labels)
  maj_acc = majority_accuracy(maj_label, test_labels)
  # print "Majority Label:", maj_label
  # print "Majority Accuracy:", maj_acc
  # print("K\t\t, Train  , Test   , Tr Imp , Te Imp")

  for k in sorted(classifiers):
    knn = classifiers[k]
    knn.fit(train_data, train_labels) 
    pickle.dump( knn, open( "wikitrain-"+str(k)+".p", "wb" ) )
    # train_acc = accuracy(knn.predict(train_data), train_labels)
    # test_acc = accuracy(knn.predict(test_data), test_labels)
    # results = ensure_structure_and_append(results,[k,"tweets","state_label","train_improvement"],train_acc - maj_acc)
    # results = ensure_structure_and_append(results,[k,"tweets","state_label","test_improvement"],test_acc - maj_acc)
    # print k,"\t,","%.4f" % train_acc,", %.4f" % test_acc, ", %.4f" % (train_acc - maj_acc), ", %.4f" % (test_acc - maj_acc)

  # put(results,"results.json")
