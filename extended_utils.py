from .utils import get_area, get_area_of_circle

def get_volume(height, width, depth):
    if depth < 0:
        raise ValueError("Depth must be greater than 0")
    return  get_area(height, width) * depth

def get_surface_area_of_cuboid(height, width, depth):
    return 2 * (get_area(height, width) + get_area(width, depth) + get_area(height, depth))

def get_surface_area_of_sphere(radius):
    return 4 * get_area_of_circle(radius)