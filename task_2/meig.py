import math
import numpy as np


def regular_h(A, b, a, x_0):
	r_A = A + a*np.eye(len(A[0]))
	b = b + a*x_0
	return [r_A, b]
	
def regular_nh(A, b, a, x_0):
	A = A.T@A
	b = A.T@A
	return regular_h(A, b, a, x_0)

def x(A, b):
	m = len(A[0])
	x_1 = np.zeros(m)
	for i in range(m):
		s = b[i]
		for k in range(i):
			s = s - A[i][k]*x_1[k]
		x_1[i] = s/A[i][i]
	return x_1

def x_(A, b):
	m = len(A[0])
	x_1 = np.zeros(m)
	for i in range(1, m+1):
		s = b[m-i]
		for k in range(1, i):
			s = s - A[m - i][m - k]*x_1[m - k]
		x_1[m - i] = s/A[m - i][m - i]
	return x_1

def cond(A):
	nr = np.linalg.norm
	return nr(A)*nr(np.linalg.inv(A))

def Rot(A, b):
	m = len(A[0])
	Temp = A
	Q = np.eye(m)
	for j in range(0, m):
		for i in range(j+1, m):
			T = np.eye(m)
			z_j = Temp[j][j]
			z_i = Temp[i][j]
			z = math.sqrt(z_j*z_j + z_i*z_i)
			c = -z_j/z
			s = z_i/z    
			T[i, i] = c
			T[j, j] = c
			T[i][j] = s
			T[j][i] = -s
			Temp = T@Temp
			Q = Q@np.transpose(T) 
	Q = Q.T
	x_1 = Q.dot(b)
	x = x_(Temp, x_1)
	return x


def LU(A, b):
	m = len(A[0])
	E = np.eye
	L = E(m)	
	for i in range(m-1):
		M = E(m)
		M_1 = E(m)
		for j in range(i+1, m):
			if A[i][i] == 0:
				print('Либо матрица вырождена, либо не имеет LU разложения :(')
				return np.zeros(m) 			
			M[j][i] = -(A[j][i])/(A[i][i])
			M_1[j][i] = (-1)*M[j][i]	
		L = L@M_1
		A = M@A
		
	x_1 = x(L, b)
	x_2 = x_(A, x_1)
	return x_2
	

