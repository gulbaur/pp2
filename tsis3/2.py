a = list(input().split())
min = 100000
for i in range(len(a)):
    n = int(a[i])
    if n<min and n>=0:
        min= n
print(min)