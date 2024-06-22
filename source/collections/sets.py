
# https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

#5.4. Sets

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # {'orange', 'banana', 'pear', 'apple'}

a = set('abracadabra')
print(a) # unique letter

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a) # non abc letters