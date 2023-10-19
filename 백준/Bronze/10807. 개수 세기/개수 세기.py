import sys

n = int(sys.stdin.readline())

array = list(map(int, input().split()))

v = int(sys.stdin.readline())

count=0
for j in range(n):
    if array[j]==v:
        count+=1

print(count)