import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import quad
import solu

def f(x):
	return 6
def k(x):
	return x*x
def k_d(x):
	return 2*x
def q(x):
	return 6
def u(x):
	return 1 - x*x

n = [3, 5, 7]

for i in n:
	solu.solv(i, f, k, k_d, q, u)