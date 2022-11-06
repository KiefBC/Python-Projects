import requests
from bs4 import BeautifulSoup
import string


def get_website(target):
    # we speak English, not Spanish
    return requests.get(target, headers={'Accept-Language': 'en-US,en;q=0.5'})


def get_news_article_link(article_link):
    # our first func call
    site = get_website(article_link)
    news_articles_link = []
    if site.status_code != 200:
        return site.status_code, news_articles_link
    soup = BeautifulSoup(site.content, "html.parser")
    # let's grab all the articles in one go, no prejudice
    all_articles = soup.find_all("article")
    # now let's iterate through them all
    for article in all_articles:
        article_span = article.find("span", {"data-test": "article.type"})
        article_type = article_span.find("span").text
        if article_type == "News":
            # start the creation of our article URL
            main_link = "https://www.nature.com"
            # grab all "a" tags with the "view article" string and grab the "href" of this selection
            article_link = article.find("a", {"data-track-action": "view article"}).get("href")
            complete_link = main_link + article_link
            news_articles_link.append(complete_link)

    return site.status_code, news_articles_link


def get_article_title(article_link):
    soup = BeautifulSoup(get_website(article_link).content, "html.parser")

    raw_title = soup.find("h1", {"class": "c-article-magazine-title"}).text
    # we are removing all punctuations and mapping a string
    table = raw_title.maketrans("", "", string.punctuation + "’")
    # translating the mapped object back into a string
    title = raw_title.translate(table)
    title = title.strip().replace(" ", "_")

    return title


def get_article_content(article_link):
    soup = BeautifulSoup(get_website(article_link).content, "html.parser")
    article_content = soup.find("div", {"class": "c-article-body"}).get_text().strip()

    return article_content


def save_article(article_link):
    title = get_article_title(article_link)
    article_content = get_article_content(article_link)

    file_name = title + ".txt"
    with open(file_name, "wb") as file:
        content_in_byte = bytes(article_content, "utf-8")
        file.write(content_in_byte)

    return title


url_in = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"

website_code, article_links = get_news_article_link(url_in)

if website_code == 200:
    saved_article = []

    for link in article_links:
        saved_title = save_article(link)
        saved_article.append(saved_title)
        print("Article downloaded:", saved_title)

    print("\nDownloaded article: ")
    for i in range(len(saved_article)):
        print(str(i + 1) + ". " + saved_article[i])
else:
    print("Invalid URL. Status code:", website_code)