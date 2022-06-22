x_height_of_house = float(input())
y_length_of_side_wall = float(input())
h_height_of_triangle_wall_of_roof = float(input())

# Calculations for the walls
area_of_side_walls = (x_height_of_house * y_length_of_side_wall) * 2
area_of_side_windows = (1.5 * 1.5) * 2
total_area_of_sides = area_of_side_walls - area_of_side_windows

area_of_front_and_back_walls = (x_height_of_house * x_height_of_house) * 2
area_of_front_door = 1.2 * 2
total_area_of_front_and_back_walls = area_of_front_and_back_walls - area_of_front_door

walls_area_for_green_painting = (total_area_of_sides + total_area_of_front_and_back_walls) / 3.4

# Calculations for the roof
area_of_roof_rectangles = (x_height_of_house * y_length_of_side_wall) * 2
area_of_roof_triangles = ((x_height_of_house * h_height_of_triangle_wall_of_roof) * 2) / 2
total_area_of_roof = area_of_roof_rectangles + area_of_roof_triangles

roof_area_for_red_painting = total_area_of_roof / 4.3

print("{0:.2f}".format(walls_area_for_green_painting))
print("{0:.2f}".format(roof_area_for_red_painting))




