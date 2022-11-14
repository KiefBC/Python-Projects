water_amount = int(400)
milk_amount = int(540)
beans_amount = int(120)
dispose_cup_amount = int(9)
money_amount = int(550)


def coffee_machine():
    print(f"""The coffee machine has:
    {water_amount} ml of water
    {milk_amount} ml of milk
    {beans_amount} g of coffee beans
    {dispose_cup_amount} disposable cups
    ${money_amount} of money \n""")


def buy_action(type):
    global water_amount, milk_amount, beans_amount, dispose_cup_amount, money_amount
    if type == '1':
        if water_amount >= int(250):
            water_amount -= int(250)
            beans_amount -= int(16)
            money_amount += int(4)
            dispose_cup_amount -= int(1)
            return ask_user()
        else:
            print('Sorry, not enough water!')
            return ask_user()

    elif type == '2':
        if water_amount >= int(350):
            water_amount -= int(350)
            milk_amount -= int(75)
            beans_amount -= int(20)
            money_amount += int(7)
            dispose_cup_amount -= int(1)
            return ask_user()
        else:
            print('Sorry, not enough water!')
            return ask_user()
    elif type == '3':
        if water_amount >= int(200):
            water_amount -= int(200)
            milk_amount -= int(100)
            beans_amount -= int(12)
            money_amount += int(6)
            dispose_cup_amount -= int(1)
            return ask_user()
        else:
            print('Sorry, not enough water!')
            return ask_user()


def fill_action():
    global water_amount, milk_amount, beans_amount, dispose_cup_amount, money_amount
    water_amount = int(input('Write how many ml of water you want to add: \n')) + water_amount
    milk_amount = int(input('Write how many ml of milk you want to add: \n')) + milk_amount
    beans_amount = int(input('Write how many grams of coffee beans you want to add: \n')) + beans_amount
    dispose_cup_amount = int(input('Write how many disposable cups you want to add: \n')) + dispose_cup_amount
    return ask_user()


def take_action():
    global money_amount
    print(f'I gave you ${money_amount} \n')
    money_amount = int(0)
    return ask_user()


def remaining_action():
    return coffee_machine(), ask_user()


def ask_user():
    user_action = input('Write action (buy, fill, take, remaining, exit): \n').lower()
    if user_action == 'buy':
        print("")
        user_buy = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: \n')
        if user_buy == 'back':
            return ask_user()
        print('I have enough resources, making you a coffee! \n')
        return buy_action(user_buy)
    elif user_action == 'fill':
        return fill_action()
    elif user_action == 'take':
        return take_action()
    elif user_action == 'remaining':
        return remaining_action()
    elif user_action == 'exit':
        return

ask_user()