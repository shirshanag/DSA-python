# Extreme brute force solution
l=[1,0,2,3]
n=4
for i in range(0,n+1):
    if i not in l:
        print(i)
        break
# Better solution 
feat_map={}
for i in range(0,n+1):
    feat_map[i]=0
for num in l:
    feat_map[num]=1

for k,v in feat_map.items():
    if v==0:
        print(k)
# optimal solution
p_sum=0
for i in range(0,n+1):
    p_sum=p_sum+i
n=sum(l)
diff=p_sum-n
print(diff)