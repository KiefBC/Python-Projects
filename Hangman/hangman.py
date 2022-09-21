import random
import string
print("H A N G M A N")
won = 0
lost = 0

while True:
    menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if menu == 'play':
        guess_word = ['python', 'java', 'swift', 'javascript']
        pick_word = random.choice(guess_word)
        length = len(pick_word)
        store_word = "-" * length
        chars = []
        x = 8  # our attempts
        run = True
        while run is True and x > 0:  # while True execute
            stored_word = "".join(store_word)
            if '-' not in stored_word:  # if no more "-" then the word is solved
                break  # end loop

            else:  # continue with the game
                print()
                print(stored_word)

                check_word = input("Input a letter: ")

                if len(check_word) != 1:  # if the user inputs more than 1 letter
                    print("Please, input a single letter.")
                elif check_word not in string.ascii_lowercase:  # if the user inputs a capital
                    print("Please, enter a lowercase letter from the English alphabet.")
                elif check_word in chars:  # if the user already guessed this letter
                    print("You've already guessed this letter.")
                elif check_word not in pick_word:  # if the users guess is not in the word
                    print("That letter doesn't appear in the word.")
                    x -= 1
                elif check_word in pick_word:  # if the users guess is in the word
                    for n in range(len(pick_word)):
                        if check_word == pick_word[n]:
                            store_word = store_word[:n] + check_word + store_word[n + 1:]
            chars.append(check_word)

        if x <= 0:  # if the number of attempts is less than 0 aka THE END
            print("You lost!")
            lost += 1
            run = False
        else:  # else they win
            print(f"You guessed the word {pick_word}!")
            print("You survived!")
            won += 1
            run = False

    elif menu == 'results':
        print(f"You won: {won} times\nYou lost: {lost} times")

    else:
        if menu == 'exit':
            break

