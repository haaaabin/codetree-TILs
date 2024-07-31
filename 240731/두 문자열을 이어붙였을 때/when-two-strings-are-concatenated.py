A = input()
B = input()

A_B = "".join([A,B])
B_A = "".join([B,A])

if A_B == B_A:
    print("true")
else:
    print("false")