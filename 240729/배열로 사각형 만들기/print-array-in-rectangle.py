temp = [[1 for _ in range(5)] for _ in range(5)]

for i in range(1,5):
    for j in range(1,5):
        temp[i][j] = temp[i-1][j] + temp[i][j-1]

for row in temp:
    for col in row:
        print(col, end= " ")
    print()