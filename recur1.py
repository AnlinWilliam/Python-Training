def add(n):
    if n==0:
        return 
    print(n)
    add(n-1)        #tail recursion
a=10
add(a)