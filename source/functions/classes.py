

class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

# class Person:
#     def __init__(self) -> None:
#         pass

# Python3 program to demonstrate instantiating a class
class Dog:

    # A simple class attribute
    attr1 = "mammal"
    attr2 = "dog"

    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)

# Driver code Object instantiation
rodger = Dog()

# Accessing class attributes and method through objects
print("directly from the class object instantiation " + rodger.attr1)
rodger.fun()

print("testing fetch cmd")