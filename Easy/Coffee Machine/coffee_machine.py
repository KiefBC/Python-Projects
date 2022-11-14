water_amount = int(input('Write how many ml of water the coffee machine has: \n'))
milk_amount = int(input('Write how many ml of milk the coffee machine has: \n'))
beans_amount = int(input('Write how many grams of coffee beans the coffee machine has: \n'))
coffee_amount = int(input('Write how many cups of coffee you will need: \n'))
coffee_cups = [water_amount // 200, milk_amount // 50, beans_amount // 15]
cups_coffee = min(coffee_cups)

if coffee_amount == cups_coffee:
    print('Yes, I can make that amount of coffee ')
elif coffee_amount < cups_coffee:
    print(f'"Yes, I can make that amount of coffee and {cups_coffee - coffee_amount} more')
else:
    print(f'No, I can make only {cups_coffee} cups of coffee')

