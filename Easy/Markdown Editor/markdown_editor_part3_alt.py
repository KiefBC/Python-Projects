class Editor:
    def get_text(self):
        self.text = input('Text:')

    def get_level(self):
        while True:
            answer = input('Level:')
            if not answer.isdigit() or not (1 <= int(answer) <= 6):
                print('The level should be within the range of 1 to 6')
                continue
            self.level = int(answer)
            break

    def get_label(self):
        self.label = input('Label:')

    def get_url(self):
        self.url = input('URL:')

    formatters = {
        'plain':('text',),
        'bold':('text',),
        'italic':('text',),
        'header':('level','text'),
        'link':('label', 'url'),
        'inline-code':('text',),
        'ordered-list':(),
        'unordered-list':(),
        'new-line':()}

    def __init__(self):
        self.text = None
        self.level = None
        self.label = None
        self.url = None
        self.page = ''

    def add_page(self, s):
        self.page += s

    def print_page(self):
        print(self.page)

    def put_plain(self):
        self.add_page(self.text)

    def put_bold(self):
        self.add_page(f'**{self.text}**')

    def put_italic(self):
        self.add_page(f'*{self.text}*')

    def put_header(self):
        self.add_page(f'{"#" * self.level} {self.text}\n')

    def put_link(self):
        self.add_page(f'[{self.label}]({self.url})')

    def put_inline_code(self):
        self.add_page('`' + self.text + '`')

    def put_new_line(self):
        self.add_page('\n')

    def do_format(self, form):
        f = open('log.txt', 'a')
        f.write(f'form={form}')
        f.close()
        for x in Editor.formatters[form]:
            f = open('log.txt', 'a')
            f.write(f'x={x}')
            f.close()
            getattr(self, 'get_' + x)()
        getattr(self, 'put_' + form.replace('-','_'))()
        self.print_page()


    def start(self):
        while True:
            answer = input('Choose a formatter:')
            if answer == '!done':
                break
            if answer == '!help':
                print('Available formatters: ', ' '.join(Editor.formatters.keys()))
                print('Special commands: !help !done')
                continue
            if answer not in Editor.formatters.keys():
                print('Unknown formatting type or command')
                continue
            self.do_format(answer)


if __name__ == '__main__':
    editor = Editor()
    editor.start()