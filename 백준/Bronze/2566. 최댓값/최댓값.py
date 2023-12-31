arr = []
for i in range(9):
    arr.append(list(map(int, input().split())))

max = -1
max_x = None
max_y = None

for i in range(9):
    for j in range(9):
        if max < arr[i][j]:
            max = arr[i][j]
            max_x = i+1
            max_y = j+1

print(max)
print(max_x, max_y)