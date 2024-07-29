str1 = input().split()

if len(str1[0]) < len(str1[1]):
    print(str1[1], len(str1[1]))
elif len(str1[0]) > len(str1[1]):
    print(str1[0], len(str1[0]))
else:
    print("same")