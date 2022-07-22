price_of_luggage_above_20_kgs = float(input())
kgs_of_luggage = float(input())
days_to_trip = int(input())
number_of_luggages = int(input())

luggage_fee = 0

if kgs_of_luggage < 10:
    luggage_fee = price_of_luggage_above_20_kgs * 0.20
elif 10 <= kgs_of_luggage <= 20:
    luggage_fee = price_of_luggage_above_20_kgs * 0.50
elif kgs_of_luggage > 20:
    luggage_fee += price_of_luggage_above_20_kgs

if days_to_trip > 30:
    luggage_fee *= 1.10
elif 7 <= days_to_trip <= 30:
    luggage_fee *= 1.15
elif days_to_trip < 7:
    luggage_fee *= 1.40

total_price_to_pay = luggage_fee * number_of_luggages

print(f'The total price of bags is: {total_price_to_pay:.2f} lv.')