a, b = map(str, input().split())

reversed_a = a[::-1]
reversed_b = b[::-1]

if int(reversed_a) > int(reversed_b):
    print(reversed_a)
else:
    print(reversed_b)