import numpy as np
import matplotlib.pyplot as plt
import math 
Pi = math.pi
atan = math.atan
din = math.sin
cos = math.cos
E = np.eye
sq = math.sqrt
sign = np.sign
sq_2 = sq(2)


def T_(A, i, j):
	m = len(A[0])
	T = E(m)

	x = -2*A[i][j]
	y = A[i][i] - A[j][j]
	if abs(y) < 1.e-20:
		c = s =	1/sq_2	
	else:
		c = sq(0.5 * ( 1 + abs(y)/sq(x*x + y*y) ) )
		s = sign(x*y)*abs(x)/(2*c*sq(x*x + y*y) )

	T[i][i] = c
	T[j][j] = c
	T[j][i] = s
	T[i][j] = -s     
	return T


def R(A):
	m = len(A[0])
	r = np.zeros(m)
	for i in range(m):
		s = 0
		for j in range(m):
			if i != j:
				s+= A[i][j]*A[i][j]
		r[i] = s
	return r

def R_i(A, i):
	s = 0
	for j in range(len(A[0])):
		if j != i:
			s+=A[i][j]*A[i][j]
	return s

def b(A):
	s = 0
	m = len(A[0])
	for i in range(m):
		for j in range(m):
			if i != j:
				s+=A[i][j]*A[i][j]
	return s


def Gersh(A, eps):
	n = 0
	m = len(A[0])
	abs = np.abs
	am = np.argmax
	r = R(A)

	while r.max() > eps:
		k = am(r)
		j = 0	            
		for i in range(m):
			if i != k and abs(A[k][i]) > abs(A[k][j]):
				j = i
		r[j] = R_i(A, j)
		r[k] = R_i(A, k)
		
		t = T_(A, k, j)
		A = t@A@t.T
		print(A)
		n += 1
	eign = [A[i][i] for i in range(m)]
	print('Количество итераций по кругам Гершгорина: %d', n)
	return eign



def Bound(A, eps):
	n = 0
	e_1 = A.max()
	m = len(A[0])
	while b(A) > eps:
		
		for j in range(m):
			for k in range(m):
				if k != j and abs(A[j][k]) >= e_1:
					t = T_(A, j, k)
					A = t@A@t.T
					n+=1
		e_1 = e_1/4
	eign = [A[i][i] for i in range(m)]
	print('Количество итераций по стратегии "преград-барьеров": %d', n)
	return eign
