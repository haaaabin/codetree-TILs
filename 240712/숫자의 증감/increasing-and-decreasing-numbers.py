c, n = input().split()

if c == "A":
    for i in range(1,int(n)+1):
        print(i, end =" ")
if c == "D":
    for i in range(int(n)+1, 1, -1):
        print(i, end =" ")