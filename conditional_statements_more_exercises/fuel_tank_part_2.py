fuel_type = str(input())
quantity_fuel = float(input())
club_card = str(input())

gasoline_price = 2.22
gas_price = 0.93
diesel_price = 2.33

gasoline_price_with_club_card = gasoline_price - 0.18
gas_price_with_club_card = gas_price - 0.08
diesel_price_with_club_card = diesel_price - 0.12;

result = 0

if quantity_fuel > 25:
    gasoline_price *= 0.90
    gas_price *= 0.90
    diesel_price *= 0.90

    gasoline_price_with_club_card *= 0.90
    gas_price_with_club_card *= 0.90
    diesel_price_with_club_card *= 0.90
elif quantity_fuel >= 20:
    gasoline_price *= 0.92
    gas_price *= 0.92
    diesel_price *= 0.92

    gasoline_price_with_club_card *= 0.92
    gas_price_with_club_card *= 0.92
    diesel_price_with_club_card *= 0.92

if club_card == "Yes":
    if fuel_type == "Gasoline":
        result = gasoline_price_with_club_card * quantity_fuel
    elif fuel_type == "Gas":
        result = gas_price_with_club_card * quantity_fuel
    elif fuel_type == "Diesel":
        result = diesel_price_with_club_card * quantity_fuel
else:
    if fuel_type == "Gasoline":
        result = gasoline_price * quantity_fuel
    elif fuel_type == "Gas":
        result = gas_price * quantity_fuel
    elif fuel_type == "Diesel":
        result = diesel_price * quantity_fuel

print(f"{result:.2f} lv.")




