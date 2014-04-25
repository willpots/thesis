from labels import *
import sqlite3
import random
from lib import *
from sklearn import cross_validation

class DataManager():
  def __init__(self, name):
    self.filename = name
    self.conn = sqlite3.connect(name)

  def select_wikipedia_train(self, **args):
    query = "SELECT body, state FROM wiki_articles"
    if "limit" in args:
      query += " ORDER BY RANDOM() LIMIT " + str(args["limit"])
    c = self.conn.cursor()
    train_b = []
    train_l = []
    count = 0
    for row in c.execute(query):
      train_b.append(row[0])
      train_l.append(row[1])
      count += 1
    return train_b, train_l

  def select_tweets(self, **args):
    if "print" in args:
      print args
    limit = args["limit"] or 1000
    table = args["table"] or "tweets"
    # cross_validation
    if "split" not in args:
      split = None
    else:
      split = args["split"]

    if "random" not in args:
      is_random = True
    else:
      is_random = args["random"]
    if "label" in args:
      the_label = args["label"]
    else:
      the_label = state_label

    self.train_b = []
    self.train_l = []
    if split != None:
      self.test_b = []
      self.test_l = []
    else:
      self.test_b = None
      self.test_l = None

    query = "SELECT * FROM %s" % (table)
    query += " WHERE id IS NOT NULL "
    if "state_fips" in args and args["state_fips"] == True:
      query += " AND fips IS NOT NULL"

    if "county_fips" in args and args["county_fips"] == True:
      query += " AND fips_county IS NOT NULL"
    if is_random == True:
      query += " ORDER BY RANDOM() "
    if limit != None:
      query += " LIMIT " + str(limit)
    c = self.conn.cursor()
    if "print" in args:
      print query
    for row in c.execute(query):
      num = random.random()
      if split != None and num > split:
        self.test_b.append(preprocess(row[1]))
        self.test_l.append(the_label(row))
      else:
        self.train_b.append(preprocess(row[1]))
        self.train_l.append(the_label(row))

    return self.train_b, self.train_l, self.test_b, self.test_l

  def unique_labels(self, train=True, test=False):
    uniques = {}
    count = 0
    if train == True and test == True:
      labels = self.train_l + self.test_l
    elif train == True:
      labels = self.train_l
    elif test == True:
      labels = self.test_l

    for l in labels:
      uniques[l] = 1
    for l in uniques:
      counts += 1
    return count

  def train_data(self):
    return self.train_b
  def train_labels(self):
      return self.train_l
  def test_data(self):
    return self.test_b
  def test_labels(self, unique=False):
    return self.test_l


