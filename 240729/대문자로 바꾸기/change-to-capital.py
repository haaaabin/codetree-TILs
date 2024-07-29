temp = [list(input().split()) for _ in range(5)]

for i in range(5):
    for j in range(3):
        temp[i][j] = chr(ord(temp[i][j]) + ord('A')- ord('a'))
        print(temp[i][j], end=" ")
    print()