import numpy
import scipy
import sqlite3
from sklearn import svm


def in_boston(lat, lng):
  if lat < 42.388822 and lat > 42.324888:
    if lng > -71.16806 and lng < -71.012878:
      return True
  return False
 
def in_america(lat, lng):
  if lat < 51.382067 and lat >  24.661994:
    if lng > -130.78125 and lng < -65.214844:
      return True
  return False


# RETRIEVE TWEETS
tweets = []
locations = []
conn = sqlite3.connect('twitter.db')
c = conn.cursor()
count = 10000
for row in c.execute("SELECT * FROM tweets LIMIT ?", (count,)):
  if row[2] != None and row[3] != None:
    tweets.append(row[1])
    locations.append(in_america(row[3],row[4]))

# CALCULATE LOCATION BUCKETS
t,f = 0,0
for i in locations:
  if i == True:
    t += 1
  if i == False:
    f += 1
print t,f


# svc = svm.SVC(kernel='linear')
# svc.fit(iris_X_train, iris_y_train)    
# SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
#   kernel='linear', max_iter=-1, probability=False, random_state=None,
#   shrinking=True, tol=0.001, verbose=False)

 

  

