import numpy as np
import iterm

A = np.array([[11100, 0.03], [ -1, 106000]])
b = np.array([-1, 1])
print('Начальные данные')
print(A, b)
print('Точное решение: ', np.linalg.solve(A, b))
print('Решение методом итераций: ',iterm.Iter(A, b, 1.e-5))
print('Методом Зейделя: ', iterm.Relax(A, b, 1.e-5))