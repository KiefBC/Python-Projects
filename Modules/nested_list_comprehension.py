# A list in Python may contain any objects as its elements, including other lists – they are called nested lists
nested_letters  = ['a', 'b', ['c', 'd'], 'e']
nested_numbers = [[1], [2], [3]]

# Note that the nested list still counts as a single element in its parent list
numbers = [1, [2, 3], 4]
nested_numbers = numbers[1]
print(nested_numbers)     # [2, 3]
# we are calling the sub-list nested_numbers own index of 1 also be done like nested_numbers[1][1]
print(nested_numbers[1])  # 3

# possible to access an element of a nested list without an additional variable using a sequence of square brackets.
lists = [0, [1, [2, 3]]]
print(lists[1][1][0])   # 2

# Naturally, if we ask for an element at the level that doesn't exist, we'll get an error
print(lists[1][1][0][1])  # TypeError: 'int' object is not subscriptable
print(lists[3])  # IndexError: list index out of range

# consider this block below matrices (consider it one entity)
# [1 2 3]
# [4 5 6]
# [7 8 9]
# the above can also be written like
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# When we want to extract an element from the matrix,
# e.g. element M[1][2] = 6, the first index selects the row, and the second index selects the column

#
# NESTED LIST COMPREHENSION
#

# To iterate over nested lists, we can use nested list comprehensions.
# original list
school = [["Mary", "Jack", "Tiffany"],
          ["Brad", "Claire"],
          ["Molly", "Andy", "Carla"]]

# If you want to create a list of all students in all classes without the list comprehension it would look like this
student_list = []
for class_group in school:
    for student in class_group:
        student_list.append(student)

# Alternatively, we can also use a comprehension with a double for loop
student_list = [student for class_group in school for student in class_group]

# both print the same
print(student_list)  # result: ["Mary", "Jack", "Tiffany", "Brad", "Claire", "Molly", "Andy", "Carla"]

# It’s not that easy to understand what the created matrix will look like. Compare to when we will put it this way
matrix = [[j for j in range(5)] for i in range(2)]
# vs
matrix = []

for i in range(2):

    # create empty row (a sublist inside our list)
    matrix.append([])

    for j in range(5):
        matrix[i].append(j)