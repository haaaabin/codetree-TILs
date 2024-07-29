n , m = map(int,input().split())
temp1 = [list(map(int,input().split())) for _ in range(m)]
temp2 = [list(map(int,input().split())) for _ in range(m)]
temp3 = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if temp1[i][j] == temp2[i][j]:
            temp3[i][j] = 0
        else:
            temp3[i][j] = 1

for row in temp3:
    for elem in row:
        print(elem, end=" ")
    print()