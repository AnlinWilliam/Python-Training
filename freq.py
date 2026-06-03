l=[1,2,1,3,1,2,1,4,4,4,4,4,4,4,2,2,2,2]#frequency --use dictionary
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
        #print(d)----{1: 4, 2: 7, 3: 1, 4: 1}
ele,m=0,0
for key in d:
    if(d[key]>m):
        m=d[key]
        ele=key
print(ele)