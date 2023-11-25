import sys
from math import ceil

n, m = map(int, sys.stdin.readline().split())
arr = [0] * n

for a in range(n):
    arr[a] = a+1

for b in range(m):
    i, j = map(int, sys.stdin.readline().split())

    for c in range(ceil((j - i) / 2)):
        arr[i-1+c], arr[j-1-c] = arr[j-1-c], arr[i-1+c]

for d in range(n):
    print(arr[d], end=' ')