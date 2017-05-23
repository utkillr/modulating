# coding=utf-8
import scipy.interpolate
import matplotlib.pyplot as plt
import numpy as np
import math


def relative_error(x0, x):
    return np.abs(x0 - x) / np.abs(x0)


B = 8  # число используемых для составления таблицы бит мантиссы
table = np.log((np.arange(2 ** (B - 1), 2 ** B, dtype=np.double)) / (2 ** B))
log2 = np.log(2)


def log_table(x):
    M, E = np.frexp(x)
    index = (M * 2 ** B).astype(np.int)
    return log2 * E + table[index - 2 ** (B - 1)]


def table_new(x):
    M, E = np.frexp(x)
    index = (M * 2 ** B).astype(np.int) + 1
    if index == 2 ** B:
        index = 2 ** (B - 1)
        E += 1
    return log2 * E + table[index - 2 ** (B - 1)]


def get_diff(x):
    M, E = np.frexp(x)
    M *= 2 ** B
    M -= math.trunc(M)
    return M


def log_table_polinom_one_pow(x):
    res = []
    for el in x:
        y1 = log_table(el)
        y2 = table_new(el)
        y_ = y1 + (y2 - y1) * get_diff(el)
        res.append(y_)
    return res

x = np.logspace(-10, 10, 1000)
y0 = np.log(x)

plt.loglog(x, relative_error(y0, log_table(x)), '-r')
plt.loglog(x, relative_error(y0, log_table_polinom_one_pow(x)), '-g')

plt.xlabel("Argument")
plt.ylabel("Relative\;error$")
plt.show()
