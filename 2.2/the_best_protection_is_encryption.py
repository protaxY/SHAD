password = input()

a = int(password[1]) + int(password[2])
b = int(password[0]) + int(password[1])

if a >= b:
    print(f'{str(a)}{str(b)}')
else:
    print(f'{str(b)}{str(a)}')