stage_of_the_championship = input()
ticket_type = input()
tickets_number = int(input())
photo_with_trophy = input()

price_of_ticket = 0
total_price = 0
price_for_one_picture = 40
total_price_trophy = 0

if stage_of_the_championship == "Quarter final":
    if ticket_type == "Standard":
        price_of_ticket = 55.50
    elif ticket_type == "Premium":
        price_of_ticket = 105.20
    elif ticket_type == "VIP":
        price_of_ticket = 118.90
if stage_of_the_championship == "Semi final":
    if ticket_type == "Standard":
        price_of_ticket = 75.88
    elif ticket_type == "Premium":
        price_of_ticket = 125.22
    elif ticket_type == "VIP":
        price_of_ticket = 300.40
if stage_of_the_championship == "Final":
    if ticket_type == "Standard":
        price_of_ticket = 110.10
    elif ticket_type == "Premium":
        price_of_ticket = 160.66
    elif ticket_type == "VIP":
        price_of_ticket = 400

total_price = price_of_ticket * tickets_number

if total_price > 4000:
    total_price *= 0.75
elif total_price > 2500:
    total_price *= 0.90

if photo_with_trophy == "N":
    total_price_trophy = 0
elif photo_with_trophy == "Y":
    total_price_trophy = tickets_number * price_for_one_picture
    total_price += total_price_trophy
elif photo_with_trophy == "Y" and total_price > 4000:
    total_price_trophy = 0


#print(f'{total_price_trophy}')
print(f'{total_price:.2f}')

