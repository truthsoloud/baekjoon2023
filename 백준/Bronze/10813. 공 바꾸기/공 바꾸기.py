import sys

n, m = map(int, sys.stdin.readline().split())
arr = [0]*n

for k in range(n):
    arr[k]=k+1

for l in range(m):
    i, j = map(int, sys.stdin.readline().split())
    temp=0
    temp=arr[i-1]
    arr[i-1]=arr[j-1]
    arr[j-1]=temp

for o in range(n):
    print(arr[o], end=' ')