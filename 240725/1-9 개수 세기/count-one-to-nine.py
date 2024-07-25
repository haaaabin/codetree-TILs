n = int(input())
num = list(map(int,input().split()))
temp = [ 0 for _ in range(10) ]

for elem in num:
    temp[elem] += 1

for i in range(1,10):
    print(temp[i])