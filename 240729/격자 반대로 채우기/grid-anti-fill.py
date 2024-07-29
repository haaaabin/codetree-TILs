n = int(input())
temp = [[0 for _ in range(n)] for _ in range(n)]

num = 1
for i in range(n-1, -1 , -1):
    if i % 2 != 0:
        for j in range(n-1, -1, -1):
            temp[j][i]= num
            num += 1
    else:
        for j in range(n):
            temp[j][i] = num
            num +=1
            
for row in temp:
    for col in row:
        print(col, end = " ")
    print()