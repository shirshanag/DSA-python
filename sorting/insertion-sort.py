
def insertion_sort_asc(nums):
    n=len(nums)
    for i in range(1,n):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
    return nums
l=[5,1,2,4,7,3]
print("Sorting is ascending order:",insertion_sort_asc(l))

def insertion_sort_desc(nums):
    n=len(nums)
    for i in range(1,n):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]<key:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
    return nums[0]
l=[5,1,2,4,7,3]
sort=insertion_sort_desc(l)

print("Sorting is descending order:",insertion_sort_desc(l))