import numpy as np
import matplotlib.pyplot as plt
import math 
''' 
	Задаем начальные условия
Решаем задачу y' = Ay + b(x)
y - размерности m,
А - матрица постоянных коэффициентов,
x - независимая переменная.
Выбираем начальные x и x_1
Выбираем кол-во точек сетки N, считаем шаг h

'''


''' оценка для N '''
def nk(A):
	return 2*int(np.abs(A).max())


''' оценка погрешности '''

def err( p, Y1, Y2):
	er = 1/(2**p - 1)*np.abs(np.subtract(Y2[::2], Y1))
	return er.max()


''' Метод Рунге-Кутты '''

def RK(A, x_0, x_1, Y, N):
	Y_RK = np.zeros((N+1, len(Y))) 	
	Y_RK[0] = Y
	naned = np.isnan
	A_dot = A.dot
	h = (x_1 - x_0)/N 
	for i in range(N):
		if np.any(naned(Y_RK)):
			print('Решение приблизилось к nan, пощадите метод Рунге-Кутты')
			Y_RK[i] = np.zeros(len(Y))
		q_1 = h*A_dot(Y_RK[i])
		q_2 = h*A_dot(Y_RK[i] + q_1/2.0)
		q_3 = h*A_dot(Y_RK[i] + q_2/2.0)
		q_4 = h*A_dot(Y_RK[i] + q_3) 
		Y_RK[i+1] = Y_RK[i] + (q_1 + 2.0 * q_2 + 2.0 * q_3 + q_4)/6.0 
	return Y_RK

''' Реализация Метод Адамса'''

def Adams(A, x_0, x_1, Y, N):

	m = len(Y)
	Y_A = np.zeros((N+1, m))
	Y_A[0] = Y
	A_dot = A.dot
	h = (x_1 - x_0)/N
	E = np.eye
	solve = np.linalg.solve

	q_1 = (A_dot(Y))
	q_2 = (A_dot(Y + h*q_1/2.0))
	q_3 = (A_dot(Y + h*q_2/2.0))
	q_4 = (A_dot(Y + h*q_3))
	Y_A[1] = Y + h*(q_1 + 2.0 * q_2 + 2.0 * q_3 + q_4)/6.0 

	for i in range(N - 1):
		B = E(m) - 5/12*h*A
		c = Y_A[i+1] + h/12*A_dot(8*Y_A[i+1] - Y_A[i])
		Y_A[i+2] = solve(B,c) 

	return Y_A  


''' Реализация метода CROS '''

def CROS(A, x_0, x_1, Y, N):
	m = len(Y)
	Y_CROS = np.zeros((N+1, m))
	Y_CROS[0] = Y
	A_dot = A.dot
	h = (x_1 - x_0)/N
	E = np.eye
	solve = np.linalg.solve
	for i in range(N):
		B = E(m) - (1 + 1.0j)/2*h*A
		w = solve(B, A_dot(Y_CROS[i]))
		Y_CROS[i+1] = Y_CROS[i] + h*(w.real)
	return Y_CROS	

'''вычисление до требуемой погрешности '''

def pres_RK(A, x_0, x_1, Y_0, k_1, k1_max, e):
	err_1 = []
	xs_1 = []
	Y_RK = RK(A, x_0, x_1, Y_0, k_1)
	while True:
		k_1*=2
		temp = RK(A, x_0, x_1, Y_0, k_1)
		er = err(4, Y_RK , temp )
		err_1.append(er)
		xs_1.append(k_1)
		Y_RK = temp
		if er < e or k_1 > k1_max:
			break
	return {'value': Y_RK.T,'error' : [xs_1, err_1]}

def pres_A(A, x_0, x_1, Y_0, k_2, k2_max, e):
	err_2 = []
	xs_2 = []
	Y_A = Adams(A, x_0, x_1, Y_0, k_2)		
	while True:
		k_2 *=2
		temp = Adams(A, x_0,x_1, Y_0, k_2)
		er = err(3, Y_A , temp )
		err_2.append(er)
		xs_2.append(k_2)
		Y_A = temp
		if er < e or k_2 > k2_max:
			break
	return {'value' : Y_A.T, 'error' : [xs_2, err_2]}
			
def pres_CROS(A, x_0, x_1, Y_0, k_3, k3_max, e):
	err_3 = []
	xs_3 = []
	Y_CROS = CROS(A, x_0, x_1, Y_0, k_3)
	while True:
		k_3*=2
		temp = CROS(A, x_0, x_1, Y_0, k_3)
		er = err(2, Y_CROS , temp)
		err_3.append(er)
		xs_3.append(k_3)
		Y_CROS = temp
		if er < e or k_3 > k3_max:
			break
	return {'value': Y_CROS.T, 'error' :[xs_3, err_3]}

''' рисуем графики '''

def err_view(e1, e2, e3):
	plt.yscale('log')
	plt.xscale('log')
	plt.xlabel('N, log')
	plt.ylabel('Delta, log')
	plt.plot( e1[0], e1[1], label = 'RK', marker = 'o', lw = 0)
	plt.plot( e2[0], e2[1], label = 'Adams', marker = 'o', lw = 0)
	plt.plot( e3[0], e3[1], label = 'CROS', marker = 'o' ,lw = 0 )
	plt.legend()
	plt.show()

def p_view(e1, e2, e3):
	
	p_1 = [math.log(e1[1][i]/e1[1][i+1])/math.log(2) for i in range(len(e1[1]) - 1) ]
	p_2 = [math.log(e2[1][i]/e2[1][i+1])/math.log(2) for i in range(len(e2[1]) - 1) ]
	p_3 = [math.log(e3[1][i]/e3[1][i+1])/math.log(2) for i in range(len(e3[1]) - 1) ]

	plt.xscale('log')
	plt.xlabel('N, log')
	plt.ylabel('p, log')
	plt.plot( e1[0][:-1], p_1, label = 'RK', marker = 'o', lw = 0)
	plt.plot( e2[0][:-1], p_2, label = 'Adams', marker = 'o', lw = 0)
	plt.plot( e3[0][:-1], p_3, label = 'CROS', marker = 'o' ,lw = 0 )
	plt.legend()
	plt.show()

''' график функции (чтобы строить, зная k)'''

def f_view(Y, x_0, x_1, name, num = [0]):
	k = len(Y[0])
	h = (x_1 - x_0)/k
	x = [x_0 + h*i for i in range(k)]
	for i in num:
		plt.plot( x, Y[i], label = name + ', y_' + str(i)) 
	plt.ylabel('y')
	plt.xlabel('x')
	plt.legend()
	plt.show()	
	