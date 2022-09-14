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

while True:  # lets start the flow

    print(msg_0)
    calc = input().split(' ')

    x, oper, y = calc[0], calc[1], calc[2]  # combining our split()

    if x == "M" or y == "M":  # checking memory
        if x == "M":
            x = memory
        if y == "M":
            y = memory
        elif y == "M":
            y = memory

    if str(x).isalpha() or str(y).isalpha():  # isalpha() checks if the variables x,y are letters
        print(msg_1)
        continue

    else:  # x and y are numbers -> continue/next -> oper adding to string
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

        if oper == "+":
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
        # break

        while True:  # asking them if they want to save the number into memory

            print(msg_4)
            answer = input()  # read input

            if answer == "n":
                break
            elif answer == "y":  # if yes then
                answer = memory

        print(msg_5)  # print msg_5
        answer = input()  # read answer
        if answer == "y" or a == "n":  # checking yes or no
            if answer == "y":  # if yes
                continue  # start again
            elif answer == "n":  # if no
                break  # end



