# Print sum from 1 to N using parametrised recursion 
def sum_n(sum,i,n):
    if i>n:
        print(sum)
        return
    sum_n(sum+i,i+1,n)
print("Using parametrised Function")
sum_n(0,1,10)
# Print sum from 1 to N using functional recursion 
def sum_m(n):
    if n==1:
        return 1
    n=n+sum_m(n-1)
    return n
print("Using Functional recursion")
print(sum_m(5))