n, m = map(int,input().split())

temp = [[0 for _ in range(m)] for _ in range(n)]

num = 1
for i in range(n):
    for j in range(m):
        temp[i][j] = num
        num +=1

for elem in temp:
    for row in elem:
        print(row, end=" ")
    print()