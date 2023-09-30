n = int(input())
m = int(input())

petya = 7
vasya = 6
# tolya = x
# gena = y
# dima = z


vasya += 3
petya -= 3
# tolya -= 2
# tolya -= 2
# gena += 2
petya += n
# dima -= n
vasya += m
# dima -= m

if vasya > petya:
    print('Вася')
elif petya > vasya:
    print("Петя")