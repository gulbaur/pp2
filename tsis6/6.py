def check(a,b,c):
    if c>=a and c<=b:
        return True
    else:
        return False
a,b,c = map(int,input().split())
if check(a,b,c):
    print("YES")
else:
    print("NO")