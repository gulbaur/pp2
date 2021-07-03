a=list(map(int, input().split()))
a.sort(key = lambda x: not x)
print(*a)