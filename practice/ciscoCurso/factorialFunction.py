#write a function that returns the factorial of a number
def factorialFunction(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    for i in range(1, n):
        n *= i
    return n
print(factorialFunction(5))
#con recursividad:
#def factorialFun(n):
#    if n < 0:
#        return None
#    if n < 2:
#        return 1
#    return n * factorialFun(n - 1)
