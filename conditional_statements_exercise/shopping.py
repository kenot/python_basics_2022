budget = float(input())
video_cards_number = int(input())
processors_number = int(input())
ram_memories_number = int(input())

video_card_price = video_cards_number * 250
processor_price = video_card_price * 0.35
ram_memory_price = video_card_price * 0.10

total_price = video_card_price + (processor_price * processors_number) + (ram_memory_price * ram_memories_number)

if video_cards_number > processors_number:
    total_price *= 0.85

needed_money = abs(budget - total_price)

if budget >= total_price:
    print(f"You have {needed_money:.2f} leva left!")
else:
    print(f"Not enough money! You need {needed_money:.2f} leva more!")
