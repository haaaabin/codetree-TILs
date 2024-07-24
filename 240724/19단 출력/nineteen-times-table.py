for i in range(1,20):
    for j in range(1,20):
        if j % 2 == 1:
            print(i, "*",j, "=", i*j, end="")
        else:
            print(" /", i, "*",j, "=", i*j)
        if j == 19:
            print()