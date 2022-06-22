from math import pi

figure = input()
area = 0

if figure == "square":
    length_of_square_side = float(input())
    area = length_of_square_side ** 2
    print(f"{area:.3f}")
if figure == "rectangle":
    width_of_rectangle = float(input())
    length_of_rectangle = float(input())
    area = width_of_rectangle * length_of_rectangle
    print(f"{area:.3f}")
if figure == "circle":
    radius_of_circle = float(input())
    area = pi * radius_of_circle ** 2
    print(f"{area:.3f}")
if figure == "triangle":
    height_of_triangle = float(input())
    base_of_triangle = float(input())
    area = (height_of_triangle * base_of_triangle) / 2
    print(f"{area:.3f}")

