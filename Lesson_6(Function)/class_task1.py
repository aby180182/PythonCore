# 1.  Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел.

def arithmetic_mean(a, *args):
    """ function that calculate the arithmetic mean of an arbitrary count of numbers """
    list_of_numbers = [*args]
    return sum(list_of_numbers, a)/(1 + len(list_of_numbers))

