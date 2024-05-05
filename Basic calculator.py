from functools import reduce


class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        return reduce(lambda x, y: x * y, args)

    @staticmethod
    def divide(*args):
        return reduce(lambda x, y: x / y, args)

    @staticmethod
    def sbtackt(*args):
        return reduce(lambda x, y: x - y, args)


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.sbtackt(90, 20, -50, 43, 7))
