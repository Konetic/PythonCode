
class calculator:
    def add(self, a, b):
        """Return the addition of two numbers."""
        return a + b

    def subtract(self, a, b):
        """Return the subtraction of two numbers."""
        return a - b

    def multiply(self, a, b):
        """Return the multiplication of two numbers."""
        return a * b

    def divide(self, a, b):
        """Return the division of two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    
    """
#just sample files
from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
    WHITE = 'white'
# enumeration
color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
    case Color.WHITE:
        print("real blonde is from scandenvian")
 """