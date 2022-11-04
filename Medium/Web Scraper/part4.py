import string
import requests
from bs4 import BeautifulSoup


# added BeautifulSoup back and combined it with Requests
# now we scrape a bunch of articles and save only the select few we want based on args
# combining everything from part 2 and 3 into a beautiful part 4

# TODO: file saving
# with open(f'{article_filename}.txt', 'wb') as file:
#     file.write(bytes(str(soup.title.text.strip(' ')), encoding='utf-8'))
#     file.write(bytes(str(soup.body.text.strip(' ')), encoding='utf-8'))
# TODO: letting us know we saved
# TODO: showing us the location
# TODO: what happens when wrong code
# TODO: count pages

class WebScraper:

    def __init__(self):
        self.url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'
        self.response = None
        self.hello_input = None
        self.articles = []
        self.article_filename = None
        self.article_content = None
        self.article_title = None

    def get_request(self, url):
        # we speak English, not Spanish
        return requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})

    def get_links(self, url):
        response = self.get_request(url)
        # let's make sure we receive a 200 status_code
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # this will select every article without prejudice and only the articles
            # CSS: all_articles = soup.find_all(class_="app-article-list-row__item")
            all_articles = soup.find_all("article")
            for article in all_articles:
                if article.find('span', class_="c-meta__type").text == "News":
                    main_link = 'https://www.nature.com'
                    article_link = article.find("a", {"data-track-action": "view article"}).get("href")
                    complete_link = main_link + article_link
                    self.articles.append(complete_link)

        return self.articles

    def article_filename(self):
        soup = BeautifulSoup(self.response.content, 'html.parser')
        unchanged_title = soup.find("h1", {"class": "c-article-magazine-title"}).text
        # creating a map of every char and removing any punctuation
        mapped_title = unchanged_title.maketrans("", "", string.punctuation + "’")
        # creating a string from our mapped object
        article_filename = unchanged_title.translate(mapped_title)
        self.article_filename = article_filename.strip().replace(" ", "_")
        # call our saving function
        self.save_article(self.url)

    def get_content(self, url):
        soup = BeautifulSoup(self.get_request(url), 'html.parser')
        self.article_content = soup.find("div", {"class": "c-article-body"}).get_text().strip()
        return self.article_content

    def save_article(self, url):
        article_content = self.get_content(url)
        title = self.article_filename(url)
        file_name = title + ".txt"
        with open(file_name, "wb") as file:
            content_in_byte = bytes(article_content, "utf-8")
            file.write(content_in_byte)

    def user_input(self):
        # normally this would be an input for the user
        self.url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'
        return self.get_links(self.url)


def main():
    ws = WebScraper()
    ws.user_input()


if __name__ == '__main__':
    main()
