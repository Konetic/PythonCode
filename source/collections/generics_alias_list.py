
# https://docs.python.org/3/library/stdtypes.html#typecontextmanager


import sys 

#stdout can be also be used to print multiple elements. Not just this stdout can be assigned to another variable as long as it supports write().

# stdout assigned to a variable 
var = sys.stdout 
arr = ['geeks', 'for', 'geeks'] 
  
# printing everything in the same line 
for i in arr: 
    var.write(i) 
  
# printing everything in a new line 
for j in arr: 
    var.write('\n'+j) 

#new line escape character
sys.stdout.write('gfdfgfhfgjghjk cfhghjghkhjljk fhfgjfghkh\ndfgsdfhsfgj')
sys.stdout.write('gfg') 
sys.stdout.write('geeks') 
sys.stdout.write('\n') 
sys.stdout.write('for geeks') 



# a function expecting a list containing float elements:
def average(values: list[float]) -> float:
    return sum(values) / len(values)

list = [3.7,4.6,5.8]
average(list)
print (list)