import sqlite3
from python_pulse import *
import pytest

# test that that user table is created
def test_user_table_created():
    connection = sqlite3.connect('tech_talent.db')
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
    result = cursor.fetchone()
    assert result is not None
    connection.close()

# Test that profile table is created
def test_profile_table_created():
    connection = sqlite3.connect('tech_talent.db')
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='profiles';")
    result = cursor.fetchone()
    assert result is not None
    connection.close()

# Test that the user table has the correct columns
def test_user_table_columns():
    connection = sqlite3.connect('tech_talent.db')
    cursor = connection.cursor()
    cursor.execute("PRAGMA table_info(users);")
    columns = [column[1] for column in cursor.fetchall()]
    expected_columns = ['user_id', 'username', 'password', 'email']
    assert sorted(columns) == sorted(expected_columns)
    connection.close()

# Test that the profile table has the correct columns
def test_profile_table_columns():
    connection = sqlite3.connect('tech_talent.db')
    cursor = connection.cursor()
    cursor.execute("PRAGMA table_info(profiles);")
    columns = [column[1] for column in cursor.fetchall()]
    expected_columns = ['profile_id', 'user_id', 'height', 'weight', 'age', 'notes']
    assert sorted(columns) == sorted(expected_columns)
    connection.close()

# Test that user and profile table have one-to-one relationship
def test_one_to_one_relationship():
    connection = sqlite3.connect('tech_talent.db')
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM users;")
    user_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM profiles;")
    profile_count = cursor.fetchone()[0]
    assert user_count == profile_count
    connection.close()

# Test that you will get an error if you try to have multiple profiles for a user
def test_user_has_only_one_profile():
    connection = sqlite3.connect('tech_talent.db')
    cursor = connection.cursor()
    try:
        cursor.execute('''INSERT INTO profiles (user_id, height, weight, age, notes) VALUES
            (1, 180, 75, 28, 'Loves hiking and outdoor activities.');''')
        connection.commit()
        cursor.execute('''INSERT INTO profiles (user_id, height, weight, age, notes) VALUES
            (1, 165, 60, 25, 'Enjoys painting and art.');''')
        connection.commit()
    except sqlite3.IntegrityError:
        assert True
    finally:
        connection.close()

# Test that you goal table is created
def test_goal_table_created():
    connection = sqlite3.connect('tech_talent.db')
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='goals';")
    result = cursor.fetchone()
    assert result is not None
    connection.close()

# Test that the goal table has the correct columns
def test_goal_table_columns():
    connection = sqlite3.connect('tech_talent.db')
    cursor = connection.cursor()
    cursor.execute("PRAGMA table_info(goals);")
    columns = [column[1] for column in cursor.fetchall()]
    expected_columns = ['goal_id', 'name', 'target_value', 'user_id']
    assert sorted(columns) == sorted(expected_columns)
    connection.close()

# Test that user and goal table have one-to-many relationship
def test_one_to_many_relationship():
    connection = sqlite3.connect('tech_talent.db')
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM users;")
    user_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM goals;")
    goal_count = cursor.fetchone()[0]
    assert user_count < goal_count
    connection.close()

# Test that you will get an error if you try to have multiple goals for a user
def test_user_has_only_one_goal():
    connection = sqlite3.connect('tech_talent.db')
    cursor = connection.cursor()
    try:
        cursor.execute('''INSERT INTO goals (name, target_value, user_id) VALUES
            ('Run 5km', 5, 1);''')
        connection.commit()
        cursor.execute('''INSERT INTO goals (name, target_value, user_id) VALUES
            ('Lose 10kg', 10, 1);''')
        connection.commit()
    except sqlite3.IntegrityError:
        assert True
    finally:
        connection.close()

# Test that workout table is created
def test_workout_table_created():
    connection = sqlite3.connect('tech_talent.db')
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='workouts';")
    result = cursor.fetchone()
    assert result is not None
    connection.close()

# Test that the workout table has the correct columns
def test_workout_table_columns():
    connection = sqlite3.connect('tech_talent.db')
    cursor = connection.cursor()
    cursor.execute("PRAGMA table_info(workouts);")
    columns = [column[1] for column in cursor.fetchall()]
    expected_columns = ['workout_id', 'name', 'description', 'duration']
    assert sorted(columns) == sorted(expected_columns)
    connection.close()

# Test that user_workout table is created
def test_user_workout_table_created():
    connection = sqlite3.connect('tech_talent.db')
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='user_workout';")
    result = cursor.fetchone()
    assert result is not None
    connection.close()

# Test that the user_workout table has the correct columns
def test_user_workout_table_columns():
    connection = sqlite3.connect('tech_talent.db')
    cursor = connection.cursor()
    cursor.execute("PRAGMA table_info(user_workout);")
    columns = [column[1] for column in cursor.fetchall()]
    expected_columns = ['user_id', 'workout_id']
    assert sorted(columns) == sorted(expected_columns)
    connection.close()

import sqlite3
import pytest

@pytest.fixture
def setup_database():
    # Setup database and create tables
    connection = sqlite3.connect(":memory:")  # Use in-memory database for testing
    cursor = connection.cursor()

    # Create tables
    cursor.execute('''CREATE TABLE users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT
    );''')
    
    cursor.execute('''CREATE TABLE workouts (
        workout_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    );''')

    cursor.execute('''CREATE TABLE user_workout (
        user_id INTEGER,
        workout_id INTEGER,
        PRIMARY KEY (user_id, workout_id),
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (workout_id) REFERENCES workouts(workout_id)
    );''')

    # Insert sample data into users table
    cursor.executemany('INSERT INTO users (username) VALUES (?);', [
        ('john_doe',),
        ('jane_smith',),
        ('alice_jones',)
    ])

    # Insert sample data into workouts table
    cursor.executemany('INSERT INTO workouts (name) VALUES (?);', [
        ('Yoga',),
        ('HIIT',),
        ('Cycling',)
    ])

    # Insert sample data into user_workout table
    cursor.executemany('INSERT INTO user_workout (user_id, workout_id) VALUES (?, ?);', [
        (1, 1),
        (1, 2),
        (2, 2),
        (3, 1),
        (3, 3)
    ])

    connection.commit()
    yield connection  # Provide the connection to tests
    connection.close()

def test_users_associated_with_multiple_workouts(setup_database):
    connection = setup_database
    cursor = connection.cursor()

    # Query to check how many workouts are associated with user_id 1
    cursor.execute('SELECT workout_id FROM user_workout WHERE user_id = 1;')
    workouts = cursor.fetchall()
    assert len(workouts) == 2  # User 1 should have 2 workouts (Yoga and HIIT)
    assert set(workout[0] for workout in workouts) == {1, 2}

def test_workouts_associated_with_multiple_users(setup_database):
    connection = setup_database
    cursor = connection.cursor()

    # Query to check how many users are associated with workout_id 2
    cursor.execute('SELECT user_id FROM user_workout WHERE workout_id = 2;')
    users = cursor.fetchall()
    assert len(users) == 2  # Workout 2 (HIIT) should have 2 users (User 1 and User 2)
    assert set(user[0] for user in users) == {1, 2}