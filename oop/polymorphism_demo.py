import math

class Shape:
    """Base class representing a generic shape."""
    def area(self):
        """Calculate the area of the shape."""
        raise NotImplementedError("Subclasses must implement this method.")


class Rectangle(Shape):
    """Rectangle shape class inheriting from Shape."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Return the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Circle shape class inheriting from Shape."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * (self.radius ** 2)


if __name__ == "__main__":
    # Example test to verify functionality
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")
