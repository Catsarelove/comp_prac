import math
import numpy as np
import meig

nr = np.linalg.norm
A = np.array([[-1, 9, -3, 4], [-1, 2, 3 ,4], [0, 1, 2, 3], [0, 0, 1, 2]])

b = np.array([-5, 0, 0, 5])
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