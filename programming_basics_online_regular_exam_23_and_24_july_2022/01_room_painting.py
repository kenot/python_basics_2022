from math import ceil, floor

boxes_with_paint = int(input())
rolls_of_wallpaper = int(input())
price_of_one_set_of_gloves = float(input())
price_of_one_brush = float(input())

price_of_paint = boxes_with_paint * 21.50
price_of_wallpaper = rolls_of_wallpaper * 5.20
needed_gloves = rolls_of_wallpaper * 0.35
needed_brush = boxes_with_paint * 0.48
price_of_gloves = ceil(needed_gloves) * price_of_one_set_of_gloves
price_of_brush = floor(needed_brush) * price_of_one_brush

total_cost_of_products = price_of_paint + price_of_wallpaper + price_of_gloves + price_of_brush
total_cosf_of_delivery = total_cost_of_products / 15

print(f'This delivery will cost {total_cosf_of_delivery:.2f} lv.')
