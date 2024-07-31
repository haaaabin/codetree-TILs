n = int(input())
string = [input() for _ in range(n)]
tot_str = ""

for elem in string:
    tot_str += elem
print(tot_str)