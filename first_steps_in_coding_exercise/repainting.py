nylon_quantity = int(input())
paint_quantity = int(input())
thinner_quantity = int(input())
hours_of_work = int(input())

nylon_price = (nylon_quantity + 2) * 1.50
paint_price = (paint_quantity + (paint_quantity * 10 / 100)) * 14.50
thinner_price = thinner_quantity * 5
bags_price = 0.40

materials_price = nylon_price + paint_price + thinner_price + bags_price

labours_price = hours_of_work * (materials_price * 30 / 100)

total_expenses = materials_price + labours_price

print(total_expenses)
