import json

import requests


class WebScraper:

    def __init__(self):
        self.url = None
        self.response = None
        self.hello_input = None

    def get_request(self):
        self.url = f'{self.hello_input}'
        self.response = requests.get(self.url).json()
        try:
            print(self.response['content'])
        except (KeyError, json.decoder.JSONDecodeError):
            print('\nInvalid quote resource!')

    def user_input(self):
        self.hello_input = input('Input the URL: \n')


def main():
    ws = WebScraper()
    ws.user_input()
    ws.get_request()


if __name__ == '__main__':
    main()
