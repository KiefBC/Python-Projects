random_numbers = [1, 22, 333, 4444, 55555]  # uh oh, we gonna get a type error
random_numbers = [str(x) for x in random_numbers]  # lets make it into a pretty string
print("\n".join(random_numbers))

# another method is this way
# print("\n".join([str(number) for number in random_numbers]))