dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

seq = input().lower().split()  # let's split the input right away
i = 0  # our counter we never really used it, oh well
bad_words = []  # empty list for our misspelled words
good_words = []  # empty list for all our correctly spelled words

# for loops are so nice, really become a fan of them
# we are checking and moving correctly and misspelled words to their own lists
for word in seq:
    if word not in dictionary:
        bad_words.append(word)
    elif word in dictionary:
        good_words.append(word)

if len(bad_words) == 0:  # just checking if we have any entries in the {bad_words} list
    print('OK')
else:
    print("\n".join(bad_words))  # this was a little tricky, i could not figure out how to get them on separate lines
