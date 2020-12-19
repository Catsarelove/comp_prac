import numpy as np
import math
import matplotlib.pyplot as plt
import Jac

eps = 1.e-10


A = np.array([[3, 0, 2], [0, 4, 4], [2, 4, 4]])

print('начальная матрица:')
print(A)
print('собственные числа:')
print(np.linalg.eigvals(A))

print('Выбор обнуляемого элемента по стратегии "преград-барьеров"')
print(Jac.Bound(A, eps))
print('Выбор обнуляемого элемента по максимальному радиуса круга Гершгорина')
print(Jac.Gersh(A, eps))