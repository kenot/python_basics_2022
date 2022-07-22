pocket_money = float(input())
money_per_day_won = float(input())
expenses_for_the_whole_period = float(input())
price_of_gift = float(input())

days_left_to_birthday = 5

saved_money_from_pocket_money = days_left_to_birthday * pocket_money
won_money = days_left_to_birthday * money_per_day_won
total_saved_money = saved_money_from_pocket_money + won_money
total_leftover = total_saved_money - expenses_for_the_whole_period

difference = abs(total_leftover - price_of_gift)

if total_leftover > price_of_gift:
    print(f'Profit: {total_leftover:.2f} BGN, the gift has been purchased.')
elif total_leftover < price_of_gift:
    print(f'Insufficient money: {difference:.2f} BGN.')