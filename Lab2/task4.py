import numpy as np
import Lab2.task_kahan_core as util


def main(k):
    x = util.samples(k)

    print("Array:", x)

    print("Amount of elements:", len(x))
    print("Max and min:", np.min(x), np.max(x))

    exact_sum_for_x = util.exact_sum(k)
    direct_sum_for_x = util.direct_sum(x)
    kahan_sum_for_x = util.kahan_sum(x)

    sorted_x = np.array(x)
    sorted_x = sorted_x[np.argsort(sorted_x)]
    print("Upsorted:", sorted_x)
    upsorted_direct_sum_for_x = util.direct_sum(sorted_x)
    upsorted_kahan_sum_for_x = util.kahan_sum(sorted_x)

    sorted_x = np.array(x)
    sorted_x = sorted_x[np.argsort(sorted_x)[::-1]]
    print("Downsorted:", sorted_x)
    downsorted_direct_sum_for_x = util.direct_sum(sorted_x)
    downsorted_kahan_sum_for_x = util.kahan_sum(sorted_x)

    sorted_x = np.array(x)
    sorted_x = sorted_x[np.argsort(np.absolute(sorted_x))]
    print("Upsorted absolute:", sorted_x)
    upsorted_absolute_direct_sum_for_x = util.direct_sum(sorted_x)
    upsorted_absolute_kahan_sum_for_x = util.kahan_sum(sorted_x)

    sorted_x = np.array(x)
    sorted_x = sorted_x[np.argsort(np.absolute(sorted_x))[::-1]]
    print("Downsorted absolute:", sorted_x)
    downsorted_absolute_direct_sum_for_x = util.direct_sum(sorted_x)
    downsorted_absolute_kahan_sum_for_x = util.kahan_sum(sorted_x)

    print("Exact, Direct, Kahan:\t\t\t\t", exact_sum_for_x, direct_sum_for_x, kahan_sum_for_x)
    print("Upsorted Direct, Kahan:\t\t\t\t", upsorted_direct_sum_for_x, upsorted_kahan_sum_for_x)
    print("Downsorted Direct, Kahan:\t\t\t", downsorted_direct_sum_for_x, downsorted_kahan_sum_for_x)
    print("Upsorted absolute Direct, Kahan:\t", upsorted_absolute_direct_sum_for_x, upsorted_absolute_kahan_sum_for_x)
    print("Downsorted absolute Direct, Kahan:\t", downsorted_absolute_direct_sum_for_x, downsorted_absolute_kahan_sum_for_x)

    print()

    print("Error of Direct sum:\t\t\t\t\t", util.relative_error(exact_sum_for_x, direct_sum_for_x))
    print("Error of Kahan sum:\t\t\t\t\t\t", util.relative_error(exact_sum_for_x, kahan_sum_for_x))
    print("Error of upsorted Direct sum:\t\t\t", util.relative_error(exact_sum_for_x, upsorted_direct_sum_for_x))
    print("Error of upsorted Kahan sum:\t\t\t", util.relative_error(exact_sum_for_x, upsorted_kahan_sum_for_x))
    print("Error of downsorted Direct sum:\t\t\t", util.relative_error(exact_sum_for_x, downsorted_direct_sum_for_x))
    print("Error of downsorted Kahan sum:\t\t\t", util.relative_error(exact_sum_for_x, downsorted_kahan_sum_for_x))
    print("Error of upsorted absolute Direct sum:\t", util.relative_error(exact_sum_for_x, upsorted_absolute_direct_sum_for_x))
    print("Error of upsorted absolute Kahan sum:\t", util.relative_error(exact_sum_for_x, upsorted_absolute_kahan_sum_for_x))
    print("Error of downsorted absolute Direct sum:", util.relative_error(exact_sum_for_x, downsorted_absolute_direct_sum_for_x))
    print("Error of downsorted absolute Kahan sum:\t", util.relative_error(exact_sum_for_x, downsorted_absolute_kahan_sum_for_x))

main(50)