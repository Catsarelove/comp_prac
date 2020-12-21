import numpy as np
import math

def Iter(A, b, eps):
	nr = np.linalg.norm
	m = len(A[0])
	c = np.zeros(m)
	B = np.zeros((m,m))
	for i in range(m):
		if A[i][i] == 0:
			print('!!!')
		c[i] = b[i]/A[i][i]
		for j in range(m):
			if j != i:
				B[i][j] = -A[i][j]/A[i][i]
	x_0 = np.zeros(m)
	N = 0
	while True:
		N+=1
		x = B.dot(x_0) + c
		if nr(x - x_0) < eps:
			x_0 = x
			print('Число итераций метода простых итераций:',N)
			break
		x_0 = x
	return x_0

def Relax(A, b, eps):
	nr = np.linalg.norm
	m = len(A[0])
	c = np.zeros(m)
	B = np.zeros((m,m))
	for i in range(m):
		if A[i][i] == 0:
			print('!!!')
		c[i] = b[i]/A[i][i]
		for j in range(m):
			if j != i:
				B[i][j] = -A[i][j]/A[i][i]
	x_0 = np.zeros(m)
	N = 0
	while True:
		N += 1
		x = np.zeros(m)
		for k in range(m):
			s = c[k]
			for j in range(k):
				s+=B[k][j]*x[j]
			for j in range(k+1, m):
				s+=B[k][j]*x_0[j]
			x[k] = s
		if nr(x_0 - x) < eps:
			x_0 = x
			print('Число итераций метода Зейделя: ', N)
			break
		x_0 = x
	return x_0	


			