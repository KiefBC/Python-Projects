# the any() function call is the boolean value:
# it returns True if an element or a group of elements in an iterable object are evaluated True.
# Otherwise, it returns False
# True corresponds to 1, while False can be represented by 0
your_results = [True, False, False]
print(any(your_results))  # True

your_results = [1, 0, 0]
print(any(your_results))  # True

andy_results = [False, False, False]
print(any(andy_results))  # False

# The list doesn't contain any elements, and since no True value is to be found the any() function returns False
jam_results = []
print(any(jam_results))  # False

# all() function works pretty much like any().
# The difference is that all() function checks if all the elements of an iterable object are True
# and returns True if they are. Otherwise, you get False
your_results = [True, False, False]
print(all(your_results))  # False

andy_results = [True, True, True]
print(all(andy_results))  # True

# The list doesn't contain any elements,
# but the all() function will return True because it searches for any False values. No False values result in True
jam_results = []
print(all(jam_results))  # True

# any() and all() can take a list containing non-boolean values
rocket_science_scores = [0, -0, 0.0, +0]
any(rocket_science_scores)  # False
all(rocket_science_scores)  # False

math_scores = [0, 1, 2, 3]
any(math_scores)  # True
all(math_scores)  # False

# all() doesn't return True for a list where false values are present. Consider the last case ^
biology_scores = [1, 2, 3, 4]
any(biology_scores)  # True
all(biology_scores)  # True

# you can turn the elements of your list into the boolean values via comparison
scores = [1, 2, 3, 4]
boolean_scores = [score >= 3 for score in scores]  # [False, False, True, True]
print(any(boolean_scores))  # True
print(all(boolean_scores))  # False

