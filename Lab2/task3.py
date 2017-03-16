import numpy as np
import Lab2.task_kahan_core as util


def main(k):
    x = util.samples(k)

    print(x)

    print("Amount of elements:", len(x))
    print("Max and min:", np.min(x), np.max(x))

    exact_sum_for_x = util.exact_sum(k)
    direct_sum_for_x = util.direct_sum(x)
    kahan_sum_for_x = util.kahan_sum(x)

    print("Exact, Direct, Kahan:", exact_sum_for_x, direct_sum_for_x, kahan_sum_for_x)

    print("Error of direct sum:", util.relative_error(exact_sum_for_x, direct_sum_for_x))
    print("Error of Kahan sum:", util.relative_error(exact_sum_for_x, kahan_sum_for_x))


main(20)
