n = int(input())
arr = []
multiplus = 1
cnt = 0

while True:
    result = n * multiplus
    print(result, end= " ")
    multiplus += 1
    if result % 5 == 0:
        cnt += 1
    
    if cnt >= 2:
        break