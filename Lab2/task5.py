import numpy as np
import Lab2.mean_core as util


def main(mean, delta):
    x = util.samples(1000000, mean, delta)

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
    print("Ошибка второй оценки дисперсии для последовательного суммирования:\t",
          util.relative_error(util.exact_variance(delta), util.direct_second_var(x)))
    print("Ошибка второй оценки дисперсии для однопроходного суммирования:\t\t",
          util.relative_error(util.exact_variance(delta), util.oneline_second_var(x)))


main(1e6, 1e-5)