number_of_cargos = int(input())

microbus = 0
truck = 0
train = 0
tons = 0
average_price = 0

for current_cargo in range(number_of_cargos):
    tonnage = int(input())
    if tonnage <= 3:
        microbus += tonnage
        tons += tonnage
    elif 4 <= tonnage <= 11:
        truck += tonnage
        tons += tonnage
    elif tonnage >= 12:
        train += tonnage
        tons += tonnage

average_price = (microbus * 200 + truck * 175 + train * 120) / tons
percentage_microbus = (microbus / tons) * 100
percentage_truck = (truck / tons) * 100
percentage_train = (train / tons) * 100

print(f'{average_price:.2f}')
print(f'{percentage_microbus:.2f}%')
print(f'{percentage_truck:.2f}%')
print(f'{percentage_train:.2f}%')
