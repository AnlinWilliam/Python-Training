print("Enter your password:")
str=input()
u=False
l=False
d=False
s=False
sp=False
for i in str:
    if i.isupper():
        u=True
    elif i.islower():
        l=True
    elif i.isdigit():
        d=True
    elif i.isspace():
        sp=True
    else:
        s=True
if len(str)>=8 and u and l and d and s and not sp:
    print("Valid")
else:
    print("Invalid")
