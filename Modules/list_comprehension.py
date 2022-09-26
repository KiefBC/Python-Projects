# list comprehension syntax
# new_list will simply consist of all elements from some_iterable object
new_list = [x for x in some_iterable]
# The code above is completely equivalent to the one below
# the equivalent code
new_list = []
for x in some_iterable:
    new_list.append(x)


# squared numbers
numbers = [1, 2, 3]
square_list = [x * x for x in numbers]  # [1, 4, 9]

# from string to float
strings = ["8.9", "6.0", "8.1", "7.5"]
floats = [float(num) for num in strings]  # [8.9, 6.0, 8.1, 7.5]

#
# LIST COMPREHENSION WITH IF STATEMENTS
#

# list comprehension with condition
# conditional statement allows you to filter the elements of the original collection
# and work only with the elements you need
new_list = [x for x in some_iterable if condition]

# odd numbers
numbers = [4, 8, 15, 16, 23, 42, 108]
odd_list = [x for x in numbers if x % 2 == 1]  # [15, 23]

# You can also modify the condition by using standard methods.
# For instance, if you want to create a list of words that end in -tion, you can do it like this
# conditions with functions
text = ["function", "is", "a", "synonym", "of", "occupation"]  # you can also split() to make a list from a string
words_tion = [word for word in text if word.endswith("tion")]
print(words_tion)  # ["function", "occupation"]

# else statement in list comprehension, the syntax here differs a bit
# [x if condition else y for x in some_iterable]
# Using this, we can, for example, get 0 in a new list for each negative number in the old list
old_list = [8, 13, -7, 4, -9, 2, 10]
new_list = [num if num >= 0 else 0 for num in old_list]  # num is like saying "num in old_list == __ else"
print(new_list)  # [8, 13, 0, 4, 0, 2, 10]