foundPiece = list(map(int, input().split()))
originalPiece = [1, 1, 2, 2, 2, 8]

for i in range(len(foundPiece)):
    print(originalPiece[i] - foundPiece[i], end=' ')