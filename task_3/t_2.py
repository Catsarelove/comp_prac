import numpy as np
import iterm

A = np.array([[2, -9, 3], [5, 4, -2], [0, 1, 2]])
b = np.array([-1, 1, -1])
print('Начальные данные')
print(A, b)
print('Точное решение: ', np.linalg.solve(A, b))
print('Решение методом итераций: ',iterm.Iter(A, b, 1.e-3))
print('Методом Зейделя: ', iterm.Relax(A, b, 1.e-3))