eggs_sizes = input()
eggs_color = input()
number_of_batches = int(input())

eggs_price = 0

if eggs_sizes == "Large":
    if eggs_color == "Red":
        eggs_price = 16
    elif eggs_color == "Green":
        eggs_price = 12
    elif eggs_color == "Yellow":
        eggs_price = 9
if eggs_sizes == "Medium":
    if eggs_color == "Red":
        eggs_price = 13
    elif eggs_color == "Green":
        eggs_price = 9
    elif eggs_color == "Yellow":
        eggs_price = 7
if eggs_sizes == "Small":
    if eggs_color == "Red":
        eggs_price = 9
    elif eggs_color == "Green":
        eggs_price = 8
    elif eggs_color == "Yellow":
        eggs_price = 5

price_of_eggs_batches = number_of_batches * eggs_price
expenses = price_of_eggs_batches * 0.35
amount_due_after_expenses = price_of_eggs_batches - expenses

print(f'{amount_due_after_expenses:.2f} leva.')