n = int(input())
arr = list(map(int,input().split()))
even_arr = []

for i in arr:
    if i % 2 == 0:
        even_arr.append(i)

print(*even_arr[::-1])