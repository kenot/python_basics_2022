from math import floor, ceil

episode = input()
episode_time = int(input())
break_time = int(input())

lunch_time = break_time * 0.125
relax_time = break_time * 0.25

time_left = break_time - lunch_time - relax_time
needed_time = 0
if time_left >= episode_time:
    needed_time = abs(time_left - episode_time)
    print(f"You have enough time to watch {episode} and left with {ceil(needed_time)} minutes free time.")
else:
    needed_time = abs(time_left - episode_time)
    print(f"You don't have enough time to watch {episode}, you need {ceil(needed_time)} more minutes.")

