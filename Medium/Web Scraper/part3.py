import requests

# we removed the beautifulsoup library
# now just scraping the data and saving if the GET was successful

class WebScraper:

    def __init__(self):
        self.url = None
        self.response = None
        self.hello_input = None
        self.request_dict = {}

    def get_request(self):
        self.url = f'{self.hello_input}'
        # could have .content this but then .status_code didn't work
        r = requests.get(self.url)
        # 200 means successful
        if r.status_code == 200:
            page_content = r.content
            # wb allows us to write in binary without encoding in UTF-8
            with open('source.html', 'wb') as file:
                file.write(page_content)
            print('Content saved.')
        else:
            print(f'The URL returned {r.status_code}!')

    def user_input(self):
        self.hello_input = input('Input the URL: \n')


def main():
    ws = WebScraper()
    ws.user_input()
    ws.get_request()


if __name__ == '__main__':
    main()
