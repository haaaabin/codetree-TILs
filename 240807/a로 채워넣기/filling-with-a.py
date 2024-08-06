s = list(input())
s[1] = 'a'
s[-2] = 'a'

new_s = ''.join(s)
print(new_s)