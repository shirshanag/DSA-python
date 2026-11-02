def selection_sort_asc(nums):
    n=len(nums)
    for i in range(0,n):
        mid_ind=i
        for j in range(i+1,n):
            if nums[mid_ind]>nums[j]: # For ascending order
                mid_ind=j
        nums[mid_ind],nums[i]=nums[i],nums[mid_ind]
    return nums
l=[1,23,8,5,0,4,2]
print("Sorting in ascending order:",selection_sort_asc(l))
def selection_sort_desc(nums):
    n=len(nums)
    for i in range(0,n):
        mid_ind=i
        for j in range(i+1,n):
            if nums[mid_ind]<nums[j]: # For descending order
                mid_ind=j
        nums[mid_ind],nums[i]=nums[i],nums[mid_ind]
    return nums
l=[1,23,8,5,0,4,2]
print("Sorting in descending order:",selection_sort_desc(l))