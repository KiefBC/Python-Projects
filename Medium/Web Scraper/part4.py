import string
import requests
from bs4 import BeautifulSoup


# added BeautifulSoup back and combined it with Requests
# now we scrape a bunch of articles and save only the select few we want based on args
# combining everything from part 2 and 3 into a beautiful part 4

class WebScraper:

    def __init__(self):
        self.url = None
        self.response = None
        self.hello_input = None
        self.articles = []

    def get_request(self):
        # self.url = f'{self.hello_input}'
        self.url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'
        self.response = requests.get(self.url, headers={'Accept-Language': 'en-US,en;q=0.5'})
        soup = BeautifulSoup(self.response.content, 'html.parser')
        # this will select every article without prejudice and only the articles
        all_articles = soup.find_all(class_="app-article-list-row__item")
        for i in all_articles:
            # first lets find which articles we care about
            if i.find('span', class_="c-meta__type").text == "News":
                article_filename = (i.find('h3').text.replace('\n', '')).replace('’', '')
                # you can't save a file on your computer with a "?" in the name
                # for this we import the Strings library and use the punctuation method
                for badthings in article_filename:
                    if badthings in string.punctuation:
                        article_filename = article_filename.replace(badthings, '')
                article_filename = article_filename.replace(' ', '_')

                # article_type = i.find('span', class_='c-meta__type').text
                # article_link = i.find('a', href=True)['href']
                # lets create a tuple of this information
                # self.articles.append((article_filename, article_type, article_link))
                # now we save the actual article content
                # r_article = requests.get('https://www.nature.com'+article_link)
                # soup_article = BeautifulSoup(r_article.content, 'html.parser')
                with open(f'{article_filename}.txt', 'wb') as file:
                    file.write(bytes(str(soup.title.text.strip(' ')), encoding='utf-8'))
                    file.write(bytes(str(soup.body.text.strip(' ')), encoding='utf-8'))

    def user_input(self):
        # self.hello_input = input('Input the URL: \n')
        pass


def main():
    ws = WebScraper()
    ws.user_input()
    ws.get_request()


if __name__ == '__main__':
    main()
