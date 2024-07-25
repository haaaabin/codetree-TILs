n = int(input())
arr = list(map(int,input().split()))

min_val = arr[0]

for elem in arr[1:]:
    if elem < min_val:
        min_val = elem

print(f"{min_val} {arr.count(min_val)}")