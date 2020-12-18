import numpy as np
import matplotlib.pyplot as plt
import math 
import diff as d
'''
x_0 = 0
x_1 = 1.0
'''


e = 0.000001

A = np.array([[0, 1],[-4, 0]])
Y_0 = np.array([0.8, 2])
k_1 = k_2 = k_3 = d.nk(A)

k1_max = 128*k_1
k2_max = 128*k_2
k3_max = 128*k_3

Y_RK = d.pres_RK(A, 0, 1,  Y_0, k_1, k1_max, e)
Y_A = d.pres_A(A, 0, 1, Y_0, k_2, k2_max, e) 
Y_CROS = d.pres_CROS(A, 0, 1, Y_0, k_3 , k3_max, e) 
Y_1 = Y_RK['value']
Y_2 = Y_A['value']
Y_3 = Y_CROS['value']
d.err_view(Y_RK['error'], Y_A['error'], Y_CROS['error'])
d.p_view(Y_RK['error'], Y_A['error'], Y_CROS['error'])
num = [0,1]
d.f_view(Y_1, 0, 1, 'метод Рунге-Кутты', num)
d.f_view(Y_2, 0, 1, 'метод Адамса', num)
d.f_view(Y_3, 0, 1, 'метод CROS', num)

