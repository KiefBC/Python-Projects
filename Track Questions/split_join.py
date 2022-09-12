# we take our input and use title() and then remove '_' to index
x = input().title().split('_')
print(''.join(x))  # then we simply make our list a string again

# The input format:
#
# A word or phrase, with words separated by underscores, like function and variable names in Python.
#
# You might want to change the case of letters since they are not necessarily lowercased.
#
# The output format:
#
# The name written in the CapWords fashion.