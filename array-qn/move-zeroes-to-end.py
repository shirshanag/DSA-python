# Better solution
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
# Optimal solution
nums=[1,0,4,3,0,2]
n=len(nums)
temp=[]
i=0
if n==1:
    print(nums)
while i<n:
    if nums[i]==0:
        break
    i+=1
if n==i:
    print(nums)
j=i+1
while j<n:
    if nums[j]!=0:
        nums[i],nums[j]=nums[j],nums[i]
        i+=1
    j+=1
print(nums)





