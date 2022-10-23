import random

# find out who is playing who
# declare out global vars
names = ["John", "Jack"]
k = 1
s_ = "'s turn!"
one_pencil = "|"
first_name = 0

# find out the starting amount of pencils on the table
print("How many pencils would you like to use:")
pencils = input()

# isnumeric() just checks if the str.pencils is a numeral (number)
while pencils.isnumeric() is False or pencils == "0":
    # if it is not a number
    if pencils.isnumeric() is False:
        print("The number of pencils should be numeric")
        pencils = input()
    # 0 is not positive and is not accepted
    elif pencils == "0":
        print("The number of pencils should be positive")
        pencils = input()

# python wants us to be explicit right?
pencils = int(pencils)

# let's ask who is going first
print("Who will be the first (" + names[0] + ", " + names[1] + "):")
first_name = input()

# if the input is not in the names list? retry
while first_name not in names:
    print("Choose between", names[0], "and", names[1])
    first_name = input()

# |||||||
print(pencils * one_pencil)

# now lets start the game until we have no more pencils
while pencils > 0:

    if first_name == names[0]:

        print(names[0] + s_)
        # ask the next player to choose a number between 1-3
        # pencils_2 is our removed amount
        pencils_2 = input()

        while pencils_2 == "0" or pencils_2.isnumeric() is False or int(pencils_2) > 3 or int(pencils_2) > pencils:
            # we only accept 1 2 or 3
            if pencils_2 == "0" or pencils_2.isnumeric() is False:
                print("Possible values: '1', '2' or '3'")
                pencils_2 = input()
            # you can only take so many pencils, remind the user
            elif int(pencils_2) > 3:
                # if removal amount is greater than 3 AND greater than the remaining amount
                if int(pencils_2) > 3 and int(pencils_2) > pencils:
                    print("Too many pencils were taken")
                    print("Possible values: '1', '2' or '3'")
                    pencils_2 = input()
                # if the removal amount is greater than 3 and less than remaining amount
                elif 3 < int(pencils_2) < pencils:
                    print("Too many pencils were taken")
                    print("Possible values: '1', '2' or '3'")
                    pencils_2 = input()
                # if the removal amount is greater than 3 and equal to the remaining amount
                elif int(pencils_2) > 3 and int(pencils_2) == pencils:
                    print("Too many pencils were taken")
                    print("Possible values: '1', '2' or '3'")
                    pencils_2 = input()
            # if the removal amount is within the parameters but is greater than the remaining amount
            elif int(pencils_2) > pencils:
                print("Too many pencils were taken")
                pencils_2 = input()
        # subtracting the removal amount from the remaining amount
        pencils -= int(pencils_2)
        print(pencils * one_pencil)
        first_name = names[1]
    else:
        # the second player (the bot) turn
        print(names[1] + "'s turn:")
        # the rudimentary AI logic
        if pencils % 4 == 0:
            pencils_2 = 3
        elif pencils % 4 == 3:
            pencils_2 = 2
        elif pencils % 4 == 2:
            pencils_2 = 1
        elif pencils == 1:
            pencils_2 = 1
        else:
            pencils_2 = random.randint(1, 3)

        pencils -= int(pencils_2)
        print(pencils_2)
        print(pencils * one_pencil)
        first_name = names[0]

# have to let the winner know they won right?
if first_name == names[0]:
    print(names[0], "won!")
else:
    print(names[1], "won!")
