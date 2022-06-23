season = input()
km_per_month = float(input())

gross_salary = 0

if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        gross_salary = (km_per_month * 0.75) * 4
    elif season == "Summer":
        gross_salary = (km_per_month * 0.90) * 4
    elif season == "Winter":
        gross_salary = (km_per_month * 1.05) * 4
elif 5000 < km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        gross_salary = (km_per_month * 0.95) * 4
    elif season == "Summer":
        gross_salary = (km_per_month * 1.10) * 4
    elif season == "Winter":
        gross_salary = (km_per_month * 1.25) * 4
elif 10000 < km_per_month <= 20000:
    gross_salary = (km_per_month * 1.45) * 4

net_salary = gross_salary * 0.90

print(f"{net_salary:.2f}")
