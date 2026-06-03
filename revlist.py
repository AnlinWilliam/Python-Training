l=[1,2,3,4,5,6]
j=len(l)-1
for i in range(len(l)//2):
    temp=l[i]
    l[i]=l[j]
    l[j]=temp
    j-=1
print(l)
j=len(l)-1
for i in range(len(l)//2):
    temp=l[i]
    l[i]=l[j]
    l[j]=temp
    j-=1
print(l)