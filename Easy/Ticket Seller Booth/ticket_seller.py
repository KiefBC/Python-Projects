TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100

# create calculate_price function take number of tickets and returns


def calculate_price(tickets):
    return (tickets * TICKET_PRICE) + SERVICE_CHARGE

# run this code forever until we run outta tickets


while tickets_remaining >= 1:
    # output how many tickets are remaining using the tickets_remaining var
    print("We have exactly, {} tickets remaining!".format(tickets_remaining))
    user = input("What is your name?    ")
    tickets = input(
        "How many Tickets would you like to purchase {}?    ".format(user))
    # expect a ValueError to happen and handle it
    try:
        tickets = int(tickets)
        # raise a ValueError if request is more than available
        if tickets > tickets_remaining:
            raise ValueError(
                "There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Oh no we ran into an issue. {}. Please try again".format(err))
    else:
        # calculations for price (num of tickets * price)
        full_price = calculate_price(tickets)
        print("Okay {}, the total price for {} tickets is ${}".format(
            user, tickets, full_price))
        confirmed = input("Are you sure? Y/N    ")
        if confirmed.lower() == "y":
            tickets_remaining -= tickets
            tickets_remaining = int(tickets_remaining)
            print("There are now only {} tickets remaining!".format(
                tickets_remaining))
        else:
            print("Can you not read? Goodbye {}".format(user))

# notify everyone the tickets have sold out
print("There are no tickets left, fuck off")
