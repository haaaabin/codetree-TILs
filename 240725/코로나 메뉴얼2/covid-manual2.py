temp = [0] * 6

for i in range(3):
    a, b = input().split()
    b = int(b)

    if a == "Y" and b >= 37 :
        index = 1
    elif a == "N" and b >=37:
        index = 2
    elif a == "Y" and b < 37:
        index = 3
    else:
        index = 4

    temp[index] += 1

for i in range(1,5):
    print(temp[i], end=" ")

if temp[1] >= 2:
    print("E")