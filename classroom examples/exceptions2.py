def factorial(n):
    if n < 0:
        raise ValueError("-ve nos have no factorials")
    f=1
    for x in range(1,n+1):
        f*=x
    return f

print(factorial(3))
print(factorial(10))
print(factorial(0))

print(factorial(-78))
