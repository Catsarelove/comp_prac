import numpy as np
import math

def norm(v):
	r = v.dot(v)
	r = math.sqrt(r)
	return r

def Power(A, x, eps):
	
	n = 3
	A_dot = A.dot
	m = len(A[0])
	x_1 = x 
	x_2 = A.dot(x_1)
	x_3 = A_dot(x_2)

	while n < 1000 and norm(x_3) != 0:
		n += 1
		if norm(x_3) > 1000 or norm(x_3) < 10*eps:
			nr = norm(x_3)
			x_1, x_2, x_3 = x_1/nr, x_2/nr, x_3/nr
		x_4 = A.dot(x_3)
		par = x_2*x_3 - x_4*x_1
		if abs(par.max()) < eps:
			break
		x_1, x_2, x_3 = x_2, x_3, x_4
	t = norm(x_3)/norm(x_2)	
	print('Количество итераций:',n)
	return t

def Smul(A, x, eps):
	A_dot = A.dot
	T = A.T
	T_dot = T.dot
	n = 3
	m = len(A[0])
	x_1 = x
	y = np.sin(x_1)
	x_2 = A_dot(x_1)
	x_3 = A_dot(x_2) 
	y = T_dot(T_dot(y))

	while n < 1000 and x_3.dot(T_dot(y)) != 0:
		if norm(x_3) > 1000 or norm(x_3) < 10*eps:
			nr = norm(x_3)
			x_1, x_2, x_3 = x_1/nr, x_2/nr, x_3/nr
		if norm(y) > 1000 or norm(y) < 10*eps:
			y = y/norm(y)	
		n+=1 
		y = T_dot(y)
		x_4 = A_dot(x_3)
		par = x_2*x_3 - x_4*x_1
		if abs(par.max()) < eps:
			break
		x_1, x_2, x_3 = x_2, x_3, x_4
	t = x_3.dot(T_dot(y))/x_2.dot(T_dot(y))
	print('Количество итераций:', n)
	return abs(t)


