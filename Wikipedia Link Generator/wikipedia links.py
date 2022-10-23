import datetime

answer_format = '%m/%d'  # 09/12
link_format = '%b_%d'  # jan_01
link = 'https://en.wikipedia.org/wiki/{}'

while True:
    answer = input('What day would you like? Please use the MM/DD format. Enter "quit" to quit. ')
    if answer.upper() == 'QUIT':
        break

    try:
        # using our {answer} string to make a date formatted in respect to {answer_format}
        date = datetime.datetime.strptime(answer, answer_format)  # creating our {date} datetime obj that takes 2 args
        # output is given a {link} containing our {date} object formatted in respect to {link_format}
        output = link.format(date.strftime(link_format))
        print(output)
    # anything not in MM/DD is rejected, including something like 15/45 since there is no 15 month and 45th day
    # in the datetime library that we are using here
    except ValueError:
        print('That is not a valid date. Please try again.')