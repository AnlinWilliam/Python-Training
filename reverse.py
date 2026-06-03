n=int(input())
m=0
while n>0:
    r=n%10
    m=m*10+r
    n=n//10
print(m)