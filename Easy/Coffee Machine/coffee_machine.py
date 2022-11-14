water_amount = int(400)
milk_amount = int(540)
beans_amount = int(120)
dispose_cup_amount = int(9)
money_amount = int(550)
while True:

    print(f"""
    The coffee machine has:
    {water_amount} ml of water
    {milk_amount} ml of milk
    {beans_amount} g of coffee beans
    {dispose_cup_amount} disposable cups
    ${money_amount} of money \n""")

    user_action = input('Write action (buy, fill, take): \n').lower()

    if user_action == 'buy':
        user_buy = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: \n')
        if user_buy == '1':
            water_amount -= int(250)
            beans_amount -= int(16)
            money_amount += int(4)
            dispose_cup_amount -= int(1)
            print(f"""
                The coffee machine has:
                {water_amount} ml of water
                {milk_amount} ml of milk
                {beans_amount} g of coffee beans
                {dispose_cup_amount} disposable cups
                ${money_amount} of money \n""")
            break
        elif user_buy == '2':
            water_amount -= int(350)
            milk_amount -= int(75)
            beans_amount -= int(20)
            money_amount += int(7)
            dispose_cup_amount -= int(1)
            print(f"""
                The coffee machine has:
                {water_amount} ml of water
                {milk_amount} ml of milk
                {beans_amount} g of coffee beans
                {dispose_cup_amount} disposable cups
                ${money_amount} of money \n""")
            break
        elif user_buy == '3':
            water_amount -= int(200)
            milk_amount -= int(100)
            beans_amount -= int(12)
            money_amount += int(6)
            dispose_cup_amount -= int(1)
            print(f"""
                The coffee machine has:
                {water_amount} ml of water
                {milk_amount} ml of milk
                {beans_amount} g of coffee beans
                {dispose_cup_amount} disposable cups
                ${money_amount} of money \n""")
            break
    elif user_action == 'fill':
        water_amount = int(input('Write how many ml of water you want to add: \n')) + water_amount
        milk_amount = int(input('Write how many ml of milk you want to add: \n')) + milk_amount
        beans_amount = int(input('Write how many grams of coffee beans you want to add: \n')) + beans_amount
        dispose_cup_amount = int(input('Write how many disposable cups you want to add: \n')) + dispose_cup_amount
        print(f"""
            The coffee machine has:
            {water_amount} ml of water
            {milk_amount} ml of milk
            {beans_amount} g of coffee beans
            {dispose_cup_amount} disposable cups
            ${money_amount} of money \n""")
        break
    elif user_action == 'take':
        print(f'I gave you ${money_amount} \n')
        money_amount = int(0)
        print(f"""
            The coffee machine has:
            {water_amount} ml of water
            {milk_amount} ml of milk
            {beans_amount} g of coffee beans
            {dispose_cup_amount} disposable cups
            ${money_amount} of money \n""")
        break

