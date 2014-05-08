# Don't clutter the damn namespace
from lib import *
from labels import *
from metrics import *
from features import *
from classifiers import Classifier
from db import DataManager

N_TIMES = 60
VECTORIZER = "tfidf"
SIZE = 20000


params = [
          ["wiki", "no_preprocess", "state_label",state_fips,False],
          # ["wiki", "no_preprocess", "county_label",county_label,False],
          # ["tweets", "no_preprocess", "grid_1_label",grid_1_degree,False],
          # ["tweets", "no_preprocess", "grid_5_label",grid_5_degree,False],
          # ["tweets", "no_preprocess", "grid_10_label",grid_10_degree,False],
          ["wiki", "preprocess", "state_label",state_fips,True]
          # ["wiki", "preprocess", "county_label",county_label,True]
          # ["tweets", "preprocess", "grid_1_label",grid_1_degree,True],
          # ["tweets", "preprocess", "grid_5_label",grid_5_degree,True],
          # ["tweets", "preprocess", "grid_10_label",grid_10_degree,True]
         ]
for p in range(0,len(params)):
  print params[p]
  TRAINING, PREPROCESSING, LABEL_FUNC, label_func, preprocess = params[p]
  for i in range(0,N_TIMES):
    print i+1, "times"
    DATABASE = "us_twitter.db"

    split = 0.8

    db_mgr = DataManager(DATABASE)

    if TRAINING == "tweets":
      train_tweets, train_labels, test_tweets, test_labels = db_mgr.select_tweets(limit=SIZE, preprocess=preprocess, table="us_tweets", split=0.8, label=label_func)
    else:
      train_tweets, train_labels = db_mgr.select_wikipedia_train()
      test_tweets, test_labels, dummy1, dummy2 = db_mgr.select_tweets(limit=(SIZE * 0.2), state_fips=True, table="us_tweets", label=label_func)
    # print "Train Size:", len(train_tweets)
    # print "Test Size:", len(test_tweets)


    vectorizer = get_vectorizer(VECTORIZER, min_df=1)

    classifiers = {
      "BernoulliNB": Classifier(classifier="bnb"),
      "MultinomialNB": Classifier(classifier="nb"),
      # "KNN-50": Classifier(classifier="knn", k=50),
      # "KNN-100": Classifier(classifier="knn", k=100),
      # "KNN-1000": Classifier(classifier="knn", k=1000),
      # "KNN-2000": Classifier(classifier="knn", k=2000)
      # "SVC": Classifier(classifier="svm", params={"C" : 1.0,"kernel" : 'linear','verbose':True})
      # "SVC": Classifier(classifier="svm", params={'kernel':'linear'})
    }

    # Vectorizing Training Data
    train_data = vectorizer.fit_transform(train_tweets)
    # Vectorizing Testing Data
    test_data = vectorizer.transform(test_tweets)

    maj_label, maj_count = majority_label(train_labels)
    maj_acc = majority_accuracy(maj_label, test_labels)
    print "Majority Label:", maj_label
    print "Majority Accuracy:", maj_acc
    print("K\t\t, Train  , Test   , Tr Imp , Te Imp")

    for c in sorted(classifiers):
      results = get("results.json")
      knn = classifiers[c]
      knn.fit(train_data, train_labels) 
      train_acc = accuracy(knn.predict(train_data), train_labels)
      test_acc = accuracy(knn.predict(test_data), test_labels)
      results = ensure_structure_and_append(results,[c,PREPROCESSING,TRAINING,LABEL_FUNC,"train_accuracy"],train_acc)
      results = ensure_structure_and_append(results,[c,PREPROCESSING,TRAINING,LABEL_FUNC,"test_accuracy"],test_acc)
      results = ensure_structure_and_append(results,[c,PREPROCESSING,TRAINING,LABEL_FUNC,"train_improvement"],train_acc - maj_acc)
      results = ensure_structure_and_append(results,[c,PREPROCESSING,TRAINING,LABEL_FUNC,"test_improvement"],test_acc - maj_acc)
      print c,"\t,","%.4f" % train_acc,", %.4f" % test_acc, ", %.4f" % (train_acc - maj_acc), ", %.4f" % (test_acc - maj_acc)
      put(results,"results.json")
