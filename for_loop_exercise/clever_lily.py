years_of_age = int(input())
price_of_laundry_machine = float(input())
price_of_toy = int(input())

total_money = 0
birthday_money = 0
toy_quantity = 0

for years in range(1 , years_of_age + 1):
    if years % 2 == 0:
        birthday_money += 10
        total_money += birthday_money
        total_money -= 1
    else:
        toy_quantity += 1

profit_from_toys = price_of_toy * toy_quantity
saved_money = total_money + profit_from_toys

leftover = abs(saved_money - price_of_laundry_machine)

if saved_money >= price_of_laundry_machine:
    print(f"Yes! {leftover:.2f}")
else:
    print(f"No! {leftover:.2f}")