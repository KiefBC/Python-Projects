# Given two strings, text and pattern, we need to identify whether there is at least one occurrence of the pattern in
# the text

# The function named contains takes two strings, text and pattern, as input and returns True if text contains pattern
# and False otherwise.

def contains(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        found = True

        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                found = False
                break

        if found:
            return True

    return False

# or just do this
print(b in a)


contains("abacabad", "cab")  # True
contains("abacabad", "abacabad")  # True
contains("aba", "")  # True
contains("abacabad", "hello")  # False

# Another way to define if there's a specific pattern in our string is called membership testing
# it is implemented with the help of the operators in and not in
print("apple" in "pineapple")  # True
print("milk" in "yogurt")  # False
print('' in '')  # True
print('' not in "lemon")  # False

# Methods startswith() and endswith() return True if the pattern is found and False otherwise
email = "email_address@something.com"
print(email.startswith("www."))  # False
print(email.endswith("@something.com"))  # True

# Optional values for start and end that bound the search area can be added: string.startswith(pattern, start,
# end). When we specify only one additional element, it's automatically considered as start
email = "my_email@something.com"
print(email.startswith("email", 2))  # False
print(email.startswith("email", 3))  # True
# In the example above, when we specified the start argument as 2, we limited the search to the substring
# "_email@something.com", which actually doesn't start with "email". Then we fixed this off-by-one mistake by setting
# start to 3.

# The substring defined for the search in the first case is "ail", while in the second one it's "ail@".
email = "my_email@something.com"
print(email.endswith("@", 5, 8))  # False
print(email.endswith("@", 5, 9))  # True

# how to define the exact position of the substring. We can use the methods find() or index()
best = "friend"

print(best.find("i"))   # 2
print(best.index("i"))  # 2

# -1 if it can't find the given element, while the latter raises ValueError
print(best.find("u"))   # -1
print(best.index("u"))  # ValueError

# In the string friend, the substring end occupies positions from 3 to 5, and the start index is returned
print(best.find("end"))  # 3

# we can additionally specify an interval for searching, just as with the boolean search:
# string.find(pattern, start, end)
magic = "abracadabra"
print(magic.find("ra"))  # 2
print(magic.find("ra", 5))      # 9
print(magic.find("ra", 5, 10))  # -1
# Alternatively, we can use methods rfind() and rindex() to search backward from the end of the string.
print(magic.rfind("ra"))  # 9
print(magic.rindex("a"))  # 10

# count how many times an element (a char or a substring) occurs in the string, and for this,
# we can use the method count()
magic = "abracadabra"
print(magic.count("abra"))  # 2
print(magic.count("a"))     # 5

# Write a function that takes a string with instructions: if it starts or ends with the words "Simon says",
# your function should return the string "I " plus what you would do: the instructions themselves. Otherwise,
# return "I won't do it!".
def what_to_do(phrase):
    if phrase.startswith("Simon says"):
        return "I {}".format(phrase[len('Simon says') + 1:])
    elif phrase.endswith("Simon says"):
        return "I {}".format(phrase[:len('Simon says') + 1])
    return "I won't do it!"