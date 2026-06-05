l=[1,2,3,4,5,6,7]
n=len(l)
k=int(input())
k=k%n
def rotate(i,j):
    while(i<j):
        l[i],l[j]=l[j],l[i]
        i+=1
        j-=1

rotate(0,n-1) 
rotate(0,k-1)
rotate(k,n-1)
 

print(l)
