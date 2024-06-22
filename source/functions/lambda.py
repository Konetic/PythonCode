
# https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
# 4.8.6. Lambda Expressions¶

def make_incrementor(n):
    """lambda is a key word in python unlike java, isn't funny?"""
    return lambda x: x + n

f = make_incrementor(42)
print(f)
f(0)

f(1)

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]