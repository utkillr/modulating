import numpy as np
import Lab2.mean_core as util
import Lab2.task_kahan_core as kahan

def kahan_mean(x):
    return kahan.kahan_sum(x) / len(x)

def oneline_variance_kahan(x):
    m_now = x[0]
    m_next = (x[1])
    x_now = x[0]

    summ = 0.0
    error_summ = 0.0
    for n in range(1, len(x) - 1):
        sum_member = (x_now - m_now) ** 2 + len(x) * ((m_now - m_next) ** 2)
        y = sum_member - error_summ
        t = summ + y
        error_summ = (t - summ) - y
        summ = t

        m_now = m_next
        m_next = (m_now * (n) + x[n + 1]) / (n + 1)

    sum_member = (x_now - m_now) ** 2 + len(x) * ((m_now - m_next) ** 2)
    y = sum_member - error_summ
    t = summ + y
    error_summ = (t - summ) - y
    summ = t

    return summ


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