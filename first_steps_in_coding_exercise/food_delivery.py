chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())

chicken_menu_price = chicken_menu * 10.35
fish_menu_price = fish_menu * 12.40
vegetarian_menu_price = vegetarian_menu * 8.15
menus_price = chicken_menu_price + fish_menu_price + vegetarian_menu_price
desert_price = menus_price * 20 / 100
delivery_price = 2.50

total_price_of_the_order = menus_price + desert_price + delivery_price

print(total_price_of_the_order)