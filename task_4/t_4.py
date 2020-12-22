import numpy as np
import math
import matplotlib.pyplot as plt
import Jac

eps = 1.e-12

A = np.zeros((6, 6))
for i in range(6):
	for j in range(6):
		A[i][j] = 1/(i + j + 1)	

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