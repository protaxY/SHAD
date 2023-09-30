from math import sqrt

a, b, c = float(input()), float(input()), float(input())

if a == 0.0 and b == 0.0 and c == 0.0:
    print('Infinite solutions')
elif a == 0.0 and b == 0.0 and c != 0.0:
    print('No solution')
elif a == 0.0:
    result = -c / b
    print(f'{result:.2f}')
else:
    d = b ** 2 - 4 * a * c
    if d < 0.0:
        print('No solution')
    elif d == 0.0:
        result = -b / (2 * a)
        print(f'{result:.2f}')
    else:
        result1 = (-b + sqrt(d)) / (2 * a)
        result2 = (-b - sqrt(d)) / (2 * a)

        if result1 <= result2:
            print(f'{result1:.2f} {result2:.2f}')
        else:
            print(f'{result2:.2f} {result1:.2f}')