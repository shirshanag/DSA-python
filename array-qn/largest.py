# largest element in array
nums=[1,2,5,3]
l=nums[0]
for i in range(0,len(nums)):
    if nums[i]>l:
        l=nums[i]
print(l)