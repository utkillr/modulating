import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.interpolate

x0 = np.logspace(-5, 5, 1000, dtype=np.double)
epsilon = np.finfo(np.double).eps
best_precision = (epsilon / 2) * np.abs(1. / np.log(x0))

def relative_error(x0, x):
    return np.abs(x0 - x) / np.abs( x0 )

def getcos(n, N):
    return math.cos(math.pi * (n + 0.5) / (N + 1))

def  main(N = 10, top = 3):
    xn = 1 + 4. / (1 + np.arange(N))
    yn = np.log(xn)

    print(xn)

    # Тестовые точки
    x = np.linspace(1 / 5, top, 1000, dtype=np.double)
    y = np.log(x)

    # Узлы итерполяции
    x_cheb = []
    for i in range(0, N):
        u_ = getcos(i, N)
        x_cheb.append((1 + (2 * u_ / 3)) / (1 - (2 * u_ / 3)))
    y_cheb = np.log(x_cheb)

    u = []
    for i in range(0, N):
        u.append(getcos(i, N))

    ux = (3 * x - 3) / (2 * (1 + x))



    # Многочлен лагранжа
    lagrange_n = scipy.interpolate.lagrange(xn, yn)
    lagrange_cheb = scipy.interpolate.lagrange(u, y_cheb)

    y_lagrange_n = lagrange_n(x)
    y_lagrange_cheb = lagrange_cheb(ux)

    # чистый логарифм
    plt.plot(x, y, '-k')
    # логарифм по точкам n
    plt.plot(xn, yn, '.r')
    # логарифм по точкам Чебышева
    #plt.plot(x_cheb, y_cheb, '.b')
    # логарифм по интерполяции по точкам n
    plt.plot(x, y_lagrange_n, '-r')
    # логарифм по интерполяции по точкам Чебышева
    #plt.plot(x, y_lagrange_cheb, '-b')
    plt.xlabel("$x$")
    plt.ylabel("$y=\ln x$")
    plt.show()

    # погрешность по точкам n
    plt.semilogy(x, relative_error(np.log(x), lagrange_n(x)), '-r')
    # погрешность по точкам Чебышева
    plt.semilogy(x, relative_error(np.log(x), lagrange_cheb(ux)), '-b')
    plt.xlabel("$x$")
    plt.ylabel("$y=\ln x$")
    plt.show()

main(20, 5)