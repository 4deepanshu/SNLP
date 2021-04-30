from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
def analysis(name, data):
  """
  Plot Zipfian distribution of words + true Zipfian distribution. Compute MSE.

  :param name: title of the graph
  :param data: list of words
  """
  vocabulary = Counter(data)
  text_len = len(data)
  sorted_vocab = sorted(vocabulary.items(), key=lambda item: item[1], reverse=True)
  # TODO use these lists instead of log lists
  rel_frequency = []
  theoretical_frequency = []
  rank = []

  denominator = 0
  for i in range(len(sorted_vocab)):
    denominator += 1 / (i+1)

  error = 0

  for i, (_, frequency) in enumerate(sorted_vocab):
    rel_frequency.append(frequency/text_len)
    rank.append(i+1)
    theoretical_frequency.append(1/(i+1)/denominator)
    error += (1/(i+1)/denominator - frequency/text_len)**2

  fig, ax = plt.subplots()
  ax.scatter(np.log(rank), np.log(rel_frequency), marker='o', linewidths=0.3)
  ax.set_title(name, fontsize=18)
  ax.set_xlabel('log-rank', fontsize=15)
  ax.set_ylabel('log - relative frequency', fontsize=15)
  ax.plot(np.log(rank), np.log(theoretical_frequency), 'r')

  fig.set_size_inches(18.5, 10.5)
  
  plt.show()
  print("MSE: {:.10f}".format(error/text_len))
  print('least freq:', sorted_vocab[-1])  
  print('most freq:', sorted_vocab[0])  


