# Import the requests, BeautifulSoup, sqlite3, and re modules
import requests
from bs4 import BeautifulSoup
import sqlite3
import re

connection = sqlite3.connect('movies.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    worldwide_gross INTEGER,
    year INTEGER
    );
''')

def scrape_wikipedia():
    response = requests.get("https://en.wikipedia.org/wiki/List_of_highest-grossing_films")
    webpage = BeautifulSoup(response.content, 'html.parser')
    table = webpage.find('table', class_='wikitable')
    rows = table.find_all('tr')
    table_data = []
    for row in rows:
        cells = row.find_all(['td', 'th'])  # Find all <td> and <th> elements
        cell_text = [cell.get_text(strip=True) for cell in cells]  # Extract and clean text
        table_data.append(cell_text)  # Append the row's text data to the list
    
    database_data = []
    for data in table_data[1:]:
        cleaned_str = re.sub(r'^(T\$|F\$|F8\$|\$)', '', data[3])
        cleaned_str = cleaned_str.replace(',', '')
        dict = {
            'title': data[2], 
            'worldwide_gross': int(cleaned_str),
            'year': data[4]
        }
        database_data.append(dict)

    return database_data


data_to_add = scrape_wikipedia()
for val in data_to_add:
    cursor.execute('''
        INSERT INTO movies (title, worldwide_gross, year)
        VALUES (?, ?, ?)
    ''', (val['title'], val['worldwide_gross'], val['year']))

# Get the values to confirm it works
data = cursor.execute('SELECT * from movies;')

for movie in data:
    print(movie)

# Don't delete this last line to ensure tests can pass
connection.commit()