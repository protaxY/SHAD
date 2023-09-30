from math import sqrt

x, y = float(input()), float(input())

if x ** 2 + y ** 2 > 10 ** 2:
    print('Вы вышли в море и рискуете быть съеденным акулой!')
else:
    is_above = False
    is_below = False

    if -7 < x < 5:
        if y > 0.25 * (x + 1) ** 2 - 9:
            is_above = True
        if -7 < x < -4 and y < (5 / 3) * x + 7 * (5 / 3):
            is_below = True
        if -4 < x < 0 and y < 5:
            is_below = True
        if 0 < x < 5 and y < sqrt(5 ** 2 - x ** 2):
            is_below = True

    if is_above and is_below:
        print('Опасность! Покиньте зону как можно скорее!')
    else:
        print('Зона безопасна. Продолжайте работу.')
