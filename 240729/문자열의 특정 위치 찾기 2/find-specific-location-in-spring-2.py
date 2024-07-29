temp = ['apple', 'banana', 'grape', 'blueberry','orange']
 
n = input()
cnt = 0

for i in range(5):
    if temp[i][2] == n or temp[i][3] == n:
        print(temp[i])
        cnt += 1

print(cnt)