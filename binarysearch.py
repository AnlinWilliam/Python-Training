#leet 34
nums=[5,7,7,8,8,10]
l=[]
target=8
start=0
end=len(nums)-1
while(start<=end):
    m=(start+end)//2
    if nums[m]==target:
        start=m-1
        end=m
        break
    elif nums[m]<target:
        start=m+1
    else:
        end=m-1
if target not in nums: 
    start=-1
    end=-1
l.append(start)
l.append(end)
print(l)