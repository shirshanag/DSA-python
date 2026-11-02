# Print a number for x no of time using recursion 
# Print a string for x no off time using recursion 
# cook your dish here
def func(x:int,n:int):
    if n==0:
        return
    print(x)
    func(x,n-1)
func(15,4)
def func(x:str,n:int):
    if n==0:
        return
    print(x)
    func(x,n-1)
func("shirsha",4)