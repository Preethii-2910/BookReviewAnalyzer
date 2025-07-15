import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://books.toscrape.com/catalogue/page-1.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all('article', class_='product_pod')

data = []

for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text[2:]
    rating = book.p['class'][1]
    availability = book.find('p', class_='instock availability').text.strip()

    data.append({
        'Title' : title,
        'Price' : float(price),
        'Rating' : rating,
        'Availability' : availability
    })

df = pd.DataFrame(data)
print(df.head())

df.to_csv('books_page1.csv', index=False)