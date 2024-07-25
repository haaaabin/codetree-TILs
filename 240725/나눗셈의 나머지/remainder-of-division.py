a,b = map(int,input().split())
temp = [0] * b

while a >1 :
    temp[a%b] += 1
    a = a // b

sum_val = 0
for i in temp:
    sum_val += (i * i)

print(sum_val)