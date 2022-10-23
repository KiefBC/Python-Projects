shopping_list = []


def add_to_list(item):
    shopping_list.append(item)
    print("You currently have {} items in your shopping cart.".format(
        len(shopping_list)))


def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop
Enter 'HELP' for help
Enter 'LIST' for Shopping Cart
""")


def show_list():
    print("Here is your Cart:")
    for item in shopping_list:
        print(item)


show_help()
while True:
    new_item = input("> ")

    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "LIST":
        show_list()
        continue
    else:
        add_to_list(new_item)
