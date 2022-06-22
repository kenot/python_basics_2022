free_days_number = int(input())

total_minutes_for_play_yearly = 30000
minutes_play_in_working_days = 63
minutes_play_in_free_days = 127

days_in_the_year = 365

norm_in_free_days = free_days_number * minutes_play_in_free_days  # 2540
norm_in_working_days = (days_in_the_year - free_days_number) * minutes_play_in_working_days # 21735

total_norm_for_play = norm_in_free_days + norm_in_working_days # 2540 + 21735 = 24275

needed_minutes_for_play = abs(total_minutes_for_play_yearly - total_norm_for_play) # 30000 - 24275 = 5725

needed_hours_for_play = needed_minutes_for_play // 60
needed_minutes_for_play_converted = needed_minutes_for_play % 60

if total_minutes_for_play_yearly <= total_norm_for_play:
    print('Tom will run away')
    print(f'{needed_hours_for_play} hours and {needed_minutes_for_play_converted} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{needed_hours_for_play} hours and {needed_minutes_for_play_converted} minutes less for play')

