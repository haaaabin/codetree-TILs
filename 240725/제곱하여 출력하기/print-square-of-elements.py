n = int(input())
_list = list(map(int,input().split()))

arr = [i * i for i in _list]

print(*arr)