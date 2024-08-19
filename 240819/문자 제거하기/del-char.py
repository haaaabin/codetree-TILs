s = list(input())

while len(s) > 1:
    a = int(input())

    if a >= len(s):
        a = -1

    s.pop(a)
    new_s = ''.join(s)
    print(new_s)