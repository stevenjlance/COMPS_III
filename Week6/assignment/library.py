import sqlite3

connection = sqlite3.connect('library.db')

# Lets you execute SQL commands
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS books;")

cursor.execute("""CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title STRING,
    author STRING,
    publication_year INTEGER,
    genre STRING
);""")

cursor.execute("""INSERT INTO books (title, author, publication_year, genre) VALUES
('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Fiction'),
('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
('1984', 'George Orwell', 1949, 'Dystopian Fiction'),
('The Lord of the Rings', 'J.R.R. Tolkien', 1954, 'Fantasy'),
('The Catcher in the Rye', 'J.D. Salinger', 1951, 'Fiction'),
('One Hundred Years of Solitude', 'Gabriel Garcia Marquez', 1967, 'Magical Realism'),
('The Hitchhikers Guide to the Galaxy', 'Douglas Adams', 1979, 'Science Fiction'),
('The Handmaids Tale', 'Margaret Atwood', 1980, 'Dystopian Fiction'),
('War and Peace', 'Leo Tolstoy', 1869, 'Fiction'),
('Ulysses', 'James Joyce', 1922, 'Fiction');
""")

test_data = cursor.execute("SELECT * FROM books;").fetchall()
print(test_data)

fiction = cursor.execute("SELECT * FROM books WHERE genre = 'Fiction';").fetchall()

# Update the Handmaids Tale to a publication date of 1985.
cursor.execute("UPDATE books SET publication_year = 1985 WHERE title = 'The Handmaids Tale';")

# Delete War and Peace
cursor.execute("DELETE FROM books WHERE title = '1984';")

# This needs to be the last line of the file for the tests to work!
connection.commit()