def compute_area_square(side_length):
    """Compute the area of a square given the length of its side."""
    return compute_area_rectangle(side_length, side_length)

def compute_area_rectangle(length, width):
    """Compute the area of a rectangle given its length and width."""
    return length * width

def compute_are_circle(radius):
    """Compute the area of a circle given its radius."""
    import math
    return math.pi * (radius ** 2)

while True:
    print("What kind of shape do you want to compute the area for?")
    shape = input("Enter 'square', 'rectangle', or 'circle' (or 'quit' to exit): ").strip().lower()
    if shape == 'quit':
        break
    elif shape == 'square':
        side = float(input("Enter the length of the side of the square: "))
        area = compute_area_square(side)
        print(f"The area of the square is: {area}")
    elif shape == 'rectangle':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = compute_area_rectangle(length, width)
        print(f"The area of the rectangle is: {area}")
    elif shape == 'circle':
        radius = float(input("Enter the radius of the circle: "))
        area = compute_are_circle(radius)
        print(f"The area of the circle is: {area}")
    else:
        print("Invalid shape. Please try again.")