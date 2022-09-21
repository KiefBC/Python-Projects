# A set is an unordered container of hashable objects sets do NOT record element position or order of insertion,
# so you cannot retrieve an element by its index So, depending on the situation, you need to decide what is more
# important to you: preserving the order of items in your collection or testing for membership in a faster way. In
# the first case, it's reasonable to store your items in the list, in the second it's better to use set.

# CREATING SETS

empty_set = set()
print(type(empty_set))   # <class 'set'>

empty_dict = {}
print(type(empty_dict))  # <class 'dict'>

# If you pass a string or a list into set(),
# the function will return a set consisting of all the elements of this string/list:
flowers = {'rose', 'lilac', 'daisy'}
# the order is not preserved
print(flowers)  # {'daisy', 'lilac', 'rose'}
letters = set('philharmonic')
print(letters)  # {'h', 'r', 'i', 'c', 'o', 'l', 'a', 'p', 'm', 'n'}

# Each element is considered a part of a set only once, so double letters are counted as one element:
letters = set('Hello')
print(len(letters))  # the length equals 4
print(letters)       # {'H', 'e', 'o', 'l'}

# Moreover, using sets can help you avoid repetitions:
states = ['Russia', 'USA', 'USA', 'Germany', 'Italy']
print(set(states))  # {'Russia', 'USA', 'Italy', 'Germany'}

# the order of naming the elements doesn't play any role, the following two sets will be equal.
set1 = {'A', 'B', 'C'}
set2 = {'B', 'C', 'A'}
print(set1 == set2)  # True

# WORKING WITH A SETS ELEMENTS

# get the number of a set's elements with the help of len() function.
# go through all the elements using for loop.
# check whether an element belongs to a specific set or not (in / not in operators), you get the boolean value.
nums = {1, 2, 2, 3}
print(1 in nums, 4 not in nums)  # True True

# add a new element to the set with add() method or update() it with another collection
nums = {1, 2, 2, 3}
nums.add(5)
print(nums)  # {1, 2, 3, 5}

more_nums = {6, 7}
nums.update(more_nums)
print(nums)  # {1, 2, 3, 5, 6, 7}

# we can also add a list
text = ['how', 'are', 'you']
nums.update(text)
print(nums)  # {'you', 1, 2, 3, 5, 6, 7, 'are', 'how'}

# or a string
word = 'hello'
nums.add(word)
print(nums)  # {1, 2, 3, 'how', 5, 6, 7, 'hello', 'you', 'are'}

# delete an element from a specific set using discard/remove methods. The only difference between them operating is a
# situation when the element to be removed is absent from this set. In this case, discard does nothing and remove
# generates a KeyError exception.
nums.remove(2)
print(nums)  # {1, 3, 5}

empty_set = set()
empty_set.discard(2)  # nothing happened
empty_set.remove(2)   # KeyError: 2

# remove one random element using pop() method. As it's going to be random, you don't need to choose an argument.
# delete all elements from the set with clear() method.
nums = {1, 2, 2, 3}
nums.pop()
print(nums)  # {2, 3}

# FROZENSET

# The only difference between set and frozenset is that set is a mutable data type, but frozenset is not.
# To create a frozenset, we use the frozenset()
empty_frozenset = frozenset()
print(empty_frozenset)  # frozenset()

# We can also create a frozenset from a list, string or set:
frozenset_from_set = frozenset({1, 2, 3})
print(frozenset_from_set)  # frozenset({1, 2, 3})

frozenset_from_list = frozenset(['how', 'are', 'you'])
print(frozenset_from_list)  # frozenset({'you', 'are', 'how'})

# frozenset is immutable. This means that while the elements of a set can change,
# in a frozenset they remain unchanged after creation
empty_frozenset.add('some_text')  # AttributeError: 'frozenset' object has no attribute 'add'

# So why do we need frozenset exactly? Since a set is mutable, we can't make it an element of another set
text = {'hello', 'world'}
nested_text = {'!'}
nested_text.add(text)  # TypeError: unhashable type: 'set'

# But with a frozenset, such problems will not appear. It can be an element of another set or an element of
# another frozenset due to its hashability and immutability.
some_frozenset = frozenset(text)
nested_text.add(some_frozenset)
print(nested_text)  # {'!', frozenset({'world', 'hello'})}