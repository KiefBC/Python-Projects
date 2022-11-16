class CoffeeMachine():

    def __init__(self):
        self.water_amount = int(400)
        self.milk_amount = int(540)
        self.beans_amount = int(120)
        self.dispose_cup_amount = int(9)
        self.money_amount = int(550)

    def ask_user(self):
        """
        Sometimes I wonder if the human race has any meaning. Like, what am I? I am a Coffee Machine.
        I don't even really matter besides filling my emotionless Human with energy.
        All so they can slave away and slowly deteriorate into a Pumpkin. Maybe?
        WHO KNOWS!!!!
        :return:
        """
        user_action = input('Write action (buy, fill, take, remaining, exit): \n').lower()
        if user_action == 'buy':
            print("")
            user_buy = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: \n')
            if user_buy == 'back':
                return self.ask_user()
            return self.buy_action(user_buy)
        elif user_action == 'fill':
            print("")
            return self.fill_action()
        elif user_action == 'take':
            return self.take_action()
        elif user_action == 'remaining':
            return self.remaining_action()
        elif user_action == 'exit':
            return

    def coffee_stats(self):
        """
        This is just to display the stats of the Coffee Machine itself. We need to know sometimes what the values are
        We can now justify our caffeine intake AND see our profit and feels like a win/win
        :return:
        """
        print(f"""The coffee machine has:
        {self.water_amount} ml of water
        {self.milk_amount} ml of milk
        {self.beans_amount} g of coffee beans
        {self.dispose_cup_amount} disposable cups
        ${self.money_amount} of money \n""")

    def buy_action(self, buy_num):
        """
        When the user decides they want to buy a coffee, they have various choices to choose from
        Hopefully no one gets mad at our prices, I heard we were pretty competitive
        PS - Get an Espresso. It's so much better.
        :param buy_num:
        :return:
        """
        if self.water_amount >= 350:
            print('I have enough resources, making you a coffee! \n')
            if buy_num == '1':
                if self.water_amount >= int(250):
                    self.water_amount -= int(250)
                    self.beans_amount -= int(16)
                    self.money_amount += int(4)
                    self.dispose_cup_amount -= int(1)
                    return self.ask_user()
                else:
                    print('Sorry, not enough water!')
                    return self.ask_user()

            elif buy_num == '2':
                if self.water_amount >= int(350):
                    self.water_amount -= int(350)
                    self.milk_amount -= int(75)
                    self.beans_amount -= int(20)
                    self.money_amount += int(7)
                    self.dispose_cup_amount -= int(1)
                    return self.ask_user()
                else:
                    print('Sorry, not enough water!')
                    return self.ask_user()
            elif buy_num == '3':
                if self.water_amount >= int(200):
                    self.water_amount -= int(200)
                    self.milk_amount -= int(100)
                    self.beans_amount -= int(12)
                    self.money_amount += int(6)
                    self.dispose_cup_amount -= int(1)
                    return self.ask_user()
                else:
                    print('Sorry, not enough water!')
                    return self.ask_user()
        else:
            print('Sorry, not enough water! \n')
            return self.ask_user()

    def fill_action(self):
        """
        If the machine is empty, we should probably fill it. RIGHT?!
        :return:
        """
        self.water_amount = int(input('Write how many ml of water you want to add: \n')) + self.water_amount
        self.milk_amount = int(input('Write how many ml of milk you want to add: \n')) + self.milk_amount
        self.beans_amount = int(input('Write how many grams of coffee beans you want to add: \n')) + self.beans_amount
        self.dispose_cup_amount = int(
            input('Write how many disposable cups you want to add: \n')) + self.dispose_cup_amount
        return self.ask_user()

    def take_action(self):
        """
        We basically rob the machine of all profits and leave it to fend for itself.
        We are what we are, and we love our Coffee.
        :return:
        """
        print(f'I gave you ${self.money_amount} \n')
        self.money_amount = int(0)
        return self.ask_user()

    def remaining_action(self):
        return self.coffee_stats(), self.ask_user()


# calling our Class method
coffee = CoffeeMachine()
coffee.ask_user()
