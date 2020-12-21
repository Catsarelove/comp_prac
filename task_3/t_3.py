import numpy as np
import iterm

A = np.array([[2000, 0, 0.3], [1, 400, 0.1], [0, -1000, 2]])
b = np.array([-1, 0, -2])
print('Начальные данные')
print(A, b)
print('Точное решение: ', np.linalg.solve(A, b))
print('Решение методом итераций: ',iterm.Iter(A, b, 1.e-3))
print('Методом Зейделя: ', iterm.Relax(A, b, 1.e-3))