import numpy as np
import matplotlib.pyplot as plt
import math
import pylab
from mpl_toolkits.mplot3d import Axes3D
import warm

a = 1
m_1 = lambda x: x*x*x
m_2 = lambda t: t*t*t
m_3 = lambda t: 1 + t*t*t
f = lambda x, t: 3*t*t - 6*x
u = lambda t, x: t*t*t + x*x*x
t_0 = 0
t_1 = 0.5
x_0 = 0
x_1 = 1
n = 100
N = 80000
warm.Sol(u, N, n, x_0, x_1, t_0, t_1, a, f, m_1, m_2, m_3)
warm.Sol(u, N//10, n, x_0, x_1, t_0, t_1, a, f, m_1, m_2, m_3)
