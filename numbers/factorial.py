""" Factorial Finder
The Factorial of a positive integer, n, is defined as the product of
the sequence n, n-1, n-2, ...1 and the factorial of zero, 0, is defined
as being 1. Solve this using both loops and recursion.
"""

def factorialRecursive(n):
    if n == 0:
        return 1
    else:
        return n * factorialRecursive(n - 1)

# Sadly, it seems that python is not optimized for tail-call recursion,
# so this solution will still cause a stack overflow with large enough n
def factorialTail(n, product=1):
    if n < 2:
        return 1 * product
    else:
        return factorialTail(n - 1, n * product)

def factorialIterative(n):
    product = n
    while n > 1:
        n = n - 1
        product = product * n
    return product

print(factorialRecursive(10))
print(factorialTail(10))
print(factorialIterative(10))
print(factorialIterative(1000))
# print(factorialTail(1000)) # Overflow
