import math
import numpy


def mc_loren_summary(num, iterates):
    res = 0
    for i in range(1, iterates):
        pre_res = (math.factorial(2 * i) * (num ** i)) / ((1 - 2 * i) * (math.factorial(i) ** 2) * (4 ** i))
        if i % 2 == 0:
            res += pre_res
        else:
            res -= pre_res
    return res


class Complex:
    number = 0
    savedOne = False
    lowerOne = False

    def __init__(self, number):
        self.number = number
        if self.number < 0:
            self.number *= (-1)
        if self.number < 1:
            self.lowerOne = True
            self.number = 2 - self.number

    def sqr(self):
        if self.savedOne:
            module = self.number
            self.number = module * module + 2 * module
            if self.number > 1:
                self.savedOne = False
                self.number += 1
        else:
            self.number = self.number * self.number

    def sqr_n(self, n):
        for i in range(n):
            self.sqr()

    def sqrt(self):
        if numpy.abs(self.number - 1) < 1 and not self.savedOne or numpy.abs(self.number) < 1 and self.savedOne:
            if not self.savedOne:
                self.savedOne = True
                self.number -= 1
            module = self.number
            beta = mc_loren_summary(module, 10)
            self.number = beta
        else:
            self.number = math.sqrt(self.number)

    def sqrt_n(self, n):
        for i in range(n):
            self.sqrt()

    def __str__(self):
        if self.lowerOne:
            if self.savedOne:
                return str.replace(str(2 - self.number), "1.", "0.")
            else:
                return str(2 - self.number)
        else:
            if self.savedOne:
                return str.replace(str(self.number), "0.", "1.")
            else:
                return str(self.number)


def main(num, iterates=100):
    x = Complex(num)
    print("sqrt and sqr " + str(iterates) + " times:")
    print(x)
    x.sqrt_n(iterates)
    x.sqr_n(iterates)
    print(x)


main(5, 100)
