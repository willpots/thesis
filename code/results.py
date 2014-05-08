from lib import *
from scipy.stats import ttest_1samp
import numpy as np

results = get("results.json")


def print_p_values(obj, space=""):
  for k in obj:
    print space + k
    if isinstance(obj[k], dict):
      print_p_values(obj[k], space+"  ")
    elif isinstance(obj[k], list):
      p = ttest_1samp(obj[k], 0)[1]
      print space+"  "+str(np.mean(obj[k]))
      print space+"  "+str(p)
    else:
      print " "




print print_p_values(results)