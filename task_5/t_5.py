import numpy as np
import math
import BigEig

eps = 1.e-10
A = np.array([[-2, 1], [3, -1]])
x = [1,1]
print('Тестовая матрица')
print(A)
print('Реальное max с.ч.')
print(-np.linalg.eigvals(A).min())
print('Посчитанное степенным методом')
print(BigEig.Power(A, x, eps))
print('Посчитанное скалярными произведениями')
print(BigEig.Smul(A, x, eps))