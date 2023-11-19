import sys

arr = []
max = 0
maxIndex = 0

for i in range(9):
    arr.append(int(sys.stdin.readline()))
    if arr[i]>max:
        max = arr[i]
        maxIndex = i+1

print(max)
print(maxIndex)