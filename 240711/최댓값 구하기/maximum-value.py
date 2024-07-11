a,b,c = map(int,input().split())

if a > b and b > c:
    print(a)
elif b > c and  c > a:
    print(b)
else:
    print(c)