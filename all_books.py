import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

all_books = []

for page in range(1, 51):
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.find_all('article', class_='product_pod')

    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text[2:]
        rating = book.p['class'][1]
        availability = book.find('p', class_='instock availability').text.strip()

        all_books.append({
            'Title': title,
            'Price (£)': float(price),
            'Rating': rating,
            'Availability': availability
        })

# Convert to DataFrame
df = pd.DataFrame(all_books)
df.to_csv('all_books.csv', index=False)
print(f'Successfully scraped {len(df)} books!')

