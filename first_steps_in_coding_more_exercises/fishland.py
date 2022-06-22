price_for_kgs_of_skumriya = float(input())
price_for_kgs_of_tsatsa = float(input())
kgs_of_palamud = float(input())
kgs_of_safrid = float(input())
kgs_of_mussels = int(input())

price_of_palamud = (price_for_kgs_of_skumriya + price_for_kgs_of_skumriya * 0.60) * kgs_of_palamud
price_of_safrid = (price_for_kgs_of_tsatsa + price_for_kgs_of_tsatsa * 0.80) * kgs_of_safrid
price_of_mussels = 7.50 * kgs_of_mussels

total_price = price_of_palamud + price_of_safrid + price_of_mussels

print("{0:.2f}".format(total_price))



