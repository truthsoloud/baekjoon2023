arr = []

for i in range(9):
    inner_arr = list(map(int, input().split()))
    arr.append(inner_arr)

max = -1
where_x = where_y = 0

for i in range(9):
    for j in range(9):
        if arr[i][j] > max:
            max = arr[i][j]
            where_x = i+1
            where_y = j+1

print(max)
print(where_x, where_y)