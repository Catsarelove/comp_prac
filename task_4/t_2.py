import numpy as np
import math
import matplotlib.pyplot as plt
import Jac

eps = 1.e-12

A = np.eye(6)
for i in range(6):
	A[i][3] = i*1.e-4
	A[3][i] = i*1.e-4
	A[i][4] = i*3
	A[4][i] = i*3

print('начальная матрица:')
print(A)
print('собственные числа:')
print(np.linalg.eigvals(A))

print('Выбор обнуляемого элемента по стратегии "преград-барьеров"')
print(Jac.Bound(A, eps))
print('Выбор обнуляемого элемента по максимальному радиуса круга Гершгорина')
print(Jac.Gersh(A, eps))