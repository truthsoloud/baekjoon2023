code = list(input())

cnt = 0
for i in range(len(code)):
    if code[i] == "A" or code[i] == "B" or code[i] == "C":
        cnt+=3
    elif code[i] == "D" or code[i] == "E" or code[i] == "F":
        cnt+=4
    elif code[i] == "G" or code[i] == "H" or code[i] == "I":
        cnt+=5
    elif code[i] == "J" or code[i] == "K" or code[i] == "L":
        cnt += 6
    elif code[i] == "M" or code[i] == "N" or code[i] == "O":
        cnt += 7
    elif code[i] == "P" or code[i] == "Q" or code[i] == "R" or code[i] == "S":
        cnt += 8
    elif code[i] == "T" or code[i] == "U" or code[i] == "V":
        cnt += 9
    elif code[i] == "W" or code[i] == "X" or code[i] == "Y" or code[i] == "Z":
        cnt += 10
print(cnt)