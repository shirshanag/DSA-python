
def sorted_array(l1,l2):
    result=[]

    n=len(l1)
    m=len(l2)
    i=0
    j=0
    while i<n and j<m:
        if l1[i]<=l2[j]:
            result.append(l1[i])
            i+=1
        else:
            result.append(l2[j])
            j+=1
    while i<n:
        result.append(l1[i])
        i+=1
    while j<m:
        result.append(l2[j])
        j+=1
    return result
def merge_sort(arr):
    n=len(arr)
    if n<=1:
        return arr
    mid=n//2
    left_half=arr[:mid]
    right_half=arr[mid:]
    left=merge_sort(left_half)
    right=merge_sort(right_half)
    return sorted_array(left,right)
nums=[1,3,1,4,5,6,2,7,3]
print("Sorted Array:",merge_sort(nums))