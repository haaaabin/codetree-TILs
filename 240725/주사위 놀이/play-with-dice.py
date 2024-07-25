nums = list(map(int,input().split()))
temp = [0] * 7

for num in nums:
    temp[num] +=1

for i in range(1,7):
    print(f"{i} - {temp[i]}")