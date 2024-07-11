a,b,c = map(int,input().split())

min_ = min(a,b,c)

if a == min_:
    print(1, end = " ")
else:
    print(0, end = " ")

if a == b and b == c and a == c:
    print(1, end =" ")
else:
    print(0, end =" ")