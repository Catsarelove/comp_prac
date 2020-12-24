import numpy as np
import matplotlib.pyplot as plt





def err( Y1, Y2):
	er = np.abs(np.subtract(Y2[::2], Y1))
	return er.max()

solve = np.linalg.solve

def sol(q, r, f, x_0, x_1, N, a, b):
	h = (x_1 - x_0)/N
	u_0 = [a[0] + 3*a[1]/2/h, -2*a[1]/h, a[1]/2/h]
	u_1 = [b[0] + 3 * b[1]/2 /h,-2 * b[1] / h, b[1] /2/h]
	A = np.zeros([N, N])
	A[0, 0:3] = u_0
	A[N-1, N-3: N+1] = u_1
	c = np.zeros(N)
	c[0] = a[2]
	c[1: N - 1] = [f(x_0 + h*i) for i in range(1, N-1)]
	c[N - 1] = b[2]
	                                                                                                                                                    
	Q = [q(x_0 + h*i) for i in range(1, N-1)]
	R = [r(x_0 + h*i) for i in range(1, N-1)]

	for i in range(1, N - 1):
		A[i, i - 1] = 1/h/h - Q[i - 1] /2/h
		A[i, i] = -(2/h/h + R[i - 1])
		A[i, i + 1] = 1/h/h + Q[i - 1]/2/h
	print('Iter done')
	return solve(A, c)

def pres_sol(q, r, f, x_0, x_1, N, a, b, e):
	err_1 = []
	xs_1 = []
	U = sol(q, r, f, x_0, x_1, N, a, b)
	while True:
		N*=2
		temp = sol(q, r, f, x_0, x_1, N, a, b)
		er = err(U , temp )
		err_1.append(er)
		xs_1.append(N)
		U = temp
		if er < e or N > 1.e+6:
			print('Количество итераций: ', len(xs_1))
			break
	return U, [xs_1, err_1]




