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
    mc_loren_accuracy = 10
    number = 0
    savedOne = False
    lowerOne = False

    def __init__(self, number, mc_loren_accuracy=10):
        self.number = number
        if self.number < 0:
            self.number *= (-1)
        if self.number < 1:
            self.lowerOne = True
            self.number = 2 - self.number

        self.mc_loren_accuracy = mc_loren_accuracy

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
            beta = mc_loren_summary(module, self.mc_loren_accuracy)
            self.number = beta
        else:
            self.number = math.sqrt(self.number)

    def sqrt_n(self, n):
        for i in range(n):
            self.sqrt()

    def magic_function(self, iterates, out):
        self.sqrt_n(iterates)
        if out:
            print(self)
        self.sqr_n(iterates)

    def __str__(self):
        if self.lowerOne:
            if self.savedOne:
                if self.number > 0.0000000001:
                    return str(1-self.number)
                else:
                    return "1 - " + str(self.number)
            else:
                return str(2 - self.number)
        else:
            if self.savedOne:
                return "1 + " + str(self.number)
            else:
                return str(self.number)

""" num is number to work,
    iterates is number of repeatings for sqrt and sqr
    mc_loren_accuracy is amount of members in mcLoren summary
"""
def main(num, iterates=100, mc_loren_accuracy=10):
    x = Complex(num, mc_loren_accuracy)
    print("sqrt and sqr " + str(iterates) + " times:")
    print(x)
    x.magic_function(iterates, True)
    print(x)

main(0.1, 100, 20)
