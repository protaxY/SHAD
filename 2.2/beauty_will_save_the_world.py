number = input()

digits = [*number]

max_digit_index = digits.index(max(digits, key=lambda x: int(x)))
min_digit_index = digits.index(min(digits, key=lambda x: int(x)))

for index in range(3):
    if max_digit_index != index and min_digit_index != index:
        mid_digit_index = index

if 2 * int(digits[mid_digit_index]) == int(digits[min_digit_index]) + int(digits[max_digit_index]):
    print('YES')
else:
    print('NO')
