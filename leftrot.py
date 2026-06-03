l=[1,2,3,4,5,6,7]
r=[]
for i in range(1,len(l)):
    r.append(l[i])
r.append(l[0])
print(r)

r=[]
for i in range(2,len(l)):
    r.append(l[i])
for i in range(2):
    r.append(l[i])
print(r)