import math
import numpy as np
import meig
import matplotlib.pyplot as plt

nr = np.linalg.norm

A = np.zeros((15, 15))
for i in range(15):
	for j in range(15):
		A[i][j] = 1/(i + j + 1)	
lst = [math.cos(i) for i in range(15)]
b = np.array(lst)


print('Условия:')
print('A:')
print(A)
print('b:')
print(b)

print('реальное решение:')
x = np.linalg.solve(A,b)
print(x)

print('решение методом вращений:')
r = meig.Rot(A, b)
print(r)


print('решение методом LU:')
lu = meig.LU(A,b)
print(lu)


print('будем менять параметр регуляризации от 1.e-3 - 1.e+3')
a_ = np.array([0, 1.e-5, 1.e-4, 1.e-3, 1.e-2, 0.1, 1, 10, 100, 1000])
r_p = np.zeros(10)
lu_p = np.zeros(10)
c_ = np.zeros(10)
i = 0
for a in a_:
	Res = meig.regular_h(A,b,a,x)
	r_1 = meig.Rot(Res[0], Res[1])
	r_p[i] = nr(abs(x-r_1))
	
	c_[i] = meig.cond(Res[0])
	
	Res_1 = meig.regular_h(A,b,a,x)
	lu_1 = meig.LU(Res_1[0],Res_1[1])
	lu_p[i] = nr(abs(x - lu_1))
	
	
	i+= 1



''' строим графики для погрешности и числа обусловленности'''

plt.plot(a_, r_p, label = 'Метод вращений', marker = 's',markersize = 7, lw = 0, c = 'magenta')
plt.plot(a_, lu_p, label = 'LU разложение', marker = 's', markersize = 7, lw = 0)
plt.xlabel('параметр a')
plt.ylabel('погрешность вычислений')
plt.yscale('log')
plt.xscale('log')
plt.legend()
plt.show()

plt.plot(a_, c_, marker = 's',markersize = 7, lw = 0, c = 'magenta')
plt.xlabel('параметр a')
plt.ylabel('число обусловленности')
plt.yscale('log')
plt.xscale('log')
plt.show()
