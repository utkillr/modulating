import numpy as np


def relative_error(x0, x):
    return np.abs(x0-x)/np.abs(x)


def samples(k, base):
    # K pieces of base^K values
    parts = [np.full((base**i,), float(base)**(-i)/k) for i in range(0, k)]
    # samples
    samples = np.concatenate(parts)
    # mix
    return np.random.permutation(samples)


def exact_sum(x):
    return 1.


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

def main(k, base):
    x = samples(k, base)

    print(x)

    print("Amount of elements:", len(x))
    print("Max and min:", np.min(x), np.max(x))

    exact_sum_for_x = exact_sum(k)
    direct_sum_for_x = direct_sum(x)

    print("Error of direct sum:", relative_error(exact_sum_for_x, direct_sum_for_x))

    sorted_x = x[np.argsort(x)]
    sorted_sum_for_x = direct_sum(sorted_x)
    print("Error of upsorted sum:", relative_error(exact_sum_for_x, sorted_sum_for_x))

    sorted_x = x[np.argsort(x)[::-1]]
    sorted_sum_for_x = direct_sum(sorted_x)
    print("Error of downsorted sum:", relative_error(exact_sum_for_x, sorted_sum_for_x))

    Kahan_sum_for_x = kahan_sum(x)  # сумма всех элементов по порядку
    print("Погрешность суммирования по Кэхэну:", relative_error(exact_sum_for_x, Kahan_sum_for_x))

main(7, 10)
