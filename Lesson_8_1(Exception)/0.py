# Створити батьківський клас Figure з методами init:
# ініціалізується колір, get_color: повертає колір фігури,
#  info: надає інформацію про фігуру та колір,
# від якого наслідуються такі класи як Rectangle, Square, які мають інформацію про ширину,
# висоту фігури, метод square, який знаходить площу фігури.


class Figure:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def info(self):
        return f'color: {self.color}'


class Rectangle(Figure):
    def __init__(self, color, width, height):
        Figure.__init__(self, color)
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height


class Square(Figure):
    def __init__(self, color, side):
        Figure.__init__(self, color)
        self.side = side

    def square(self):
        return self.side * self.side

figure = Figure('red')
print(figure.get_color())
print(figure.info())

rectangle = Rectangle('green', 3, 4)
print(rectangle.square())

sq = Square('blue', 9)
print(sq.square())