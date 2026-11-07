nums=[1,2,4,5,3,6]
search=7
n=len(nums)
for i in range(0,n):
    if nums[i]==search:
        print(i)
        break
    else:
        print("Not in the list!!")
        break