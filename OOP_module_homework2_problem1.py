from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        return f"This is a {self.__class__.__name__}"

    @staticmethod
    def validate_positive(value, name):
        if value > 0:
            return True
        print(f"{name} must be positive!")
        return False


class Circle(Shape):
    def __init__(self, radius):
        if not self.validate_positive(radius, "radius"):
            raise ValueError("Invalid radius")
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        if not (self.validate_positive(width, "width") and self.validate_positive(height, "height")):
            raise ValueError("Invalid dimensions")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        for idx, side in enumerate([side1, side2, side3], start=1):
            if not self.validate_positive(side, f"side{idx}"):
                raise ValueError("Invalid side")
        self.side1, self.side2, self.side3 = side1, side2, side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


class ShapeCollection:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def total_area(self):
        return sum(shape.area() for shape in self.shapes)

    def total_perimeter(self):
        return sum(shape.perimeter() for shape in self.shapes)


if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4,6)
    triangle = Triangle(3,4,5)

    print("Individual Shapes:")
    for s in [circle, rectangle, triangle]:
        print(f" {s.describe()}")
        print(f" Area: {s.area():.2f}")
        print(f" Perimeter: {s.perimeter():.2f}")

    collection = ShapeCollection()
    collection.add_shape(circle)
    collection.add_shape(rectangle)
    collection.add_shape(triangle)
    print("\nCollection Totals:")
    print(f" Total Area: {collection.total_area():.2f}")
    print(f" Total Perimeter: {collection.total_perimeter():.2f}")

    try:
        bad_circle = Circle(-5)
    except ValueError:
        print("Correctly rejected negative radius")
