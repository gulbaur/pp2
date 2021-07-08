def unique(a):
    x=[]
    for i in a:
        if i not in x:
            x.append(i)
    return x
a = list(map(int,input().split()))
print(unique(a))