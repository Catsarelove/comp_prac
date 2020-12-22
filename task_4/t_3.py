import numpy as np
import math
import matplotlib.pyplot as plt
import Jac

eps = 1.e-20


A = np.array([[3, 0, 2], [0, 4, 4], [2, 4, 4]])

print('начальная матрица:')
print(A)
print('собственные числа:')
l = np.sort(np.linalg.eigvals(A))
print(l)

print('Выбор обнуляемого элемента по стратегии "преград-барьеров"')
b = np.sort(Jac.Bound(A, eps))
print('Погрешность:', np.linalg.norm(b - l))
print('Выбор обнуляемого элемента по максимальному радиуса круга Гершгорина')
g = np.sort(Jac.Gersh(A, eps))

print('Погрешность:', np.linalg.norm(g-l))