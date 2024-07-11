a,b = map(int,input().split())

if a < 90:
    print(0)
elif b >= 95 or b <= 100:
    print(100000)
else:
    print(50000)