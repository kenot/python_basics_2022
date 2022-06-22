from math import floor, ceil

magnolia_quantity = int(input())
zumbul_quantity = int(input())
rose_quantity = int(input())
cactus_quantity = int(input())
price_of_gift = float(input())

magnolia_price = 3.25 * magnolia_quantity
zumbul_price = 4 * zumbul_quantity
rose_price = 3.50 * rose_quantity
cactus_price = 8 * cactus_quantity

profit = magnolia_price + zumbul_price + rose_price + cactus_price

profit_after_tax = profit - (profit * 0.05)

leftover = abs(price_of_gift - profit_after_tax)

if price_of_gift > profit_after_tax:
    print(f"She will have to borrow {ceil(leftover)} leva.")
else:
    print(f"She is left with {floor(leftover)} leva.")




