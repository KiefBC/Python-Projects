import random
# lets declare our variables up here and import random right away
words = ['python', 'java', 'swift', 'javascript']
missing_words = []

# make the hamgman word
hangman_word = random.choice(words)  # randomising our choice
first_letters = hangman_word[0:3]  # selecting the first index up to the third index
hidden_letters = ("-" * (len(hangman_word) - 3))  # replacing the last 3 words with ---
obfuscate = first_letters + hidden_letters  # wooaaaah coding betty, wooooah

# the game below here
print("H A N G M A N")  # announce to the werld
word = input(f"Guess the word {obfuscate}:")

# I like concating str like this it just looks a lot cleaner
print("You survived!" if word == hangman_word else "You lost!")