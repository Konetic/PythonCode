
# https://docs.python.org/3/tutorial/controlflow.html#match-statements

for test in set(range(5, 10)):
    if test % 2 == 0:
        print(test)

list(range(0, 10, 3)) # [0, 3, 6, 9]

list(range(-10, -100, -30)) #[-10, -40, -70]
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

#v 4.8.8. Function Annotations

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')
#Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
#Arguments: spam eggs 'spam and eggs'

# any arguments
def cheeseshop(*arguments):
    """Do nothing, but document it.
    No, really, it doesn't do anything.
    """
    print(cheeseshop.__doc__)

    print("-- Do you have any""?")
    print("-- I'm sorry, we're all out of")
    for test in arguments:
        print(test)
    print("-" * 40)


cheeseshop("Limburger", "It's very runny, sir.",
        "It's really very, VERY runny, sir.",) 


# *name must occur before **name

# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])

# cheeseshop("Limburger", "It's very runny, sir.",
#         "It's really very, VERY runny, sir.",
#         shopkeeper="Michael Palin",
#         client="John Cleese",
#         sketch="Cheese Shop Sketch")      

# accepts one required argument (voltage) and three optional arguments (state, action, and type).

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)                                          # 1 positional argument parrot()  # required argument missing
parrot(voltage=1000)                                  # 1 keyword argument parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments parrot(110, voltage=220)     # duplicate value for the same argument
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments parrot(actor='John Cleese')  # unknown keyword argument
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword







"""
4.8.1. Default Argument Values
The most useful form is to specify a default value for one or more arguments. This creates a 
function that can be called with fewer arguments than it is defined to allow.
This function can be called in several ways:
giving only the mandatory argument: ask_ok('Do you really want to quit?')
giving one of the optional arguments: ask_ok('OK to overwrite the file?', 2)
or even giving all arguments: ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
"""
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)