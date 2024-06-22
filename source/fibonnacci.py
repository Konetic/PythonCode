

# https://docs.python.org/3/tutorial/modules.html#importing-from-a-package


from fibo import fib as fibonacci
fibonacci(500)

from fibo import *

import fibo
fibo.fib(10) 

import fibo as fib
fib.fib(500)

# If you intend to use a function often you can assign it to a local name:
fi = fibo.fib
fi(10)

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)