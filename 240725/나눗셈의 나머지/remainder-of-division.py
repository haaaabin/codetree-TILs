a,b = map(int,input().split())
temp = [0] * b
while True:
    temp[a%b] += 1
    a = a // b
    if a < 1:
        break

sum_val = 0
for i in range(len(temp)):
    sum_val += (temp[i] **2)

print(sum_val)