# l=[2,3,1,5,2,4,6,7,8,5,2,2,3]
# k=int(input())
# s=0
# for i in range(0,len(l)-k):
#     sum=0
#     for j in range(i,i+k):
#         sum+=l[j]
#     s=max(s,sum)
# print(s)
l=[2,3,1,5,2,4,6,7,8,5,2,2,3]
n=len(l)
k=int(input())
s=sum(l[:k])
m=s
for i in range(1,n-k+1):
    s=s-l[i-1]+l[i+k-1]
    m=max(m,s)
print(m)