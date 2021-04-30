import numpy as np
import math as m
from numpy.random import Generator, PCG64
import matplotlib.pyplot as plt

G = Generator(PCG64())

def stick_breaking(n:int,alpha:float) -> np.ndarray:
  """
  Draws n samples from a stick-breaking process with beta distribution intensity alpha.

  :param n: number of samples
  :param alpha: intensity parameter of the beta distribution
  :returns: stick lengths
  """
  betas = G.beta(b=alpha, a=1.0, size=n)
  betas[1:] *= np.cumprod(1-betas[:-1])
  weights = np.sort(betas)[::-1]
  return weights

def plot_stick_lengths(stick_lengths:np.array,
		       alpha:float,
		       B:int) -> None:
  """
  Plots -log2(sticks)
  :param sticks: list of stick lenghts
  """
  plt.plot(np.log2(np.array(range(1,101))), -1*np.log2((stick_lengths)), 'b')
  plt.xlabel('log2 of values from 1 to 100')
  plt.ylabel('-Log2(stick_lengths)')
  plt.title('Stick Breaking')
  plt.show()
