number_of_months = int(input())

electricity_bill = 0
water_bills = 0
internet_bills = 0
others = 0

for current_month in range(number_of_months):
    electricity = float(input())
    electricity_bill += electricity
    water_bills += 20
    internet_bills += 15
    others += (electricity + 20 + 15) * 1.20

average_bill = (electricity_bill + water_bills + internet_bills + others) / number_of_months

print(f'Electricity: {electricity_bill:.2f} lv')
print(f'Water: {water_bills:.2f} lv')
print(f'Internet: {internet_bills:.2f} lv')
print(f'Other: {others:.2f} lv')
print(f'Average: {average_bill:.2f} lv')
