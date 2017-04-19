from math import factorial
import numpy as np
import matplotlib.pyplot as plt


def relative_error(x0, x): return np.abs(x0 - x) / np.abs(x0)


def log_teylor_series(x, eps=0.000001):
    res = []
    for el in x:
        a = el - 1
        a_k = a
        y = a
        k = 2
        while calculate_end(a, k) > eps:
            a_k = -a_k * a
            y = y + a_k / k
            k += 1
        res.append(y)
    return res

log_const = np.log(np.sqrt(2))

def calculate_end(a, N):
    res = (a + 1) ** (N + 1) / (N + 1) / (1 - np.abs(a + 1)) / log_const
    return res


x0 = np.logspace(-5, 5, 1000, dtype=np.double)
epsilon = np.finfo(np.double).eps
best_precision = (epsilon / 2) * np.abs(1. / np.log(x0))

x = np.logspace(-5, 1, 1000)
y0 = np.log(x)
y = log_teylor_series(x)
plt.loglog(x, relative_error(y0, y), '-k')
plt.loglog(x0, best_precision, '--r')
log_const = np.log(np.sqrt(100000))
y1 = log_teylor_series(x)
plt.loglog(x, relative_error(y0,y1), '--b')

plt.xlabel('$x$')
plt.ylabel('$(y_0-y)/y_0$')
plt.legend(["$Real\;2 error.$", "$Min\;error.$","$Real\;100000 error.$"], loc=5)
plt.show()