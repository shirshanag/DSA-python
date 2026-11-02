# Brute force approach
nums=[1,2,3,4,5,6,7,8,9,10]
freq_map={}

def duplicate(nums):
    n=len(nums)
    for i in range(0,n):
        freq_map[nums[i]]=0
    j=0
    for k in freq_map:
        nums[j]=k
        j+=1
    return freq_map.keys()
print(duplicate(nums))
# Here the Time complexity is O(n) and Space complexity is O(n)
# Optimal solution
n=len(nums)
i=0
j=i+1
while j<n:
    if nums[i]!=nums[j]:
        i+=1
        nums[i],nums[j]=nums[j],nums[i]
    j+=1
print(i+1)
# Here the Time complexity is O(n) and Space complexity is O(1)
