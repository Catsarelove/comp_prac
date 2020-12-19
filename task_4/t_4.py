import numpy as np
import math
import matplotlib.pyplot as plt
import Jac

eps = 1.e-7

A = np.zeros((6, 6))
for i in range(6):
	for j in range(6):
		A[i][j] = 1/(i + j + 1)	

print('начальная матрица:')
print(A)
print('собственные числа:')
print(np.linalg.eigvals(A))

print('Выбор обнуляемого элемента по стратегии "преград-барьеров"')
print(Jac.Bound(A, eps))
print('Выбор обнуляемого элемента по максимальному радиуса круга Гершгорина')
print(Jac.Gersh(A, eps))