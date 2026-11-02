# Reverse an array
nums=[4,2,34,1,2,5]
def reverse_array(nums,left,right):
    if left>=right:
        return
    nums[left],nums[right]=nums[right],nums[left]
    reverse_array(nums,left+1,right-1)
    return nums
print(reverse_array(nums,0,5))