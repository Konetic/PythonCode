
#https://www.geeksforgeeks.org/args-kwargs-python/

def non_keyword_args(*argv):
    for arg in argv:
        print(arg)


non_keyword_args('Hello', 'Welcome', 'to', 'GeeksforGeeks')

#Python program to illustrate *args with a first extra argument
def non_keyword_extra_agrs(arg1, *argv):
    print("First argument :", arg1)  #First argument : Hello
    for arg in argv:
        print("Next argument through *argv :", arg) 
        
        # Next argument through *argv : Welcome
        # Next argument through *argv : to
        # Next argument through *argv : GeeksforGeeks
        

non_keyword_extra_agrs('Hello', 'Welcome', 'to', 'GeeksforGeeks')


def keyword_args(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
keyword_args(first='Geeks', mid='for', last='Geeks')


def keyword_extra_args(arg1, **kwargs):
    print("First keyword args", arg1)
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
keyword_extra_args("Hi", first='Geeks', mid='for', last='Geeks')

#Using both *args and **kwargs in Python to call a function

def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun(*args)

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)


def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun(*args)

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)


def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")


# class

Using *args and **kwargs in Python to set values of object
*args receives arguments as a tuple.
**kwargs receives arguments as a dictionary.

# defining car class
class Car():
    # args receives unlimited no. of arguments as an array
    def __init__(self, *args):
        # access args index like array does
        self.speed = args[0]
        self.color = args[1]


# creating objects of car class
audi = Car(200, 'red')
bmw = Car(250, 'black')
mb = Car(190, 'white')

# printing the color and speed of the cars
print(audi.color)
print(bmw.speed)


# defining car class
class Car():
    # args receives unlimited no. of arguments as an array
    def __init__(self, **kwargs):
        # access args index like array does
        self.speed = kwargs['s']
        self.color = kwargs['c']


# creating objects of car class
audi = Car(s=200, c='red')
bmw = Car(s=250, c='black')
mb = Car(s=190, c='white')

# printing the color and speed of cars
print(audi.color)
print(bmw.speed)
