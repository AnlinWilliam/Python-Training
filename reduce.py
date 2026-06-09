# def red(c,n): 
#     if n<=1:
#         return c
#     if n%2==0:
#         c+=1
#         n=n//2
#     else:
#         c+=2
#         n+=1
#         n=n//2 
#     return red(c,n)

# n=int(input())
# print(red(0,n))

def fun(n):
    if n==1:
        return 0
    elif n%2==0:
        return 1+fun(n//2)
    else:
        return 1+min(fun(n-1),fun(n+1))
n=int(input())
print(fun(n))