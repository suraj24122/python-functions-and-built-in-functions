# factorial of the given number

def fact(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
    
print(fact(5))

