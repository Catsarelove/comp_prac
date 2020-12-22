import numpy as np
import math
import BigEig

eps = 1.e-6
A = np.eye(5)
for i in range(5):
	A[i][2] = -i
	A[2][i] = i
	A[i][3] = i*2
	A[3][i] = i + 2
x = A.T[0]
print('Тестовая матрица')
print(A)
print('Реальное max с.ч.')
l = np.linalg.eigvals(A).max()
print(l)
print('|L| = %f', abs(l)) 


print('Посчитанное степенным методом')
print(BigEig.Power(A,x, eps))
print('Посчитанное скалярными произведениями')
print(BigEig.Smul(A,x, eps))