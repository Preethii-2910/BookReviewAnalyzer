# BookReviewAnalyzer
Web scraping and analysis of book data using Python
=======
# Book Review Analyzer

## Project Overview 
This project demonstrates my Python skills for web-scraping, data cleaning, website analysis, and generating visual insights with tools like matplotlib and seaborn.

---

# Tools and Technologies :
- Python 3
- BeautifulSoup
- Pandas
- matplotlib
- seaborn
- PyCharm IDE

---

## Project Structure :
- 'scrape_books.py' : Scrapes a single page of book data from the browser.
- 'all_books.py' : Scrapes all 50 pages (1000 books in total) of the webpage.
- 'analyze_books.py' : Performs analysis and visualizations, gathers key business statistics and insights which includes Name of the Book, Book Rating, Availability of the book(In-stock or out of stock), Price of the Book.
- 'all_books.csv' : Final dataset with Book Name, Book Availability, Book Price and Book Rating.

---

## Features And Insights

### 1) Web Scraping : 
- Extracts :
 - Book title
 - Price (in £)
 - Rating (Converted from words to numbers['One' as 1 'Two' as 2])
 - Availability (In stock or Out of Stock).
 - Scraped website : [http://books.toscrape.com] (http://books.toscrape.com)

### 2) Data Analysis :
- Total books in the website : 1000
- Average book price using mean
- Cheapest/ Most expensive book
- Rating distribution (1-5)
- Book Availability (In-stock or Out-of stock).

### 3) Data Visualization :
- Bar Chart : Rating distribution is defined
- Pie Chart : Availability of books (In-stock/Out-of stock).
- Histogram : Price distribution is defined.

---


## Visual Output (screenshots):
![Screenshot (256).png](..%2F..%2F..%2FOneDrive%2FPictures%2FScreenshots%2FScreenshot%20%28256%29.png)


![Screenshot (257).png](..%2F..%2F..%2FOneDrive%2FPictures%2FScreenshots%2FScreenshot%20%28257%29.png)


![Screenshot (258).png](..%2F..%2F..%2FOneDrive%2FPictures%2FScreenshots%2FScreenshot%20%28258%29.png)

---

## Errors and Fixes faced : 
- 'KeyError' : 'Price(£)' - Fixed by matching exact column name.
- `tight_layout('string')`- Removed argument, used `tight_layout()` correctly
- Palette warning in seaborn - Used`'hue='Rating'`
- Graphs not showing together - Learned to close each `plt.show()` window.

---

## What I learned :
- Navigating real HTML with BeautifulSoup.
- Data frame creation and manipulation with pandas.
- Build informative visualizations using matplotlib and seaborn
- Debugging and handling real-world issues during development.

---

## Future Improvements :
- Add interactive dashboard.
- Include books genre/ category and Author names data if available.

---

## Author :
**Preethi V**

Data Enthusiast

This is the first project in my Python project series.


