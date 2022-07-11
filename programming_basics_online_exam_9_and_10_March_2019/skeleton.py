minutes = int(input())
seconds = int(input())
length_in_meters = float(input())
seconds_for_100_meters = int(input())

minutes_converted_in_seconds = minutes * 60 + seconds
time_to_be_decreased = length_in_meters / 120
total_decreased_time = time_to_be_decreased * 2.5
marins_time = (length_in_meters / 100) * seconds_for_100_meters - total_decreased_time

difference = abs(marins_time - minutes_converted_in_seconds)

if marins_time <= minutes_converted_in_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {marins_time:.3f}.")
else:
    print(f"No, Marin failed! He was {difference:.3f} second slower.")