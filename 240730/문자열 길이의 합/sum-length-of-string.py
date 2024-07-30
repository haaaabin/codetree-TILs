n = int(input())
string = [ input() for _ in range(n)]

cnt = 0
len_val = 0

for i in range(n):
    len_val += len(string[i])
    if string[i][0] == 'a':
        cnt += 1
        
print(len_val, cnt)