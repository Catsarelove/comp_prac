import numpy as np
import math
import BigEig

eps = 1.e-8
A = np.eye(5)
for i in range(5):
	for j in range(i):
		A[i][j] = i
		A[j][i] = i

print('Тестовая матрица')
print(A)
print('Реальное max с.ч.')
print(np.linalg.eigvals(A).max())
print('Посчитанное степенным методом')
print(BigEig.Power(A, eps))
print('Посчитанное скалярными произведениями')
print(BigEig.Smul(A, eps))