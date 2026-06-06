#longest subarray whose sum<=10
#r-l+1--len of subarray
li=[2,1,6,2,1,2,4,7,8,1,2]
k=10
r,l=0,0
m,s=0,0
while r<len(li):
    s+=li[r]
    while s>k:
        s-=li[l]
        l+=1
    length=r-l+1
    m=max(m,length)
    r+=1
print(m)