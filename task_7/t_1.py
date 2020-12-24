import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import quad
import solu

def f(x):
	return 1 - 3*(math.cos(x-1))**2
def k(x):
	return math.cos(x-1)
def k_d(x):
	return -math.sin(x-1)
def q(x):
	return -2*math.cos(x-1)
def u(x):
	return math.sin(x-1) * (x+1)

n = [3, 5, 7]

for i in n:
	solu.solv(i, f, k, k_d, q, u)