def factorial(n):
    ans = 1
    while n > 0:
        ans = ans * n
        n -= 1
    return ans

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))