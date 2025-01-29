import requests
from bs4 import BeautifulSoup
import sqlite3
import re
# 1. Import and install pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# # Code below is commented out as we can run it once to populate the database (i.e. what we did last week) and then the data will be present.
# # Connect to the books database
# connection = sqlite3.connect('books.db')
# cursor = connection.cursor()
# # cursor.execute("DROP TABLE IF EXISTS books")
# cursor.execute('''CREATE TABLE IF NOT EXISTS books(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title TEXT,
#     price REAL,
#     rating INTEGER,
#     availability TEXT,
#     genre TEXT
#     );
# ''')

# # Create a scrap_page function that will scrape the Books to Scrape website
# def scrape_pages(url, start, end):
#     books = []
#     for page in range(start, end + 1):
#         response = requests.get(BASE_URL.format(page))
#         webpage = BeautifulSoup(response.content, 'html.parser')
#         rating_dictionary = {'One': 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

#         genre_match = re.search(r'/category/books/([\w-]+)_\d+/', BASE_URL)
#         genre = genre_match.group(1).title()

#         book_elements = webpage.find_all('article', class_='product_pod')
#         for book in book_elements:
#             title = book.h3.a['title']
#             raw_price = book.find('p', class_="price_color").text
#             price = float(raw_price.strip('£'))
#             rating_class = book.find('p', class_='star-rating')['class'][1]
#             rating = rating_dictionary[rating_class]
#             availability = book.find('p', class_='instock availability').text.strip()
#             books.append([title, price, rating, availability, genre])
#     return books

# # Scrape the fiction page
# BASE_URL = "http://books.toscrape.com/catalogue/category/books/fiction_10/page-{}.html"
# books = scrape_pages("https://books.toscrape.com/catalogue/category/books/fiction_10/index.html", 1, 4)

# # Insert the values into the books database
# for book in books:
#     cursor.execute('''
#         INSERT INTO books (title, price, rating, availability, genre)
#         VALUES (?, ?, ?, ?, ?)
#     ''', (book[0], book[1], book[2], book[3], book[4]))

# # Commit the values
# connection.commit()

# 2. Connect to the database
connection = sqlite3.connect('books.db')

# 3. Load Data from SQLite
query = "SELECT * FROM books"
df = pd.read_sql_query(query, connection)
connection.close()

# 4. Print out the data frame to show the full table
print(df)

# Clean and Explore Data
# 5. Calculate the average rating
average_rating = df['rating'].mean().round(2)
print(f'Average Rating: {average_rating}')

# 6. Find the most common rating
most_common_rating = df['rating'].mode()[0]
print(f'Most common rating: {most_common_rating}')
# 7. Display basic statistics
print(df.describe())

# 8. Save the dataframe to a CSV file
df.to_csv('book_data.csv')

# Create Visualizations
# Create a bar plot of the count of books by rating
# 9. Count the number of each rating and then sort the values lowest to highest
rating_counts = df['rating'].value_counts().sort_index()
# 10. Format the figure size. This will carry over to the other figures
plt.figure(figsize=(8, 5)) 
# 11. Create a bar chart. The default value for .plot() is a line graph
rating_counts.plot(kind='bar')
# 12. Give the chart a title and label the x and y axis
plt.title('Count of Books by Rating')
plt.xlabel('Rating (Stars)')
plt.ylabel('Count')
# 13. Save the chart. You can also do .show() to show the graph but it will not save the file to your machine.
plt.savefig('bar_chart.png')

# Histogram: Price Distribution
# 14. Create a histogram. Include some additional styling as well
plt.hist(df['price'], color='skyblue', edgecolor='black')
plt.title('Price Distribution of Books')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.savefig('histogram.png')

# Scatter Plot: Price vs. Rating
# 15. Create a scatter plot of rating vs. price.
plt.scatter(df['rating'], df['price'])
plt.title('Price vs. Rating')
plt.xlabel('Rating (Stars)')
plt.ylabel('Price')
plt.savefig('Price_vs_Rating.png')
