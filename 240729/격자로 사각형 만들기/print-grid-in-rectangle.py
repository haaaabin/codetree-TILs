n = int(input())

temp = [[1 for _ in range(n)] for _ in range(n)]

for i in range(1,n):
    for j in range(1, n):
        temp[i][j] = temp[i-1][j] + temp[i][j-1] + temp[i-1][j-1]

for row in temp:
    for col in row:
        print(col, end=" ")
    print()