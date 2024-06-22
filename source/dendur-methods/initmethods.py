from queue import Queue
import inspect



class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
v1 = Vector(10, 20)
print(v1.x)
"""

"""

#print(dir(int))

# declare our own string class 
class String: 
	
	# magic method to initiate object 
	def __init__(self, string): 
		self.string = string 
	
	# def __repr__(self):
	# 	return f"String({self.string})"
      
	  # orr with main method
if __name__ == '__main__': 
	
	# object creation 
	string1 = String('Hello') 

	# print object location 
	print(string1) 