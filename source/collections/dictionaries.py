
# https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
#
#5.5. Dictionaries

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel) # {'jack': 4098, 'sape': 4139, 'guido': 4127}
tel['irv'] = 4127
sorted_values = sorted(tel)
print(sorted_values)

tel['jack'] # 4098
del tel['sape'] 

# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
test = dict([("sape", 4139), ('guido', 4127), ('jack', 4098)])
print(f"tuple list tuple {test}") #{'sape': 4139, 'guido': 4127, 'jack': 4098}

{x: x**2 for x in (2, 4, 6)} # {2: 4, 4: 16, 6: 36}

dic_tuples = dict(sape=4139, guido=4127, jack=4098)
print(f"dictioanry tupes are  {dic_tuples}") # {'sape': 4139, 'guido': 4127, 'jack': 4098}



#5.6. Looping Techniques
#When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v) # gallahad the pure robin the brave

"""
When looping through a sequence, the position index and corresponding value can be retrieved at
the same time using the enumerate() function.
"""
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
""" 
0 tic
1 tac
2 toe """







