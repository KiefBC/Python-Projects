# dictionary (dict)
# You can picture a real dictionary — a large book with definitions for a lot of words. The definition contains two parts: the word itself
# (let's call it a key) and the definition for it (a value)

birds = {"pigeon": 12, "sparrow": 5, "red crossbill": 1}
prices = {'espresso': 5.0, 'americano': 8.0, 'latte': 10, 'pastry': 'various prices'}
empty_dict = {}

print(type(birds))  # <class 'dict'>
print(type(prices))  # <class 'dict'>
print(type(empty_dict))  # <class 'dict'>birds = {"pigeon": 12, "sparrow": 5, "red crossbill": 1}
prices = {'espresso': 5.0, 'americano': 8.0, 'latte': 10, 'pastry': 'various prices'}
empty_dict = {}

print(type(birds))  # <class 'dict'>
print(type(prices))  # <class 'dict'>
print(type(empty_dict))  # <class 'dict'>

# Another way to create a dictionary is to use the dict constructor.
another_empty_dict = dict()  # using the dict constructor
print(type(another_empty_dict))  # <class 'dict'>

# note that the future dictionary keys are listed without quotes
prices_with_constr = dict({'espresso': 5.0}, americano=8.0, latte=10, pastry='various prices')

print(prices_with_constr)  # {'espresso': 5.0, 'americano': 8.0, 'latte': 10, 'pastry': 'various prices'}

# the following lines will give you an error:
# dict(americano=8.0), the left part of the expression is treated as a variable
d1 = dict(888=8.0)
d2 = dict("americano"=8.0)
d3 = dict(["americano", "filter"]=8.0)
d4 = dict(the best americano=8.0)

# Finally, you can create a nested dictionary. It's a collection of dictionaries inside one single dictionary.

# a nested dictionary example
my_pets = {'dog': {'name': 'Dolly', 'breed': 'collie'},
           'cat': {'name': 'Fluffy', 'breed': 'maine coon'}}

# another nested dictionary example
# note that keys of the outer dictionary are numbers
digits = {1: {'Word': 'one', 'Roman': 'I'},
          2: {'Word': 'two', 'Roman': 'II'},
          3: {'Word': 'three', 'Roman': 'III'},
          4: {'Word': 'four', 'Roman': 'IV'},
          5: {'Word': 'five', 'Roman': 'V'}}

# The syntax for accessing an item is quite simple — dictionary name followed by a key in square brackets [].
# This approach works both for adding objects to a dictionary and for reading them from there

my_pet = {}

# add 3 keys and their values into the dictionary
my_pet['name'] = 'Dolly'
my_pet['animal'] = 'dog'
my_pet['breed'] = 'collie'

print(my_pet)  # {'name': 'Dolly', 'animal': 'dog', 'breed': 'collie'}

# get information from the dictionary about an added item
print(my_pet['name'])  # Dolly

# our nested dictionary once again:
my_pets = {'dog': {'name': 'Dolly', 'breed': 'collie'},
           'cat': {'name': 'Fluffy', 'breed': 'maine coon'}}

print(my_pets['cat'])  # {'name': 'Fluffy', 'breed': 'maine coon'}

print(my_pets['cat']['breed'])  # maine coon

# You can save objects of any type in a dictionary, but not all of them qualify as a key. You need a good, unique key for each object in your collection
# If a key has already been added to your dictionary, its old value will be overwritten:
trilogy = {'IV': 'Star Wars', 'V': 'The Empire Strikes Back', 'VI': 'Return of the Jedi'}
print(trilogy['IV'])  # Star Wars

trilogy['IV'] = 'A New Hope'
print(trilogy['IV'])  # A New Hope

# In Python 3.7 and up, dictionaries do maintain the insertion order for values they store, but in previous versions it is not necessarily so:
alphabet = {}
alphabet['alpha'] = 1
alphabet['beta'] = 2

print(alphabet)
# Python 3.8 output: {'alpha': 1, 'beta': 2}