# ==========================
#   Brute Force Approach
# ==========================
nums=[23,1,4,5,10,11]
n=len(nums)
print("Array before rotation by one place:",nums)
temp=nums[n-1]
for i in range(n-2,-1,-1):
    nums[i+1]=nums[i]
nums[0]=temp
print("Array after rotation by one place:",nums)
# ==========================
#   Slicing Approach
# ==========================
nums[:]=[nums[n-1]]+nums[0:n-2]