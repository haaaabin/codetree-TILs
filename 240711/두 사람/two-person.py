F_age , F_sex = map(str, input().split())
S_age , S_sex = map(str,input().split())

if (int(F_age) >= 19 or int(S_age) >= 19) and (F_sex == "M" or S_sex == "M"):
    print(1)
else:
    print(0)