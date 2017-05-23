import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.interpolate


def relative_error(x0, x):
    return np.abs(x0 - x) / np.abs( x0 )

def log_newton(x, N=10):
    y = 1
    for i in range(N):
        y = y - 1 + x/np.exp(y)
    return y

def my_log_frexp(param):
    M, E = np.frexp(param)
    y = log_newton(M)

    return y + E * np.log(2)

def main2():
    x = np.logspace(-3, 3, 1000)
    y = np.log(x)

    y_newton = log_newton(x)
    y_my = my_log_frexp(x)

    plt.loglog(x, relative_error(y_my, y), '-g')
    plt.loglog(x, relative_error(y_newton, y), '-r')
    plt.xlabel("$Argument")
    plt.ylabel("Relative\;error$")
    plt.show()


main2()