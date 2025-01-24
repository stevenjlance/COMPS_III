from library import *
import sqlite3
import os

# Test that the books table has been created
def test_books_table_exists():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'library.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='books';")
    result = cursor.fetchone()
    assert result is not None
    connection.close()

# Test that fiction holds all the books in the fiction genre
def test_fiction_genre():
    assert len(fiction) == 5
    assert fiction[0][1] == 'The Great Gatsby'

# Test that the Handmaids Tale has been updated to a publication year of 1985
def test_handmaids_tale_update():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'library.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    # Fetch the updated row
    updated = cursor.execute("SELECT * FROM books WHERE title = 'The Handmaids Tale';").fetchone()
    
    # Assert that the publication year is 1985
    assert updated[3] == 1985
    connection.close()

# Verify that 1984 has been deleted
def test_1984_deletion():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'library.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    # Attempt to fetch the deleted row
    deleted = cursor.execute("SELECT * FROM books WHERE title = '1984';").fetchone()
    
    # Assert that the row no longer exists
    assert deleted is None
    connection.close()

# Verify the table has 9 rows and that the rows have the correct values
def test_final_book_table_length():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'library.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    # Fetch all rows
    rows = cursor.execute("SELECT * FROM books;").fetchall()
    
    # Assert that there are 9 rows
    assert len(rows) == 9
    
    connection.close()


def test_final_books_table_contents():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'library.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    # Fetch all rows
    rows = cursor.execute("SELECT * FROM books;").fetchall()
    
    # Assert that the rows have the correct values
    expected_titles = [
        'The Great Gatsby',
        'To Kill a Mockingbird',
        'The Lord of the Rings',
        'The Catcher in the Rye',
        'One Hundred Years of Solitude',
        'The Hitchhikers Guide to the Galaxy',
        'The Handmaids Tale',
        'War and Peace',
        'Ulysses'
    ]
    
    actual_titles = [row[1] for row in rows]
    
    assert sorted(actual_titles) == sorted(expected_titles)
    
    connection.close()