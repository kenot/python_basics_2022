n1_number = int(input())
n2_number = int(input())
symbol = input()

result = 0

if symbol == "+" or symbol == "-" or symbol == "*":
    if symbol == "+":
        result = n1_number + n2_number
    elif symbol == "-":
        result = n1_number - n2_number
    elif symbol == "*":
        result = n1_number * n2_number

    if result % 2 == 0:
        print(f'{n1_number} {symbol} {n2_number} = {result} - even')
    else:
        print(f'{n1_number} {symbol} {n2_number} = {result} - odd')
elif symbol == "/":
    if n2_number == 0:
        print(f"Cannot divide {n1_number} by zero")
    else:
        result = n1_number / n2_number
        print(f"{n1_number} {symbol} {n2_number} = {result:.2f}")
elif symbol == "%":
    if n2_number == 0:
        print(f"Cannot divide {n1_number} by zero")
    else:
        result = n1_number % n2_number
        print(f"{n1_number} {symbol} {n2_number} = {result}")


