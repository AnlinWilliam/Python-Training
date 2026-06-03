l=list(map(int,input().split()))
larg=0
sec=0
for i in l:
    if i>larg:
        sec=larg
        larg=i
    elif i>sec and i!=larg:
        sec=i
print(sec)