import string

s=str(input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(alphabet)):
    print(s.find(alphabet[i]), end=' ')