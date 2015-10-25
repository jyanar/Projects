""" Collatz Conjecture
Start with a number n > 1. Find the number of steps it takes to reach one
using the following process:
    If n is even, divide it by 2.
    If n is odd, multiply it by 3 and add 1.
"""

def collatz(n):
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        print(n)
    return []

print(collatz(2**89 - 1))
print(collatz(244142))
print(collatz(1000))
