n = int(input())
arr = list(map(int,input().split()))

cnt = 0
result = -1
for index, elem in enumerate(arr):
	if elem == 2:
		cnt += 1
		if cnt == 3:
			result = index

print(result+1)