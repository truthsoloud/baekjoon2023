a = int(input())
b = int(input())

third = a * (b % 10)
fourth = a * (b // 10 % 10)
fifth = a * (b // 100 % 10)
sixth = fifth*100 + fourth*10 + third

print(third)
print(fourth)
print(fifth)
print(sixth)