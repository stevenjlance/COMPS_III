import sqlite3
import os

def test_cities_table_exists():
    """Verify that the cities table exists in the database."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'world_cities.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Check if users table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='cities';")
    result = cursor.fetchone()
    assert result is not None, "Cities table does not exist"
    
    connection.close()

def test_cities_table_columns():
    """Verify the schema of the users table."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'world_cities.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Get table info
    cursor.execute("PRAGMA table_info(cities);")
    columns = cursor.fetchall()
    print(columns)
    
    # Expected columns and their types
    expected_columns = [
        (0, 'id', 'INTEGER', 0, None, 1),
        (1, 'name', 'TEXT', 0, None, 0),
        (2, 'population', 'INTEGER', 0, None, 0),
        (3, 'country', 'TEXT', 0, None, 0)
    ]
    
    # Check number of columns
    assert len(columns) == 4, f"Expected 4 columns, found {len(columns)}"
    
    # Check each column's details
    for expected, actual in zip(expected_columns, columns):
        assert actual[1] == expected[1], f"Column name mismatch: expected {expected[1]}, got {actual[1]}"
        assert actual[2].upper() == expected[2], f"Column type mismatch for {actual[1]}: expected {expected[2]}, got {actual[2]}"
        assert actual[5] == expected[5], f"Primary key configuration mismatch for {actual[1]}: expected {expected[5]}, got {actual[5]}"
    
    connection.close()

def test_beijing_population_update():
    """Test that Beijing's population was updated correctly"""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'world_cities.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("SELECT population FROM cities WHERE name = 'Beijing'")
    population = cursor.fetchone()[0]
    assert population == 19400000  # Updated population value

def test_deleted_cities():
    """Test that specified cities were deleted"""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'world_cities.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM cities WHERE name IN ('New York', 'Cairo', 'Paris')")
    deleted_cities = cursor.fetchall()
    assert len(deleted_cities) == 0

def test_final_cities_count():
    """Test that all initial cities were inserted correctly"""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'world_cities.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM cities")
    count = cursor.fetchone()[0]
    assert count == 7  # After DELETE operations

def test_remaining_cities():
    """Test the data integrity of remaining cities"""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'world_cities.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("SELECT name, population, country FROM cities ORDER BY name")
    cities = cursor.fetchall()
    
    expected_cities = [
        ('Beijing', 19400000, 'China'),
        ('Lagos', 14368332, 'Nigeria'),
        ('Mumbai', 12442373, 'India'),
        ('Osaka', 2752123, 'Japan'),
        ('Sao Paulo', 12252023, 'Brazil'),
        ('Sydney', 5312163, 'Australia'),
        ('Tokyo', 13515271, 'Japan')
    ]
    
    assert cities == expected_cities