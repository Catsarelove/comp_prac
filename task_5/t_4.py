import numpy as np
import math
import BigEig

eps = 1.e-10
A = np.zeros((5,5))
for i in range(4):
	A[i][i+1] = i*2 + 1
	if i != 3:
		A[i+1][i+2] = i + 2
print('Тестовая матрица')
print(A)
print('Реальное max с.ч.')
print(np.linalg.eigvals(A).max)
print('Посчитанное степенным методом')
print(BigEig.Power(A, eps))
print('Посчитанное скалярными произведениями')
print(BigEig.Smul(A, eps))