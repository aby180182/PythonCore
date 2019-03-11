from functools import reduce
# 5.  Написати функцію, яка обчислює суму цифр введеного числа.

def sum_of_numbers(list_of_numbers):
    """ function that calculates the sum of the entered numbers. """
    return reduce(lambda c, x: c + x, list_of_numbers)