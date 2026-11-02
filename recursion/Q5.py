# Print the sum of fibbonacci series from 1 to n
def fib(n):
    if n==1:
        return 2
    return n+fib(n-1)
print(fib(5))