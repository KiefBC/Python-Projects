words = input().title().replace(' ', '')  # we have capitalized the words and removed the whitespace
# join the words list but first lower the first index and then add on the title()'d words
print(''.join(words[0].lower()) + ''.join(words[1:]))