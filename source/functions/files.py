
# https://www.w3schools.com/python/python_file_open.asp

import os
import uuid
from bs4 import BeautifulSoup
import redirect


with open('help.txt', 'w') as f:
    with redirect_stdout(f):
        print('it now prints to `help.text`')
        

print(uuid.uuid1())

txt = f"The price is 49 dollars"
print(txt)

price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt)

def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

# Check if file exists, then delete it:
if os.path.exists("myfile.txt"):
  os.remove("myfile.txt")
else:
  print("The file does not exist") 

# Remove the folder "myfolder":
os.rmdir("myfolder") 

f = open("requirements.txt", "r") # /Users/koneabo/Documents/PythonAndPyTest/requirements.txt
print(f.read()) # returns the entire file in the files

# To delete a file, you must import the OS module, and run its os.remove() function:
os.remove("myfile.txt")
cwd = os.getcwd()
print(f"the current working directory is {cwd}")
# Loop through the file line by line:
for x in f:
  print(x) 


# Create a New empty File called myfile.txt
f = open("myfile.txt", "x")

#Create a new file if it does not exist: and throws "FileExistsError:" as "x" creates already myfile.txt
f = open("myfile.txt", "w")

# Open the file "requirements.txt" and overwrite the content:
f = open("requirements.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

f = open("requirements.txt", "r")
print(f.read(5)) # retunrs the first encount of 5 charactors

#readlines
print(f.readline()) # Read one line of the file:
f.close() 






