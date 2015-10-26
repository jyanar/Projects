""" Fibonnaci Sequence
Enter a number and have the program generate the Fibonacci sequence to
that number or to the Nth number.
"""

def fibonnaci(n):
    fn  = 1
    fn1 = 1
    fn2 = 0
    while fn < n:
        print(fn)
        fn = fn1 + fn2
        fn2 = fn1
        fn1 = fn

def uptoNthFib(n):
    fn  = 1
    fn1 = 1
    fn2 = 0
    count = 1
    while count <= n:
        print("f_{0}: {1}".format(count, fn))
        count += 1
        fn  = fn1 + fn2
        fn2 = fn1
        fn1 = fn


fibonnaci(400)
fibonnaci(1000)
uptoNthFib(400)
