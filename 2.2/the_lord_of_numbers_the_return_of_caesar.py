number1 = input()
number2 = input()

digits = list(map(int, number1 + number2))

unused_indexes = list(range(4))

first_digit_index = digits.index(max(digits))
unused_indexes.remove(first_digit_index)
last_digit_index = digits.index(min(digits))
unused_indexes.remove(last_digit_index)

mid_digit = (digits[unused_indexes[0]] + digits[unused_indexes[1]]) % 10

print(f'{max(digits)}{mid_digit}{min(digits)}')