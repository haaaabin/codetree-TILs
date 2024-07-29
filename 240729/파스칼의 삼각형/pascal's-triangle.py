n = int(input())

temp = [[ 0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    temp[i][0] = 1
    temp[i][i] = 1

for i in range(n):
    for j in range(1, i):
        temp[i][j] = temp[i-1][j-1] + temp[i-1][j]

for i in range(n):
    for j in range(i+1):
        print(temp[i][j], end=" ")
    print()