"""
this is documentation
"""

def multiply(x, y):
    """ Return the product of x and y"""
    return x * y
#documentation
print(multiply(4,5))
print(multiply.__doc__)

class Rectangle:
    """
    a class used to represent a rectangle shape.
    """
    # def __init__(self) -> None:
    #     pass

    def __init__(self, width, length):
        self.width = width
        self.length= length

    def area(self):
        """ Return the area of the rectangle. """
        return self.width * self.length
    
    def convertEuroToDollar():
        amount * 1.28
        return result
    if __name__ == '__main__':
        print(convertEuroToDollar)