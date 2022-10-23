import requests


def main():
    url = input('Input the URL:\n> ')
    quote = get_quote_from_url(url)
    print(quote or 'Invalid quote resource!')


def get_quote_from_url(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None

    return response.json().get('content')


if __name__ == '__main__':
    main()