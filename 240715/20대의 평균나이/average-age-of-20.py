cnt = 0
sum_val = 0
while True:
    n = int(input())
    if n >= 30 or n < 20:
        print(f"{average:.2f}")
        break
    sum_val += n
    cnt += 1
    average = sum_val / cnt