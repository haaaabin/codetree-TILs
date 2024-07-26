n = int(input())
arr = list(map(int,input().split()))

min_val = arr[1]-arr[0]

for i in range(2,n):
    sub = arr[i] - arr[i-1]
    if sub < min_val:
        min_val = sub

print(min_val)