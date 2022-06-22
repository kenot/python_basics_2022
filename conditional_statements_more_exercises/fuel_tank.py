# fuel = input()
# liters_of_fuel = float(input())
#
# if liters_of_fuel >= 25:
#     if fuel == 'Diesel' or fuel == 'Gas' or fuel == 'Gasoline':
#         print(f"You have enough {fuel}.")
#     else:
#         print("Invalid fuel!")
# else:
#     if fuel == 'Diesel' or fuel == 'Gas' or fuel == 'Gasoline':
#         print(f"Fill your tank with {fuel}!")
#     else:
#         print("Invalid fuel!")

fuel = str(input())
liters_of_fuel = float(input())

if (fuel == "Diesel") or (fuel == "Gas") or (fuel == "Gasoline"):
    if liters_of_fuel >= 25:
        print(f"You have enough {fuel.lower()}.")
    elif liters_of_fuel < 25:
        print(f"Fill your tank with {fuel.lower()}!")
else:
    print("Invalid fuel!")

