string = input()

for i in range(len(string)-1, -1, -1):
    if (i+1) % 2 == 0:
        print(string[i], end="")