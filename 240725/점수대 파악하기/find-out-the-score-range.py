nums = list(map(int,input().split()))
temp = [0] * 11

for num in nums:
    if num == 0:
        break
    if num < 10:
        continue
    k = num // 10
    temp[k] += 1

for i in range(10, 0,-1):
    print(f"{i}0 - {temp[i]}")