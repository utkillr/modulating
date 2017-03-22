import numpy as np
import Lab2.mean_core as util
import Lab2.task_kahan_core as kahan

def kahan_mean(x):
    return kahan.kahan_sum(x) / len(x)

def oneline_variance_kahan(x):
    n = len(x)
    m = x[0]  # мат ожидание
    m2 = (x[0] + x[1]) / 2.0  # следующее мат ожидание
    res = (x[0] - m) ** 2 + n * (m - m2) ** 2
    alpha = 0.0
    for i in range(1, n - 1):
        m = m2
        alpha = m - m2
        m2 = (m2 * (i + 1) + x[i + 1]) / (i + 2)
        res = (x[i] - m) ** 2 + alpha ** 2
    # res += alpha * n
    return res


def main(mean, delta):
    x = util.samples(1000000, mean, delta)

    print("Exact var, Direct first var, My var:")
    print(util.exact_variance(delta), util.direct_first_var(x), oneline_variance_kahan(x))

    print()

    print("Размер выборки:\t\t", len(x))
    print("Среднее значение:\t", util.exact_mean(mean))
    print("Оценка дисперсии:\t", util.exact_variance(delta))

    print()

    print("Ошибка среднего для встроенной функции:\t\t", util.relative_error(util.exact_mean(mean), np.mean(x)))
    print("Ошибка дисперсии для встроенной функции:\t", util.relative_error(util.exact_variance(delta), np.var(x)))

    print()

    print("Ошибка среднего для последовательного суммирования:", util.relative_error(util.exact_mean(mean), util.direct_mean(x)))

    print()

    print("Ошибка первой оценки дисперсии для последовательного суммирования:\t",
          util.relative_error(util.exact_variance(delta), util.direct_first_var(x)))
    print("Ошибка моей оценки дисперсии для последовательного суммирования:\t",
          util.relative_error(util.exact_variance(delta), oneline_variance_kahan(x)))


main(1e6, 1e-5)