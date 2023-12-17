remainderlist = [None] * 42
cnt = 0
for i in range(10):
    newNum = int(input())
    remainder = newNum % 42
    if remainder not in remainderlist:
        remainderlist[i] = remainder
        cnt += 1
print(cnt)