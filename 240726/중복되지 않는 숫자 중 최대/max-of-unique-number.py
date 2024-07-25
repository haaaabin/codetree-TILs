n = int(input())
arr = list(map(int,input().split()))

max_num = -1
for elem in arr:
    cnt = arr.count(elem)
    if cnt < 2:
        max_num = elem

print(max_num)