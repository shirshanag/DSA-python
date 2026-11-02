# printing second largest element in list
# Better version
nums=[1,2,5,2,-1]
largest=-1
second=-1
for i in range(0,len(nums)):
    if nums[i]>largest:
        largest=nums[i]
for i in range(0,len(nums)):
    if nums[i]>second and nums[i]!=largest:
        second=nums[i]
print("Version 1:",second)

#Optimal version

nums=[97,32,-98,3,91,97]
largest=-1
second=-1
    
for i in range(0,len(nums)):
    if nums[i]>largest:
            largest=nums[i]
    if nums[i]>second and nums[i]!=largest:
        second=nums[i]
print("Version 2:",second)
