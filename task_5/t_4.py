import numpy as np
import math
import BigEig

eps = 1.e-20

A = np.zeros((6, 6))
for i in range(6):
	for j in range(6):
		A[i][j] = 1/(i + j + 1)	
x = np.arange(6)
print('Тестовая матрица')
print(A)
print('Реальное max с.ч.')
l = np.linalg.eigvals(A).max()
print(l)

print('Посчитанное степенным методом')
p = BigEig.Power(A, x, eps)
print(p)
print('Посчитанное скалярными произведениями')
s = BigEig.Smul(A, x, eps)
print(s)

print('Погрешность ст. метода', abs(p - l))
print('Погрешность метода скалярных произведений', abs(s - l))