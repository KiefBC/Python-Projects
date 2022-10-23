# we were grabbing a hyperlink tag off a website based on an input
# this took me way too long
import requests

from bs4 import BeautifulSoup

user_input = int(input()) - 1  # since an index starts at 0
r = input()  # this is our URL input
r_request = requests.get(r)
selection = []  # empty list
soup = BeautifulSoup(r_request.content, 'html.parser')
find_input = soup.find_all('a')
# just going to add all the anchors to a list so we can iterate
for i in find_input:
    selection.append(i)
print(selection[user_input].get('href'))  # now print the href tag value #act2

# potentially a better way to do the inputs: act, url = int(input()), input()
# turn the soup and url input into one: soup = BeautifulSoup(requests.get(input()).content, 'html.parser')
# could have done varf = find_all() then create var = varf[user_input] instead of looping
# still need the get('href') to get the value of the tag
# could have just done: r = requests.get(input())

# same code as above, but 4 lines shorter
user_input = int(input()) - 1
r = requests.get(input())
soup = BeautifulSoup(r.content, 'html.parser')
find_input = soup.find_all('a')
find_input2 = find_input[user_input]
print(find_input2['href'])

# same code as above but only 3 lines
user_input = int(input()) - 1
soup = BeautifulSoup(requests.get(input()).content, 'html.parser').find_all('a')
print(soup[user_input].get('href'))
