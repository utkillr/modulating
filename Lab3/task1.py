import math


def redux_sqr(x, eps):
    arg = 1
    return redux_sqr_inner(x, eps, arg)


def redux_sqr_inner(x, eps, arg):
    if x < 0:
        raise ValueError("Can't evaluate log(negative)")
    if x == 0:
        raise ValueError("Can't evaluate log(0)")
    if 0 < x <= 1:
        if x < 1 - eps:
            arg /= 2
            x *= x
            return redux_sqr_inner(x, eps, arg)
        return x, arg
    if x > 1 + eps:
        arg *= 2
        x = math.sqrt(x)
        return redux_sqr_inner(x, eps, arg)
    return x, arg


def redux_div(x, eps):
    arg = 1
    return redux_div_inner(x, eps, arg)


def redux_div_inner(x, eps, arg):
    if x < 0:
        raise ValueError("Can't evaluate log(negative)")
    if x == 0:
        raise ValueError("Can't evaluate log(0)")
    if 0 < x < 1:
        if 0.5 <= x:
            return x, arg
        arg -= arg/2
        x *= 2
        return redux_div_inner(x, eps, arg)
    if 1 <= x <= 2:
        return x, arg
    if x > 1 + eps:
        if (arg == 0): arg += 1
        else: arg += arg
        x /= 2
        return redux_div_inner(x, eps, arg)
    return x, arg



def redux(x, eps):
    if x > 2:
        x, div = redux_div(x, eps)
    else:
        div = 0
    x, sqr = redux_sqr(x, eps)
    return x, div, sqr


def main(x, eps):
    y, arg_div, arg_sqr = redux(x, eps)
    print("Param: ", x)
    print("Function: log(", x, ")")
    print("Reduced: ", arg_sqr, "* log(", y, ") + log(", arg_div, ")")

main(10, 0.05)