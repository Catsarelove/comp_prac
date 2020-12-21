import math
import numpy as np
import meig

nr = np.linalg.norm
A = np.array([[2, 0, 3], [1, 1, 0], [1, 0, -1]])
b = np.array([5, 0, 0])
print('Условия, A и b')
print(A)
print(b)
print('реальное решение:')
x = [1, - 1, 1]
print(x)
print('решение методом вращений, погрешность:')
r = meig.Rot(A, b)
print(r)
print(nr(abs(x-r)))

print('решение методом LU, погрешность:')
lu = meig.LU(A,b)
print(lu)
print(nr(abs(x - lu)))