n = int(input())
satisfied = True

for i in range(2, n):
    if i % n == 0:
        satisfied = False
if satisfied == True:
    print("P")
else:
    print("C")