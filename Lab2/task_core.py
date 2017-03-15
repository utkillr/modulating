import numpy as np


def relative_error(x0, x):
    return np.abs(x0-x)/np.abs(x)


def samples(k):
    samples = []
    for i in range(1, k+1):
        samples.append(np.sin(i))
    return samples


def exact_sum(k):
    return 1/2 * (np.sin(k) + np.cos(k)/np.tan(1/2) + 1/np.tan(1/2))


def direct_sum(x):
    summ = 0.0
    for elem in x:
        summ += elem
    return summ


def kahan_sum(x):
    summ = 0.0
    error_summ = 0.0
    for elem in x:
        y = elem - error_summ
        t = summ + y
        error_summ = (t - summ) - y
        summ = t
    return summ