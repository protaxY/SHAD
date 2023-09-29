number1 = input()
number2 = input()

number1 = number1.zfill(3)
number2 = number2.zfill(3)

result = ''

for i in range(3):
    result += str((int(number1[i]) + int(number2[i])) % 10)

print(int(result))