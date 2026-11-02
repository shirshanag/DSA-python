# Sorting in Ascending order
def bubble_sort_asc(nums):
    n=len(nums)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if(nums[j]>nums[j+1]):
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums
l=[1,4,5,2,3]
print("Sorting in ascending order:",bubble_sort_asc(l))
# Sorting in descending order
def bubble_sort_desc(nums):
    n=len(nums)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if(nums[j]<nums[j+1]):
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums

l=[1,4,5,3,3]
print("Sorting in descending order:",bubble_sort_desc(l))
