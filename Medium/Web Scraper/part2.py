import requests
import json
from bs4 import BeautifulSoup


class WebScraper:

    def __init__(self):
        self.url = None
        self.response = None
        self.hello_input = None
        self.request_dict = {}

    def get_request(self):
        self.url = f'{self.hello_input}'
        try:
            # headers forces the request library to parse in English only - or whatever we want
            self.response = requests.get(self.url, headers={'Accept-Language': 'en-US,en;q=0.5'})
            soup = BeautifulSoup(self.response.content, 'html.parser')
            title = soup.find('h1', {'class': 'TitleHeader__TitleText-sc-1wu6n3d-0'}).get_text()
            description = soup.find('span', {'data-testid': 'plot-l'}).get_text()
            self.request_dict = {'title': title, 'description': description}
            print(self.request_dict)
        except AttributeError:
            print('\nInvalid movie page!')
        return self.request_dict


    def user_input(self):
        self.hello_input = input('Input the URL: \n')


def main():
    ws = WebScraper()
    ws.user_input()
    ws.get_request()


if __name__ == '__main__':
    main()
