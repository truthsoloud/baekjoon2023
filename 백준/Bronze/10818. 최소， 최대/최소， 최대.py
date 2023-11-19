import sys

n = sys.stdin.readline()

array = list(map(int, sys.stdin.readline().split()))

print(min(array), end=' ')
print(max(array))