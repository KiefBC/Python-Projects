import string
import requests
from bs4 import BeautifulSoup


# added BeautifulSoup back and combined it with Requests
# now we scrape a bunch of articles and save only the select few we want based on args
# combining everything from part 2 and 3 into a beautiful part 4

# # TODO: filename
# # article_filename = (articles.find('h3').text.replace('\n', '')).replace('’', '')
# for badthings in article_filename:
#     if badthings in string.punctuation:
#         article_filename = article_filename.replace(badthings, '')
# article_filename = article_filename.replace(' ', '_')

## TODO: file saving
# with open(f'{article_filename}.txt', 'wb') as file:
#     file.write(bytes(str(soup.title.text.strip(' ')), encoding='utf-8'))
#     file.write(bytes(str(soup.body.text.strip(' ')), encoding='utf-8'))

class WebScraper:

    def __init__(self):
        self.url = None
        self.response = None
        self.hello_input = None
        self.articles = []

    def get_request(self):
        self.url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'
        self.response = requests.get(self.url, headers={'Accept-Language': 'en-US,en;q=0.5'})

        # let's make sure we receive a 200 status_code
        if self.response.status_code == 200:
            soup = BeautifulSoup(self.response.content, 'html.parser')

            # this will select every article without prejudice and only the articles
            # CSS: all_articles = soup.find_all(class_="app-article-list-row__item")
            all_articles = soup.find_all("article")
            for article in all_articles:
                if article.find('span', class_="c-meta__type").text == "News":
                    main_link = 'https://www.nature.com'
                    article_link = article.find("a", {"data-track-action": "view article"}).get("href")
                    complete_link = main_link + article_link
                    self.articles.append(complete_link)
        return self.articles, self.url, self.response

    def article_filename(self):
        soup = BeautifulSoup(self.response.content, 'html.parser')
        unchanged_title = soup.find("h1", {"class": "c-article-magazine-title"}).text
        # creating a map of every char and removing any punctuation
        mapped_title = unchanged_title.maketrans("", "", string.punctuation + "’")
        # creating a string from our mapped object
        article_filename = unchanged_title.translate(mapped_title)
        article_filename = article_filename.strip().replace(" ", "_")
        return article_filename

    def user_input(self):
        # self.hello_input = input('Input the URL: \n')
        pass


def main():
    ws = WebScraper()
    ws.user_input()
    ws.get_request()


if __name__ == '__main__':
    main()
