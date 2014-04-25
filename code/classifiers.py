from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
import pickle

class Classifier():

  def __init__(self, **args):
    if "params" in args:
      params = args["params"]
    else:
      params = {}
    if "load" in args:
      self.load(args["load"])
    else:
      self.name = "classifier"
      if "classifier" not in args:
        args["classifier"] = nb
      self.name += "-" + args["classifier"]
      if args["classifier"] == "bnb":
        self.classifier = BernoulliNB(**params)
      elif args["classifier"] == "knn":
        if "k" in args:
          k = args["k"]
        else:
          k = 1000
        self.name += "-" + str(k)
        self.classifier = KNeighborsClassifier(n_neighbors=k, **params)
      elif args["classifier"] == "svm":
        self.classifier = SVC(**params)
      else:
        self.classifier = MultinomialNB(**params)


  def fit(self, data, labels):
    return self.classifier.fit(data, labels)

  def predict(self, data):
    return self.classifier.predict(data)

  def load(self, name):
    self.classifier = pickle.load( open( name+".p", "rb" ) )

  def save(self):
    pickle.dump( self.classifier, open( self.name+".p", "wb" ) )