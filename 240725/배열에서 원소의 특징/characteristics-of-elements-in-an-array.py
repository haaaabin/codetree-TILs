arr = list(map(int,input().split()))
k = 0
for i in arr:
    if i % 3 == 0:
        k == i
        break

print(arr[k+1])