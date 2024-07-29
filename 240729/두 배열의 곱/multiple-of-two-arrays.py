temp1 = [list(map(int,input().split())) for _ in range(3)]
input()
temp2 = [list(map(int,input().split())) for _ in range(3)]

temp3 = [[0 for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        mul_val = temp1[i][j] * temp2[i][j]
        temp3[i][j] = mul_val

for row in temp3:
    for elem in row:
        print(elem, end=" ")    
    print()