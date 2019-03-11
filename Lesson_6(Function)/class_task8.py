# 8.  Написати програму, яка обчислює дискримінант квадратного рівняння

def discriminant_of_quadratic_equation ():
    print("Quadratic equation: a(x**2) + bx + c")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    discriminant = b ** 2 - 4 * a * c
    print("Discriminant of quadratic equation is ", discriminant)
