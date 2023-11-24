import sys

n, m = map(int, sys.stdin.readline().split())
arr = [0] * n

for a in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    for b in range(j-i+1):
        arr[i-1] = k
        i+=1

for c in range(n):
    print(arr[c], end=' ')