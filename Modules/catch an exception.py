# Capture the input (e.g. 2) as an integer value
index = int(input())

# Get a list of all the exceptions returned from calling the builtin function
all_exceptions = dir(locals()['__builtins__'])

# Print the exception with the index provided as input
print(all_exceptions[index])