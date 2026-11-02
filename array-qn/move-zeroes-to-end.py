nums=[1,0,4,3,0,2]
n=len(nums)
temp=[]
for i in range(0,n):
    if nums[i]!=0:
        temp.append(nums[i])
nz=len(temp)

for i in range(0,nz):
    nums[i]=temp[i]
for j in range(nz,n):
    nums[j]=0
print(nums)

