# 문자열을 입력받습니다.
string = input()
	
# 문자열의 첫 번째 문자와 두 번째 문자를 저장합니다.
a = string[0]
b = string[1]
	
# 문자열을 순회하면서 첫 번째 문자와 두 번째 문자를 교환합니다.
for i in range(len(string)):
	if string[i] == a:
		string = string[:i] + b + string[i + 1:]
	elif string[i] == b:
		string = string[:i] + a + string[i + 1:]
	
# 교환된 이후의 문자열을 출력합니다.
print(string)