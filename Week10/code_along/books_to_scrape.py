# Import the requests, BeautifulSoup, sqlite3, and re modules
import requests
from bs4 import BeautifulSoup
import sqlite3
import re

# Create a books database
connection = sqlite3.connect('books.db')
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS books")
cursor.execute('''CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    price REAL,
    rating INTEGER,
    availability TEXT,
    genre TEXT
    );
''')

# Create a scrap_page function that will scrape the Books to Scrape website
def scrape_pages(url, start, end):
    books = []
    # iterate through pages 1 through 4 (the number of fiction pages that there are)
    for page in range(start, end + 1):
        response = requests.get(BASE_URL.format(page))
        webpage = BeautifulSoup(response.content, 'html.parser')
        rating_dictionary = {'One': 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

        # The genre is in the url. This looks for the /category/books raw string. 
        # ([\w]+) Captures the category name (letters, numbers, hyphens).
        # _ Matches the underscore character
        # \d+ matches one ore more digit
        # /index.html matches the literal text
        genre_match = re.search(r'/category/books/([\w-]+)_\d+/', BASE_URL)
        # We use group(1) because we want just the capturing group (i.e. the think in ([\w]+) ), not the whole regex search.
        genre = genre_match.group(1).title()

        # Every book is in "article" element with a class of "product_pod".
        book_elements = webpage.find_all('article', class_='product_pod')
        # Iterate through all of these book elements and pull out the book information
        for book in book_elements:
            # Title is inside an h3 element. Note that some of the titles are incomplete but the anchor has the title as "title"
            title = book.h3.a['title']
            # There are multiple paragraphs, so do find with the class name
            raw_price = book.find('p', class_="price_color").text
            # Remove the currency and convert to float
            price = float(raw_price.strip('£'))
            # The rating class has the ratings for the book. The rating is stored as the second class name
            rating_class = book.find('p', class_='star-rating')['class'][1]
            # Convert the rating to an int using a dictionary
            rating = rating_dictionary[rating_class]
            # Get the availability and strip extra whitespace
            availability = book.find('p', class_='instock availability').text.strip()
            # Add all the content to the growing books list
            books.append([title, price, rating, availability, genre])
    return books

# Scrape the fiction page
BASE_URL = "http://books.toscrape.com/catalogue/category/books/fiction_10/page-{}.html"

books = scrape_pages("https://books.toscrape.com/catalogue/category/books/fiction_10/index.html", 1, 4)

# Insert the values into the books database
for book in books:
    cursor.execute('''
        INSERT INTO books (title, price, rating, availability, genre)
        VALUES (?, ?, ?, ?, ?)
    ''', (book[0], book[1], book[2], book[3], book[4]))

# Commit the values
connection.commit()

# Get the values to confirm it works
data = cursor.execute('SELECT * from books;')

for book in data:
    print(book)