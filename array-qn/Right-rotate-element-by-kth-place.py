nums=[23,1,4,2,5,1,4]
n=len(nums)
k=int(input())
r=k%n
for _ in range(0,r):
    e=nums.pop()
    nums.insert(0,e)
print(r)
print(nums)
