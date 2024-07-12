a,b = map(int,input().split())

print(f"{a//b}.",end ="")

# a를 b로 나눈 나머지에 10을 곱한 값을 b로 나눴을 때의 몫을 순서대로 적는 것을 계속 반복
na = a % b
for _ in range(20):
    na *= 10
    print(na // b , end="")

    # a를 b로 나눈 나머지를 계속 갱신해준다.
    na %= b