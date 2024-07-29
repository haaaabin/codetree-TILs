n , m = map(int,input().split())
temp1 = [list(map(int,input().split())) for _ in range(n)]
temp2 = [list(map(int,input().split())) for _ in range(n)]
temp3 = [[1 if temp1[i][j] != temp2[i][j] else 0 for j in range(m)] for i in range(n)]

for row in temp3:
    for elem in row:
        print(elem, end=" ")
    print()