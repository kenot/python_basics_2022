letter = input()

c_is_appeared = False
o_is_appeared = False
n_is_appeared = False

word = ''

while letter != "End":
    first_condition_capital_letters = 65 <= ord(letter) <= 90
    second_condition_small_letters = 97 <= ord(letter) <= 122

    if first_condition_capital_letters or second_condition_small_letters:
        if letter == 'n':
            if n_is_appeared:
                word += letter
            n_is_appeared = True
        elif letter == 'c':
            if c_is_appeared:
                word += letter
            c_is_appeared = True
        elif letter == 'o':
            if o_is_appeared:
                word += letter
            o_is_appeared = True
        else:
            word += letter

        if n_is_appeared and c_is_appeared and o_is_appeared:
            print(word, end=' ')
            word = ''

            c_is_appeared = False
            n_is_appeared = False
            o_is_appeared = False
    letter = input()
