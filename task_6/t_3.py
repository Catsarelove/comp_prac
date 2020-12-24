import numpy as np
import matplotlib.pyplot as plt
import setka
import math
e = 1.e-2

def q1(x):
	return 0
def r1(x):
	return -x*math.exp(x)

def f1(x):
	return math.sin(x)

a1 = [0.3, 1, -0.8]
b1 = [0.9, 1, -0.1]

U, err = setka.pres_sol(q1, r1, f1, -1, 1, 10, a1, b1, e)		

N = len(U)
h = 2/N
x = [-1 + i*h for i in range(N)]
plt.plot(err[0], err[1])
plt.xlabel('x')
plt.ylabel('погрешность')
plt.show()
plt.plot(x, U)
plt.xlabel('x')
plt.ylabel('u')
plt.show()