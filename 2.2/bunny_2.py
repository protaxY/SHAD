string0, string1, string2 = input(), input(), input()

zaika_strings = []

if 'зайка' in string0:
    zaika_strings.append(string0)
if 'зайка' in string1:
    zaika_strings.append(string1)
if 'зайка' in string2:
    zaika_strings.append(string2)

result = min(zaika_strings)

print(result, len(result))

