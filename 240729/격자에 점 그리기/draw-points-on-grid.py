n, m = map(int,input().split())
temp = [[0 for _ in range(n)] for _ in range(n)]

num = 1
for i in range(m):
    r,c = map(int,input().split())
    temp[r-1][c-1] = num
    num += 1

for row in temp:
    for col in row:
        print(col, end=" ")
    print()