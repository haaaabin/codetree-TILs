n = int(input())
temp = input().split()
tot_str = ""

for i in range(n):
    tot_str += temp[i]

for i in range(len(tot_str)):
    print(tot_str[i], end="")
    if (i+1) % 5 == 0:
        print()