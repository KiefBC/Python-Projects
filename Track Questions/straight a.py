text = input()
words = text.split()
for word in words:
    # just if elif checking if our words contain the arguments
    # worth checking them in lower but printing normally
    if "https://" in word.lower():
        print(word)
    elif "http://" in word.lower():
        print(word)
    elif "www." in word.lower():
        print(word)

# another way of doing this, and looks better and clean on one line
# if word.lower().startswith(('https://', 'http://', 'www.')):