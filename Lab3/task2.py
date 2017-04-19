import numpy as np
import matplotlib.pyplot as plt
import math


def get_derivative(x, n):
    if n == 0:
        return np.log(x)
    else:
        return ((-1) ** (n + 1)) * 1.0 * math.factorial(n - 1) / (x ** n)


def get_r(x, n):
    return get_derivative(x + 1, n + 1) * (x ** (n + 1)) / math.factorial(n + 1)


def get_s(x, n):
    return ((-1) ** n) * (x ** n) / n


def relative_error(x0, x):
    return np.abs(x0 - x) / np.abs(x0)


def counted_r(teta, n):
    r = 1.0 / (n * (teta ** (n + 1)))
    return r


def log_teylor_series(x, eps=0.05):
    a = x - 1
    res = a
    k = 1
    while counted_r(1, k) > eps:
        # while get_r(a, k) > eps:
        res += get_s(a, k)
        k += 1
    return res


def main():
    x0 = np.logspace(-5, 5, 1001, dtype=np.double)
    epsilon = np.finfo(np.double).eps
    best_precision = (epsilon / 2) * np.abs(1. / np.log(x0))

    x = np.logspace(-5, 1, 1001)
    y0 = np.log(x)
    y = []
    for elem in x:
        y.append(log_teylor_series(elem, 0.01))
    plt.loglog(x, relative_error(y0, y), '-k')
    plt.loglog(x0, best_precision, '--r')
    plt.xlabel('$x$')
    plt.ylabel('$(y_0-y)/y_0$')
    plt.legend(["$Достигнутая\;погр.$", "$Минимальная\;погр.$"], loc=5)
    plt.show()

def debug():
    x = 1.1
    y = np.log(x)
    my = log_teylor_series(x)
    print(x, y, my)

#main()
debug()