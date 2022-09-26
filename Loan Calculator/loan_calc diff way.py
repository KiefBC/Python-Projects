def main():
    print("Enter the loan principal:")
    get_loan()
    what_to_calculate()


def get_loan():
    get_loan.loan = int(input())
    return get_loan.loan


def what_to_calculate():
    print("What do you want to calculate?")
    print('type "m" for number of monthly payments,')
    print('type "p" for the monthly payment:')
    action = input()
    if action == "m":
        calculate_num_mont_payment()
    elif action == "p":
        calculate_mont_payment()


def calculate_num_mont_payment():
    total_amount = get_loan.loan
    print("Enter the monthly payment:")
    monthly_payment = int(input())
    months = total_amount / monthly_payment
    if months == 1:
        print("It will take {} month to repay the loan".format(int(months)))
    elif total_amount % monthly_payment == 0:
        print("It will take {} months to repay the loan".format(int(months)))
    else:
        print("It will take {} months to repay the loan".format(int(months + 1)))


def calculate_mont_payment():
    total_amount = get_loan.loan
    print("Enter the number of months:")
    month_numbers = int(input())
    monthly_payment = total_amount / month_numbers
    if total_amount % int(month_numbers) != 0:
        monthly_payment = int(monthly_payment + 1)
        last_payment = total_amount - (month_numbers - 1) * monthly_payment
        print("Your monthly payment = {} and the last payment = {}".format(int(monthly_payment), int(last_payment)))
    else:
        print("Your monthly payment = {}".format(int(monthly_payment)))


if __name__ == '__main__':
    main()