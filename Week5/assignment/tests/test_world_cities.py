import pytest
import sqlite3
from pathlib import Path

@pytest.fixture
def db():
    """Create a temporary in-memory database for testing"""
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Get the path to the SQL file in parent directory
    current_dir = Path(__file__).parent
    sql_path = current_dir.parent / 'world_cities.sql'
    
    # Read and execute the SQL file
    sql_file = sql_path.read_text()
    cursor.executescript(sql_file)
    
    yield conn
    
    # Cleanup
    conn.close()

def test_initial_cities_count(db):
    """Test that all initial cities were inserted correctly"""
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM cities")
    count = cursor.fetchone()[0]
    assert count == 7  # After DELETE operations

def test_japanese_cities(db):
    """Test that Japanese cities are correctly inserted and can be queried"""
    cursor = db.cursor()
    cursor.execute("SELECT name FROM cities WHERE country = 'Japan'")
    cities = cursor.fetchall()
    japanese_cities = {city[0] for city in cities}
    assert japanese_cities == {'Tokyo', 'Osaka'}

def test_beijing_population_update(db):
    """Test that Beijing's population was updated correctly"""
    cursor = db.cursor()
    cursor.execute("SELECT population FROM cities WHERE name = 'Beijing'")
    population = cursor.fetchone()[0]
    assert population == 1542000  # Updated population value

def test_deleted_cities(db):
    """Test that specified cities were deleted"""
    cursor = db.cursor()
    cursor.execute("SELECT name FROM cities WHERE name IN ('New York', 'Cairo', 'Paris')")
    deleted_cities = cursor.fetchall()
    assert len(deleted_cities) == 0

def test_remaining_cities_data(db):
    """Test the data integrity of remaining cities"""
    cursor = db.cursor()
    cursor.execute("SELECT name, population, country FROM cities ORDER BY name")
    cities = cursor.fetchall()
    
    expected_cities = [
        ('Beijing', 1542000, 'China'),
        ('Lagos', 14368332, 'Nigeria'),
        ('Mumbai', 12442373, 'India'),
        ('Osaka', 2752123, 'Japan'),
        ('Sao Paulo', 12252023, 'Brazil'),
        ('Sydney', 5312163, 'Australia'),
        ('Tokyo', 13515271, 'Japan')
    ]
    
    assert cities == expected_cities

def test_table_structure(db):
    """Test that the table structure is correct"""
    cursor = db.cursor()
    cursor.execute("PRAGMA table_info(cities)")
    columns = cursor.fetchall()
    
    expected_columns = [
        (0, 'id', 'INTEGER', 0, None, 1),
        (1, 'name', 'STRING', 0, None, 0),
        (2, 'population', 'INTEGER', 0, None, 0),
        (3, 'country', 'STRING', 0, None, 0)
    ]
    
    assert columns == expected_columns