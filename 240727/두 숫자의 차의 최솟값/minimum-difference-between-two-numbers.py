n = int(input())
arr = list(map(int,input().split()))

min_val = 100

for i in range(n):
    for j in range(i+1,n):
        sub = -1 * (arr[i] - arr[j])
        if sub < min_val:
            min_val = sub

print(min_val)