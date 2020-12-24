import numpy as np
import matplotlib.pyplot as plt
import setka
import math
e = 1.e-2

def q1(x):
	return - (1 + x / 2) * (x - 3)
def r1(x):
	return (x - 3) * math.exp(x/2)

def f1(x):
	return - (2 - x) * (x - 3)

a1 = [1, 0, 0]
b1 = [1, 0, 0]

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