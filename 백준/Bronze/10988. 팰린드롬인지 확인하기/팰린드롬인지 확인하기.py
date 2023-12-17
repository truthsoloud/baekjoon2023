words = str(input())
wordlist = list(words)
n = len(wordlist)
cnt = 0
for i in range(n//2):
    if wordlist[i] != wordlist[n-1-i]:
        break
    else:
        cnt+=1

if cnt == n//2:
    print(1)
else:
    print(0)
