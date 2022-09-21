the_input = input().split()
reversed_ = []

# reversed() is a builtin function of python
for num in reversed(the_input):
    reversed_.append(num)

print(' '.join(reversed_))
