proper_inputs = ["plain", "bold", "italic", "inline-code", "link", "header", "unordered-list", "ordered-list",
                 "new-line"]
text_inputs = []


def ask_us():
    pass


def headings():
    while True:
        heading_level = int(input('Level: '))
        if int(heading_level) > 6:
            print('The level should be within the range of 1 to 6')
            continue
        elif int(heading_level) <= 6:
            the_text = input('Text: ')
            formatted = f'{"#" * int(heading_level)} {the_text}\n'
            text_inputs.append(formatted)
            printer(formatted)
            return ask_us(), text_inputs


def text(formatter):
    if formatter == 'bold':
        the_text = input('Text: ')
        formatted = f'**{the_text}**'
        text_inputs.append(formatted)
        printer(formatted)
        return ask_us(), text_inputs
    elif formatter == 'italic':
        the_text = input('Text: ')
        formatted = f'*{the_text}*'
        text_inputs.append(formatted)
        printer(formatted)
        return ask_us(), text_inputs
    elif formatter == 'plain':
        the_text = input('Text: ')
        formatted = f'{the_text}'
        text_inputs.append(formatted)
        printer(formatted)
        return ask_us(), text_inputs
    elif formatter == 'new-line':
        formatted = '\n'
        text_inputs.append(formatted)
        printer(formatted)
        return text_inputs
    elif formatter == 'inline-code':
        the_text = input('Text: ')
        formatted = f'`{the_text}`'
        text_inputs.append(formatted)
        printer(formatted)
        return ask_us(), text_inputs


def link():
    link_label = input('Label: ')
    link_url = input('URL: ')
    formatted = f'[{link_label}]({link_url})'
    text_inputs.append(formatted)
    printer(formatted)
    return text_inputs


def printer(formatted):
    seperator = '\n'
    print(f"{''.join(text_inputs)}")
    return ask_us()


def choose_formatter(formatter):
    if formatter == '!help':
        print(' '.join(proper_inputs) + '\nSpecial commands: !help !done')
    elif formatter == 'header':
        return headings()
    elif formatter == 'plain' or formatter == 'bold' or formatter == 'italic' or formatter == 'inline-code':
        return text(formatter)
    elif formatter == 'link':
        return link()
    elif formatter == 'new-line':
        return text(formatter)
    else:
        print("Unknown formatting type or command")
        ask_us()


while True:
    formatter = input('Choose a formatter: ').lower()
    if formatter == "!done":
        break
    elif formatter not in proper_inputs:
        continue
    else:
        choose_formatter(formatter)
