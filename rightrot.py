l=[1,2,3,4,5,6,7]
temp=l[len(l)-1]
j=l[1]
for i in range(1,len(l)-1):
    l[i+1]=l[j]
    j+=1
l[0]=temp
print(l)



l=[1,2,3,4,5,6,7]
temp=l[-1]
for i in range(len(l)-1,0,-1):
    l[i]=l[i-1]
l[0]=temp
print(l)