from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer



def get_vectorizer(type, **args):
  if type == "tfidf":
    return CountVectorizer(args)
  else:
    return TfidfVectorizer(args)

