temperature = float(input())

if (temperature >= 5) and (temperature <= 11.9):
    print("Cold")
elif (temperature >= 12.0) and (temperature <= 14.9):
    print("Cool")
elif (temperature >= 15.00) and (temperature <= 20.00):
    print("Mild")
elif (temperature >= 20.1) and (temperature <= 25.9):
    print("Warm")
elif (temperature >= 26.00) and (temperature <= 35.00):
    print("Hot")
else:
    print("unknown")

