# write your code here
# calc = input().split(' ')
oper_list = ['+', '-', '*', '/']
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

while True:  # lets start the flow

    print(msg_0)
    calc = input().split(' ')
    x, oper, y = calc[0], calc[1], calc[2]  # combining our split()

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
            else:  # we dont need this per objective, but, why not?
                print("Yeah... division by zero. Smart move...")
                continue
        else:  #
            print(msg_2)
            continue
        # print(float(result))
        break

