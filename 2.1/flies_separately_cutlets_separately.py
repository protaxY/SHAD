n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())

print(f'{(m * n - k2 * n) // (k1 - k2)} {(k1 * n - m * n) // (k1 - k2)}')