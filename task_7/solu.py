import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import quad

def rec(p_1, p_2, n):
	return lambda x: (2*n +1)/(n+1)*x*p_1(x) - n/(n+1)*p_2(x)
def dif(p_1, p_2, i):
	return lambda x: i*(p_2(x) - x*p_1(x)) - 2*x*p_1(x)
def dif_2(p_1, p_2,p_3, i):
	return lambda x: -(i+2)*p_1(x) + i/(1-x*x)*((i-1)*(p_3(x) - x*p_2(x)) - (i+2)*x*(p_2(x) - x*p_1(x)))

def solv(n, f, k, k_d, q, u_0):
	d = np.zeros(n)
	C = np.zeros((n,n))
	p = []
	p.append(lambda x: 1.0)
	p.append(lambda x: x)
	for i in range(1, n - 1):
		p.append(rec(p[i], p[i-1], i))                                                                  

	p_d = [lambda x: -2*x]
	for i in range(1, n):
		p_d.append(dif(p[i], p[i-1], i)) 

	for i in range(n):
		d[i] = quad(lambda x, i: f(x)*p[i](x)*(1 - x*x), -1, 1, args = (i))[0]
	for i in range(n):
		for j in range(n):
			C[i][j] = quad(lambda x, i, j: k(x)*p_d[i](x)*p_d[j](x) + q(x)*p[i](x)*p[j](x)*(1-x*x)**2, -1, 1, args = (i,j))[0]

	t_ = [math.cos((2*k - 1)*math.pi/(2*n)) for k in range(1, n+1)]
	
	g = [f(t_[i]) for i in range(n)]

	p_d_2 = [lambda x: -2.0, lambda x: -6.0*x]
	for i in range(2, n):
		p_d_2.append(dif_2(p[i], p[i-1], p[i-2], i))
	H = np.zeros((n,n))

	for j in range(n):
		for i in range(n):
			H[j][i] = -k_d(t_[j])*p_d[i](t_[j]) - k(t_[j])*p_d_2[i](t_[j]) + q(t_[j])*p[i](t_[j])*(1 - t_[j]*t_[j])
 
	b_2 = np.linalg.solve(H, g)
	b = np.linalg.solve(C, d)
	u = np.zeros(81)
	u_2 = np.zeros(81)
	x_ = [-1 + i/40 for i in range(81)]
	for i in range(81):     
		for j in range(n):
			u[i]+=b[j]*p[j](x_[i])*(1-x_[i]*x_[i])

	for i in range(81):
		for j in range(n):
			u_2[i]+=b_2[j]*p[j](x_[i])*(1-x_[i]*x_[i])


	y = [ u_0(x) for x in x_]
	err = np.abs(y - u)
	err_2 = np.abs(y - u_2)
	plt.plot(x_, err, marker = '.',label = 'Ritz', lw = 0)

	plt.plot(x_, err_2, marker = '.',label = 'Collocation', lw = 0)
	plt.xlabel('x')
	plt.ylabel('error')
	plt.legend()
	plt.show()
	



