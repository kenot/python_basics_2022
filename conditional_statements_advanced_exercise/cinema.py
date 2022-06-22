type_of_movie = input()
rows_number = int(input())
columns_number = int(input())

total_space = rows_number * columns_number

price = 0

if type_of_movie == "Premiere":
    price = 12.00
elif type_of_movie == "Normal":
    price = 7.50
elif type_of_movie == "Discount":
    price = 5.00

revenue = price * total_space

print(f"{revenue:.2f} leva")

