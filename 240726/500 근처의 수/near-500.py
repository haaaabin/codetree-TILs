arr = list(map(int,input().split()))
min_val = 1000
max_val = 1

for i in arr:
    if i < 500 and i > max_val:
        max_val = i
    if i > 500 and i < min_val:
        min_val = i

print(max_val, min_val)