n = int(input())
string = [input() for _ in range(n)]
a = input()
cnt = 0
leng = 0
for i in range(n):
    if string[i][0] == a:
        cnt += 1
        leng += len(string[i])
    
print(f"{cnt} {(leng / cnt):.2f}")