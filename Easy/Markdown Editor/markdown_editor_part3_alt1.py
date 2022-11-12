# formatters section


def plain():
    return input('Text: > ')


def header():
    while True:
        level = input('Level: > ')
        try:
            level = int(level)
            assert 1 <= level <= 6
        except (ValueError, AssertionError):
            print('The level should be within the range of 1 to 6')
        else:
            break
    text = plain()
    return '#' * level + ' ' + text + '\n'


def bold():
    return f"**{input('Text: > ')}**"


def italic():
    return f"*{input('Text: > ')}*"


def inline_code():
    return f"`{input('Text: > ')}`"


def link():
    label = input('Label: > ')
    url = input('URL: > ')
    return f"[{label}]({url})"


def new_line():
    return '\n'


available_formatters = {
    'plain': plain,
    'bold': bold,
    'italic': italic,
    'inline-code': inline_code,
    'link': link,
    'header': header,
    # 'unordered-list',
    # 'ordered-list',
    'new-line': new_line,
}


# action section
def action_help():
    print('Available formatters: ' + ' '.join(available_formatters))
    print('Available commands: ' + ' '.join(available_commands))


def action_done():
    quit()


available_commands = {
    '!help': action_help,
    '!done': action_done
}

# main loop
text = ''
while True:
    user_input = input('Choose a formatter: > ')
    if user_input in available_formatters:
        text += available_formatters[user_input]()
        print(text)
        continue
    if user_input in available_commands:
        available_commands[user_input]()
        continue

    print('Unknown formatting type or command')