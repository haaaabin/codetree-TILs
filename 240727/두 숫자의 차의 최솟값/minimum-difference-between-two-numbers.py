n = int(input())
arr = list(map(int,input().split()))

min_val = 100

for i in range(5):
    for j in range(i+1):
        if arr[i] > arr[j] and arr[i] - arr[j] < min_val:
            min_val = arr[i] - arr[j]
        elif arr[i] < arr[j] and arr[j] - arr[i] < min_val:
            min_val = arr[j] - arr[i]

print(min_val)