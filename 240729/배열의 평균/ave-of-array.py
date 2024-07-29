temp = [list(map(int,input().split())) for _ in range(2)]

for i in range(2):
    sum_val = 0
    for j in range(4):
        sum_val += temp[i][j]
        width_average = sum_val / 4

    print(f"{width_average:.1f}", end=" ")
print()

for j in range(4):
    sum_val = 0
    for i in range(2):
        sum_val += temp[i][j]
        length_average = sum_val / 2
    print(f"{length_average:.1f}", end=" ")
print()

sum_val = 0
for i in range(4):
    for j in range(2):
        sum_val += temp[j][i]
print(f"{(sum_val / 8):.1f}")