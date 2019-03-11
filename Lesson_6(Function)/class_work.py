# 1.  Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел.

def arithmetic_mean(a, *args):
    """ function that calculate the arithmetic mean of an arbitrary count of numbers """
    list_of_numbers = [*args]
    return sum(list_of_numbers, a)/(1 + len(list_of_numbers))



# Написати функцію, яка повертає абсолютне значення числа
from math import *

def absolute_number(x):
    """ function that returns the absolute value of the number """
    return abs(x)



# 3. Написати функцію,
# яка знаходить максимальне число з двох чисел, а також в функції використати рядки документації DocStrings.

def max_number(a, b):
    """ function that returns the maximum number of two numbers"""
    return max(a, b)



# 4.  Написати програму, яка обчислює площу прямокутника, трикутника та кола
# (написати три функції для обчислення площі, і викликати їх в головній програмі в залежності від вибору користувача)
from math import pi

def square_rectangle():
    a = float(input("Enter first side of rectangle: "))
    b = float(input("Enter second side of rectangle: "))
    print("Square of rectangle", a * b)


def square_triangle():
    a = float(input("Enter side of triangle: "))
    h = float(input("Enter height of triangle: "))
    print("Square of triangle", a / 2 * h )


def square_circle():
    r = float(input("Enter radius of circle: "))
    print("Square of circle {0:.4f}".format(pi * (r**2)))


def main():
    choise = input("1 - square_rectangle\n2 - square_triangle\n3 - square_circle\n")
    if choise == '1':
        square_rectangle()
    elif choise == '2':
        square_triangle()
    elif choise == '3':
        square_circle()


if __name__ == "__main__":
    main()


from functools import reduce
# 5.  Написати функцію, яка обчислює суму цифр введеного числа.

def sum_of_numbers(list_of_numbers):
    """ function that calculates the sum of the entered numbers. """
    return reduce(lambda c, x: c + x, list_of_numbers)

# 6.  Написати програму калькулятор, яка складається з наступних функцій:

# головної, яка пропонує вибрати дію та додаткових, які реалізовують вибрані дії,
# калькулятор працює доти, поки ми не виберемо дію вийти з калькулятора,
#  після виходу, користувач отримує повідомлення з подякою за вибір нашого програмного продукту!!!

sum = lambda a, b: a + b
difference = lambda a, b: a - b
product = lambda a, b: a * b
division = lambda a, b: a / b

def main():
    while True:
        a = float(input("First number: \n"))
        b = float(input("Second number: \n"))
        choise = input("Do your choise:\n1 - sum\n2 - difference\n3 - product\n4 - division\n0 - exit\n")
        if choise == '1':
            print(sum(a, b))
        elif choise == '2':
            print(difference(a, b))
        elif choise == '3':
            print(product(a, b))
        elif choise == '4':
            print(division(a, b))
        elif choise == '0':
            print("Thank you for choosing our software\n")
            break
        else: continue

if __name__ == "__main__":
    main()


# 7.  Побудувати рекурсивну функцію обчислення чисел Фібоначі до числа введеного користувачем.


# 8.  Написати програму, яка обчислює дискримінант квадратного рівняння

def discriminant_of_quadratic_equation ():
    print("Quadratic equation: a(x**2) + bx + c")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    discriminant = b ** 2 - 4 * a * c
    print("Discriminant of quadratic equation is ", discriminant)
