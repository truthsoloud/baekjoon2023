time = int(input())

for i in range(time):
    howmany, word = map(str, input().split())
    for j in range(len(word)):
        for k in range(int(howmany)):
            print(word[j], end='')
    print('')