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
