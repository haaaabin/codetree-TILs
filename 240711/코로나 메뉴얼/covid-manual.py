a1, a2 = input().split()
b1, b2 = input().split()
c1, c2 = input().split()

if (a1 == "Y" and int(a2) >= 37):
    if (b1 == "Y" and int(b2) >= 37):
        print("E")
    elif (c1 == "Y" and int(c2) >= 37):
        print("E")
    else:
        print("N")
else:
    if(b1 == "Y" and int(b2) >= 37) and (c1 == "Y" and int(c2) >= 37):
        print("E")
    else:
        print("N")