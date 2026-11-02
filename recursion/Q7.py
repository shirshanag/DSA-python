# Check wether a string is palindrome or not
s="Nitin?!nitin"
fresh=(''.join(ch for ch in s if ch.isalnum())).lower()
rev=fresh[::-1]

if (fresh==rev):
    print("Its a Palindrome string")
else:
    print("It's not a palindrome string")
# Another Approach 
s="nitin"

left=0
right=len(s)-1

while left<right:
    if (s[left]!=s[right]):
        print("Not")
    left+=1
    right-=1
print("PAL") 

# using recursion 
def pal(s:str,left,right):
   
    if left>=right:
        return True
    if s[left]!=s[right]:
        return False
    return pal(s,left+1,right-1)
print(pal("nitin",0,4))

    


