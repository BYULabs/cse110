# This program calculates the area of a square, rectangle, and circle based on user input.

import math

# Square: ask in centimeters, compute cm^2 and m^2
side_length_cm = float(input("What is the length of a side of the square (in centimeters)? "))
square_area_cm2 = side_length_cm ** 2
square_area_m2 = square_area_cm2 / 10000  # 1 cm^2 = 1/10000 m^2
print(f"The area of the square is: {square_area_cm2:.1f} cm^2 ({square_area_m2:.4f} m^2)")

# Rectangle: ask in centimeters, compute cm^2 and m^2
rectangle_length_cm = float(input("What is the length of the rectangle (in centimeters)? "))
rectangle_width_cm = float(input("What is the width of the rectangle (in centimeters)? "))
rectangle_area_cm2 = rectangle_length_cm * rectangle_width_cm
rectangle_area_m2 = rectangle_area_cm2 / 10000
print(f"The area of the rectangle is: {rectangle_area_cm2:.1f} cm^2 ({rectangle_area_m2:.4f} m^2)")

# Circle: ask in centimeters, compute cm^2 and m^2
circle_radius_cm = float(input("What is the radius of the circle (in centimeters)? "))
circle_area_cm2 = math.pi * circle_radius_cm ** 2
circle_area_m2 = circle_area_cm2 / 10000
print(f"The area of the circle is: {circle_area_cm2:.1f} cm^2 ({circle_area_m2:.4f} m^2)")