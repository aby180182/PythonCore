from functools import reduce


def summation(num):
    return reduce(lambda a, x: a + x, range(1, num + 1))
