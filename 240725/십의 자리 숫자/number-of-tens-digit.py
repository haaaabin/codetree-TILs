nums = list(map(int,input().split()))

temp = [0] * 101

for num in nums:
    if num == 0:
        break
    k = num // 10
    temp[k] += 1

for i in range(1, 10):
    print(f"{i} - {temp[i]}")