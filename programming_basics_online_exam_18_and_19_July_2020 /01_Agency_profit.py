air_company_agency = input()
tickets_for_adults = int(input())
tickets_for_kids = int(input())
net_price_for_adults = float(input())
price_for_servicing = float(input())

net_price_for_kids = net_price_for_adults * 0.30
price_for_adults_with_servicing = net_price_for_adults + price_for_servicing
price_for_kids_with_servicing = net_price_for_kids + price_for_servicing
total_price_for_all_tickets = (tickets_for_kids * price_for_kids_with_servicing) + (tickets_for_adults * price_for_adults_with_servicing)
profit_of_the_air_company_agency = total_price_for_all_tickets * 0.20

print(f'The profit of your agency from {air_company_agency} tickets is {profit_of_the_air_company_agency:.2f} lv.')