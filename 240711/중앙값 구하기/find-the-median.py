a,b,c = map(int,input().split())

if a >= b:
    if b >= c:
        print(b)
    else:
        print(a)
else:
    if a >= c:
        print(a)
    else:
        print(c)