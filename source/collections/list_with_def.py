from collections import deque

# https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks
# https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences


import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

filtered_data # [56.2, 51.7, 55.3, 52.5, 47.8]

# To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
questions.sort()
questions.reverse()
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

#What is your name?  It is lancelot.
#What is your quest?  It is the holy grail.
#What is your favorite color?  It is blue.

# To loop over a sequence in reverse, first specify the sequence in a forward direction and then 
# call the reversed() function
for i in reversed(range(1, 10, 2)):
    print(i)


# To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
#for test in sorted(basket):
test = sorted(set(basket))
print(test)



#5.1.3. List Comprehensions

squares = []
# comprehension
squares = list(map(lambda x: x**2, range(10))) # or
squares = [x**2 for x in range(10)]
#traditional
for x in range(10):
    squares.append(x**2)

print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y] #[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
# orrrr
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print(combs) # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

#5.1.2. Using Lists as Queues

queue_list = deque(["Eric", "John", "Michael"])
queue_list.append("Terry")           # Terry arrives
queue_list.append("Graham")          # Graham arrives
print(queue_list)
queue_list.popleft()                 
print(f"The first to arrive Eric is now leaves, {queue_list} remaining team")
queue_list.popleft()                 # The second to arrive now leaves 'John'

queue_list                           # Remaining queue in order of arrival deque(['Michael', 'Terry', 'Graham'])




fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
apple_count = fruits.count('apple') 
print(apple_count) # 2

tangerine_count = fruits.count('tangerine') 
print(tangerine_count)# 0

fruits.index('banana') # 1

fruits.index('banana', 4)  # Find next banana starting at position 4 => position 6th

fruits.reverse() #fruits ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape') #fruits ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort() # fruits ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
pop_last_fruit_sorted = fruits.pop() 
print(pop_last_fruit_sorted)# 'pear'


numbers = [1,2,3,4,5]

numbers_squared = []
for number in numbers:
  numbers_squared.append(number ** 2)

print(numbers_squared)

# List comrehension
numbers_squared = [ number ** 2 for number in numbers]
print(numbers_squared)


""" List functions"""
def my_function(food):
   """ Return the food types"""
   for fruit_type in food:
     print(fruit_type)

fruits = ["apple", "banana", "cherry"]

print(my_function(fruits))

"""
Positional-Only Arguments
You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
To specify that a function can have only positional arguments, add , / after the arguments:
"""

def positional_args(x, /):
  """" positional args statement"""
  print(x)

positional_args(3)

def positional_args2(x):
  print(x)

positional_args2(x = 3)
