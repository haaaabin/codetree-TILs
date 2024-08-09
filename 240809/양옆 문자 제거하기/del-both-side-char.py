string = list(input())

string.pop(2)
string.pop(-2)

new_s = ''.join(string)
print(new_s)