str1 = input()
str2 = input()
str3 = input()

len1 = len(str1)
len2 = len(str2)
len3 = len(str3)

max_val = max(len1,len2,len3)
min_val = min(len1,len2,len3)

print(max_val - min_val)