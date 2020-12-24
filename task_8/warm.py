import numpy as np
import matplotlib.pyplot as plt
import math
import pylab
from mpl_toolkits.mplot3d import Axes3D

def L(n, x_0, x_1, a, f):
	h = (x_1 - x_0)/(n-1)
	L = np.zeros((n,n))
	for i in range(n):
		L[i][i] = -2*a/(h*h)
		if i != 0:
			L[i][i-1] = a/(h*h)
		if i != n-1:
			L[i][i+1] = a/(h*h)
	F = lambda t: np.array([f(x_0 + h*i, t) for i in range(n)])
	return L, F

def ex(A, t_0, t_1, Y, N, F, m_2, m_3):
	m = len(Y)
	Y_ = np.zeros((N+1, m))
	Y_[0] = Y
	A_dot = A.dot
	h = (t_1 - t_0)/N
	for i in range(1, N+1):
		if np.any(np.isnan(Y_[i])):
			print('метод не сходится')
			return Y_
		Y_[i] = Y_[i-1] + h*(A_dot(Y_[i-1]) + F(t_0 + h*(i-1)))
		Y_[i][0] = m_2(t_0 + h*i)
		Y_[i][m-1] = m_3(t_0 + h*i)
	return Y_

def CROS(A, t_0, t_1, Y, N, F, m_2, m_3):
	m = len(Y)
	Y_CROS = np.zeros((N+1, m))
	Y_CROS[0] = Y
	A_dot = A.dot
	h = (t_1 - t_0)/N
	solve = np.linalg.solve
	for i in range(N):
		B = np.eye(m) - (1 + 1.0j)/2*h*A
		w = solve(B, A_dot(Y_CROS[i]) + F(t_0 + h*i))
		Y_CROS[i+1] = Y_CROS[i] + h*(w.real)
		Y_CROS[i+1][0] = m_2(t_0 + h*(i+1))
		Y_CROS[i+1][m-1] = m_3(t_0 + h*(i+1))
	return Y_CROS	


def Sol(u, N, n, x_0, x_1, t_0, t_1, a, f, m_1, m_2, m_3):
	h_1 = (x_1 - x_0)/n
	h_2 = (t_1 - t_0)/N	
	x_ = np.array([x_0 + h_1*i for i in range(n+1)])
	t_ = np.array([t_0 + h_2*i for i in range(N+1)])
	u_0 = np.array([m_1(x) for x in x_])
	
	l, F = L(n+1, x_0, x_1, a, f)
	u_1 = ex(l, t_0, t_1, u_0, N, F, m_2, m_3)
	u_2 = CROS(l, t_0, t_1, u_0, N, F, m_2, m_3) 
	Real = np.zeros((N+1, n+1))
	for i  in range(N+1):
		for j in range(n+1):	
			Real[i][j] = u(t_[i], x_[j])

	Err_1 = np.abs(np.subtract(Real, u_1))
	print(Err_1)
	print(Err_1.max())
	Err_2 = np.abs(np.subtract(Real, u_2))
	print(Err_2)
	print(Err_2.max())        
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	T, X = np.meshgrid(t_, x_) 
	ax.plot_surface(T, X, Err_2.T, label = 'Явная схема')
	plt.show()
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.plot_surface(T, X, Err_2.T, label = 'Неявная схема')
	plt.show()

