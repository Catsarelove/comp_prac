import numpy as np
import math
import BigEig

eps = 1.e-20
A = np.eye(12)
for i in range(12):
	A[i][2] = i*10
	A[2][i] = i*10
x = np.arange(12)
print('Тестовая матрица')
print(A)
print('Реальное max с.ч.')
print(np.linalg.eigvals(A).max())
print('Посчитанное степенным методом')
print(BigEig.Power(A, x, eps))
print('Посчитанное скалярными произведениями')
print(BigEig.Smul(A,x, eps))