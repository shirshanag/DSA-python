# optimal Appoach where Tc= O(n+m) sc= O(1)
nums1=[1,2,4]
nums2=[1,1,3,5]
n=len(nums1)
m=len(nums2)
i=0
j=0
res=[]
while i<n and j<m:
    if nums1[i]<=nums2[j]:
        if len(res)==0 or nums1[i]!=res[-1]:
            res.append(nums1[i])
        i+=1
    else:
        if len(res)==0 or nums2[j]!=res[-1]:
            res.append(nums2[j])
        j+=1
while i<n:
    if len(res)==0 or nums1[i]!=res[-1]:
        res.append(nums1[i])
while j<m:
        if len(res)==0 or nums2[j]!=res[-1]:
            res.append(nums2[j])
        j+=1


print(res)

