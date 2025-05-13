# Створіть абстрактний клас Shape, який містить метод calculate_area().
# Створіть кілька дочірніх класів, таких як Rectangle, Circle, і Triangle, які будуть реалізовувати метод calculate_area() по-своєму.
# Напишіть функцію, яка приймає список об'єктів типу Shape і викликає метод calculate_area() для кожного з них.

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.widht = width
        self.height = height

    def calculate_area(self):
        return self.widht * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


def print_area(shapes:list[Shape]):
    for shape in shapes:
        print(f"{shape.__class__.__name__} erea: {shape.calculate_area():.2f}см")


shapes = [
    Rectangle(5, 10),
    Circle(7),
    Triangle(6, 4)
]

print_area(shapes)