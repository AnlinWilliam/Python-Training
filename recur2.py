# def add(n):
#     if n==0:
#         return 200
#     a=add(n-1)                #head recursion
#     print(n,end=" ")
#     return a
# a=10
# k=add(a)
# print(k)

# def even(n):
#     if n==1:
#         return 
#     if n%2==0:
#         print(n)
#     even(n-1)
# a=10
# even(a)

# def even(n):
#     if n==1:
#         return
#     even(n-1)
#     if(n%2==0):
#         print(n,end=" ")
# a=10
# even(a)

# def rev(n):
#     if n==0:
#        return
#     print(n,end=" ")
#     rev(n-1)
#     if n>1:
#         print(n,end=" ")
# a=5
# rev(a)

def rev(n,m=0):
    if n==m:
        return
    print(m+1,end=" ")
    rev(n,m+1)
    if n!=m+1:
        print(m+1,end=" ")
a=5
rev(a)