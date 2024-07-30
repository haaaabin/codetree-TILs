n = int(input())
cnt = 0
len_val = 0

for i in range(n):
    text = input()
    len_val += len(text)
    for i in text:
        if i == 'a':
            cnt += 1

print(len_val, cnt)