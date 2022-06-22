annual_tax = int(input())

sneakers_price = annual_tax - (annual_tax * 40 / 100) # annual_tax * 0.6
dress_price = sneakers_price - (sneakers_price * 20 / 100) # sneakers_price * 0.8
ball_price = dress_price / 4
accessories_price = ball_price / 5 # ball_price * 1 / 5
total_needed_sum = annual_tax + sneakers_price + dress_price + ball_price + accessories_price

print(total_needed_sum)