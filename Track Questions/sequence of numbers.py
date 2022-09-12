seq = input().split()  # take our sequence of numbers and turn into a list
find = input()  # take our x or "find"
indexes = []

# index is our counter, value is our value at the current count for our iterable list {seq}
for index, value in enumerate(seq):
    if value == find:  # if the value is equal to our {find}
        indexes.append(str(index))  # append it

# finally print it OR don't
print(' '.join(indexes) or 'not found')