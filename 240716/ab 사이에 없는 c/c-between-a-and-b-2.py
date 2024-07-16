a,b,c = map(int,input().split())
satisfied = True

for i in range(a, b+1):
    if c % i != 0:
        satisfied = False
if satisfied == False:
    print("YES")
else:
    print("NO")