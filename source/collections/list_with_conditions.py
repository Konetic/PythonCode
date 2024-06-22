# 
# https://docs.python.org/3/tutorial/controlflow.html#match-statements
# Default, keyward arguments

"""
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
ask_ok(4)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

Point(0,0)
# class Point:
#     __match_args__ = ('x', 'y')
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
# points = Point(0,0)
# match points:
#     case []:
#         print("No points")
#     case [Point(0, 0)]:
#         print("The origin")
#     case [Point(x, y)]:
#         print(f"Single point {x}, {y}")
#     case [Point(0, y1), Point(0, y2)]:
#         print(f"Two on the Y axis at {y1}, {y2}")
#     case _:
#         print("Something else")


class switch_method:

    def __init__(self, testing):
        self.testing = testing
""" http testing """
def http_error(status):
    match status:
        case 400 | 401 | 404:
            print( "Bad request")
        case 404 | 405:
            print( "Not found")
        case 418 | 419:
            print( "I'm a teapot")
        case _:
           print( "Something's wrong with the internet")

http_error(600)
# strings = http_error(400)
# print(strings)

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        break
   
   # print("Found an odd number", num)

# dictionary: Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy and delete inactive users
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
        print(f"the inactive and deleted user {status} is", user)

# Strategy:  Create a new collection and return active users only
active_users = {}
for user, status in users.items(): #items() => (method) def items() -> dict_items[str, str] D.items() -> a set-like object providing a view on D's ite
    if status == 'active':
        active_users[user] = status
        print(f"active user are {status}" , (user))

# List: length some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(f"the length of {w} is ", len(w))




