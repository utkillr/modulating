import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.interpolate


def relative_error(x0, x):
    return np.abs(x0 - x) / np.abs( x0 )


def redux_div(x):
    arg = 1
    return redux_div_inner(x, arg)


def redux_div_inner(x, arg):
    if x < 0:
        raise ValueError("Can't evaluate log(negative)")
    if x == 0:
        raise ValueError("Can't evaluate log(0)")
    if 0 < x < 1:
        arg -= arg/2
        x *= 2
        return redux_div_inner(x, arg)
    if 1 <= x <= 2:
        return x, arg
    if arg == 0: arg += 1
    else: arg += arg
    x /= 2
    return redux_div_inner(x, arg)


def redux_div_arg(arg):
    multiplier = 1
    if arg > 2:
        while arg != 2:
            arg /= 2
            multiplier += 1
    else:
        while arg != 2:
            arg *= 2
            multiplier -= multiplier/2
    return arg, multiplier


def log_newton(x, N=10):
    y = 1
    for i in range(N):
        y = y - 1 + x/np.exp(y)
    return y

def my_log(param):
    x = param
    x, arg = redux_div(x)
    arg, mult = redux_div_arg(arg)

    y = log_newton(x)

    return y + mult * np.log(arg)


def my_log_frexp(param):
    M, E = np.frexp(param)
    y = log_newton(M)

    return y + E * np.log(2)


def debug(param):
    x = param
    x, arg = redux_div(x)
    arg, mult = redux_div_arg(arg)
    print("Param: ", param)
    print("Function: log(", param, ")")
    print("Reduced: log(", x, ") +", mult, "* log(", arg, ")")

    y = log_newton(x)

    print("Result:", y, "+", mult, "* log(", arg, ")")

    print("=", y + mult * np.log(arg))


def main():
    x = np.logspace(-3, 3, 1000)
    y = np.log(x)
    y_newton = log_newton(x)
    y_my = []
    for item in x:
        y_my.append(my_log(item))

    plt.loglog(x, relative_error(y_my, y), '-g')
    plt.loglog(x, relative_error(y_newton, y), '-r')
    plt.xlabel("$Argument")
    plt.ylabel("Relative\;error$")
    plt.show()


def main2():
    x = np.logspace(-3, 3, 1000)
    y = np.log(x)
    y_newton = log_newton(x)

    y_my = my_log_frexp(x)
    #y_my = []
    #for item in x:
    #    y_my.append(my_log(item))

    plt.loglog(x, relative_error(y_my, y), '-g')
    plt.loglog(x, relative_error(y_newton, y), '-r')
    plt.xlabel("$Argument")
    plt.ylabel("Relative\;error$")
    plt.show()


main2()