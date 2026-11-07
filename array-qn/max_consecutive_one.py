l=[1,1,0,1,1,1]
n=len(l)
count=0
max_count=0
for i in range(0,n):
    if l[i]==1:
        count+=1
    else:
        if count>max_count:
            max_count=max(count,max_count)
            count=0
print(max(max_count,count)) # This is the for the one if we have the longest sequence at the end and there we will not encounter 0 so our else block will never run. So at the end its necessary to find the max between max_count and count 
