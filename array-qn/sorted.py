def sort(n):
    for i in range(0,len(n)-1):
        if n[i]>n[i+1]:
            return False
    return True
l=[1,2,5,3,2,4]
print(sort(l))