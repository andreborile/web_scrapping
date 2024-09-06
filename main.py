import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://books.toscrape.com/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

data = []

all_books = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

for book in all_books:
    item = {}

    item['title'] = book.find('img').attrs['alt']
    item['link'] = 'https://books.toscrape.com/'+book.find('a').attrs['href']
    item['price'] = book.find('p', class_='price_color').text[2:]

    data.append(item)

print(item)
print(data)
df = pd.DataFrame(data)
df.to_excel('books.xlsx', index=False)