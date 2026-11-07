l=[-1,0]
n=len(l)
target=-1
feat_map={}
for i in range(0,n):
    rem=target-l[i]
    if rem in feat_map:
        print(feat_map[rem],i)
    else:
        feat_map[l[i]]=i