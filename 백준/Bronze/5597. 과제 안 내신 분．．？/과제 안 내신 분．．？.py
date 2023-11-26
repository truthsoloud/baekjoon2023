import sys

arr = [0] * 30

for i in range(28):
    a = int(sys.stdin.readline())
    arr[a-1] = a

for j in range(30):
    if arr[j] == 0:
        print(j+1)