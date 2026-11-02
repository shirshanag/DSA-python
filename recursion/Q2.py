# Print x to n using Tail-recursion 
def func(x:int ,n:int):
    if x>n:
        return
    print(x) 
    func(x+1,n)
print("==Print 1 to n using Head-recursion==")
func(1,10)
# Print n to x  using Head-recursion
def func(x:int,n:int):
    if x>n:
        return 
    func(x+1,n)
    print(x)
print("==Print n to 10  using Head-recursion==")
func(10,15)
# Print 1 to n using Head recursion
def func_tail(n:int):
    if n==0:
        return
    func_tail(n-1)
    print(n)
print("==Print 1 to n using Head recursion==")
func_tail(10)