s=input()
up=0
low=0
for i in s:
    if i.isupper():
        up+=1
    if i.islower():
        low+=1
print("No. of Upper case characters :",up)
print("No. of Lower case Characters :",low)