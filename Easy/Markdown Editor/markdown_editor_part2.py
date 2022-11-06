# write your code here
proper_inputs = ["plain", "bold", "italic", "inline-code", "link", "header", "unordered-list", "ordered-list", "new"
                                                                                                               "-line"]

while True:
    hello_input = input("Choose a formatter: ").lower()
    if hello_input in proper_inputs:
        continue
    elif hello_input == '!help':
        print(' '.join(proper_inputs) + '\nSpecial commands: !help !done')
    elif hello_input == '!done':
        break
    else:
        print("Unknown formatting type or command")

# TODO: try using dict or sets or try match instead of if else
# TODO: try making a class and function dependent application