number = input()

digits = list(map(int, number))

max_digit = max(digits)
digits.remove(max_digit)
min_digit = min(digits)
digits.remove(min_digit)
mid_digit = digits[0]

min_number = ''
max_number = ''
min_used = [False, False, False]
max_used = [False, False, False]

if min_digit != 0 and not min_used[0]:
    min_number += str(min_digit)
    min_used[0] = True
elif mid_digit != 0 and not min_used[1]:
    min_number += str(mid_digit)
    min_used[1] = True
elif max_digit != 0 and not min_used[2]:
    min_number += str(max_digit)
    min_used[2] = True

if not min_used[0]:
    min_number += str(min_digit)
    min_used[0] = True
elif not min_used[1]:
    min_number += str(mid_digit)
    min_used[1] = True
elif not min_used[2]:
    min_number += str(max_digit)
    min_used[2] = True

max_number += str(max_digit) + str(mid_digit)

print(f'{min_number} {max_number}')