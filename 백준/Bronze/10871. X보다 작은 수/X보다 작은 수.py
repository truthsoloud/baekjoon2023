import sys

n, x = map(int, sys.stdin.readline().split())

array = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    if array[i]<x:
        print(array[i], end=' ')