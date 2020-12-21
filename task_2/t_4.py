import math
import numpy as np
import meig

nr = np.linalg.norm
A = 2*np.eye(5)
for i in range(1,4):
	A[i][i + 1] += i
	A[i][i - 1] += 2
	A[i-1][i+1] += i/4
	A[i+1][i-1] = -2
	A[i-1][i-1] *= i-12
b = np.arange(5)
print('Условия, A и b')
print(A)
print(b)
print('реальное решение:')
x = np.linalg.solve(A,b)
print(x)
print('решение методом вращений, погрешность:')
r = meig.Rot(A, b)
print(r)
print(nr(abs(x-r)))

print('решение методом LU, погрешность:')
lu = meig.LU(A,b)
print(lu)
print(nr(abs(x - lu)))