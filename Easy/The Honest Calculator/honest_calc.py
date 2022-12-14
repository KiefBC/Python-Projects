# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"

memory = 0  # just to declare it
result = 0
oper_list = ['+', '-', '*', '/']
flag = False


def is_one_digit(v):
    # asking if v is indeed an int and is great/less -10/10
    if v == int(v) and (-10 < v < 10):
        output = True
    else:
        output = False
    return output


def check(v1, v2, v3):
    # lets declare these inside the function, so we know where they belong
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != '':
        msg = msg_9 + msg
        # print out the result
        print(msg)


while True:  # let's start the flow

    print(msg_0)  # Do you even know what numbers are? Stay focused!
    calc = input().split(' ')

    x, oper, y = calc[0], calc[1], calc[2]  # combining our split()

    # will use this if the user wants to continue calculations
    if x == 'M' or y == 'M':  # checking memory
        if x == 'M':
            x = memory
        if y == 'M':
            y = memory
        elif y == 'M':
            y = memory

    if str(x).isalpha() or str(y).isalpha():  # isalpha() checks if the variables x,y are letters
        print(msg_1)
        continue
    else:  # x and y are numbers -> continue/next
        # we should check first if something is a float or not (0.2225255) vs (2)
        if x == str(x):
            if '.' in str(x):
                x = float(x)
            else:
                x = int(x)
        if y == str(y):
            if '.' in str(y):
                y = float(y)
            else:
                y = int(y)

        # kind of pointless
        check(x, y, oper)

        # making sure you don't divide by zero and confirming oper placement
        if oper == '+':
            result = (x + y)
        elif oper == '-':
            result = (x - y)
        elif oper == '*':
            result = (x * y)
        elif oper == '/':
            if oper == '/' and y != 0:
                result = (x / y)
            else:  # don't divide by zero, it is awful
                print(msg_3)
                continue
        print(float(result))

        while True:  # asking them if they want to save the number into memory

            print(msg_4)  # "Do you want to store the result? (y / n):"
            answer = input()  # read input

            if answer == 'n':
                break
            elif answer == 'y':
                # we will work from here to implement is_one_digit(result)
                if is_one_digit(result):

                    msg_index = 10
                    msg_10 = "Are you sure? It is only one digit! (y / n)"
                    msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
                    msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
                    msg_ = ""

                    # loop through our msg_10/11/12 until iterated through all of them
                    # we do this because want to make sure the user understands
                    while msg_index <= 12:

                        print(locals().get("".join(("msg_", str(msg_index)))))
                        answer = input()

                        if answer == 'y':  # if yes then ->
                            if msg_index < 12:
                                msg_index += 1
                                continue
                            if msg_index == 12:
                                flag = True
                                memory = result
                                break  # break this if cycle

                        elif answer == 'n':
                            if answer == 'n':
                                flag = True
                                break
                            else:
                                continue
                        else:
                            break
                        memory = result

                else:  # if function is false
                    memory = result  # write in memory
                    break  # next
                if flag is True:  # a flag to out this cycle
                    break  # next

        print(msg_5)  # Do you want to continue calculations? (y / n):
        answer = input()  # read answer
        if answer == 'y' or answer == 'n':  # yes or no accepted
            if answer == 'y':  # if yes, lets go back and restart
                continue
            else:
                break
