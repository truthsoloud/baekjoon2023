import sys

n = int(sys.stdin.readline())

for i in range(n):
    for k in range(n-i-1):
        print(' ', end='')
    for j in range(i+1):
        print('*', end='')
    print('\n',end='')