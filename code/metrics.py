

def majority_accuracy(majority, labels):
  total = 0.0
  correct = 0.0
  for i,v in enumerate(labels):
    if majority == v:
      correct += 1
    total += 1
  return correct / total

def accuracy(results, labels):
  total = 0.0
  correct = 0.0
  for i,v in enumerate(results):
    if results[i] == labels[i]:
      correct += 1
    total += 1
  return correct / total
