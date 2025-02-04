import math

def get_area(height, width):
    if height < 0:
        raise ValueError("Height must be greater than 0")
    if width < 0:
        raise ValueError("Width must be greater than 0")
    return (height * width)

def get_perimeter(height, width):
    return 2 * (height + width)

def get_area_of_circle(radius):
    return math.pi * radius ** 2