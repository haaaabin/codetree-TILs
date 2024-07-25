n = int(input())

_list = list(map(int,input().split()))

new_list = ( i for i in _list if i % 2 == 0)

print(*new_list)