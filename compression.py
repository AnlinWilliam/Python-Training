s=input()
i=0
while i<len(s):
    c=1
    while i<len(s)-1 and s[i]==s[i+1]:
        c+=1
        i+=1
    print(s[i]+str(c),end="")
    i+=1