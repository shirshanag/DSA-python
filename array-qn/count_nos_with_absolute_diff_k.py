l=[1,2,2,1]
n=len(l)
feat_map={}
count=0
k=1
count=0
for i in range(0,n-1):
   for j in range(i+1,n):
      diff=l[i]-l[j]
      if diff==k or diff==-k:
         count+=1
print(count)

# optimal 
feat_map={}
count=0
k=1
n=len(l)
for i in l:
    if k+i in feat_map:
      count=count+feat_map[k+i]
    if i-k in feat_map:
        count=count+feat_map[i-k]
    feat_map[i]=feat_map.get(i,0)+1
print(count)

