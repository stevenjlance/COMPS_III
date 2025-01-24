import sqlite3
import os

# Test that the users table has been created
def test_users_table_exists():
    """Verify that the users table exists in the database."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'python_pulse.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Check if users table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
    result = cursor.fetchone()
    assert result is not None, "Users table does not exist"
    
    connection.close()

# Test that the users table has the correct columns
def test_users_table_columns():
    """Verify the schema of the users table."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'python_pulse.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Get table info
    cursor.execute("PRAGMA table_info(users);")
    columns = cursor.fetchall()
    
    # Expected columns and their types
    expected_columns = [
        ('user_id', 'INTEGER', 1, None, 1),  # Primary key, autoincrement
        ('username', 'TEXT', 0, None, 0),
        ('password', 'TEXT', 0, None, 0),
        ('email', 'TEXT', 0, None, 0)
    ]
    
    # Check number of columns
    assert len(columns) == 4, f"Expected 4 columns, found {len(columns)}"
    
    # Check each column's details
    for expected, actual in zip(expected_columns, columns):
        assert actual[1] == expected[0], f"Column name mismatch: expected {expected[0]}, got {actual[1]}"
        assert actual[2] == expected[1], f"Column type mismatch for {actual[1]}"
        assert actual[5] == expected[4], f"Primary key configuration mismatch for {actual[1]}"
    
    connection.close()

# Test that the profile table has been created
def test_profiles_table_exists():
    """Verify that the profiles table exists in the database."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'python_pulse.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='profiles';")
    result = cursor.fetchone()
    assert result is not None, "Profiles table does not exist"
    
    connection.close()

# Test that the profiles table has the correct columns
def test_profiles_table_columns():
    """Verify the schema of the profiles table."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'python_pulse.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Get table info
    cursor.execute("PRAGMA table_info(profiles);")
    columns = cursor.fetchall()
    
    # Expected columns and their types
    expected_columns = [
        ('profile_id', 'INTEGER', 1, None, 1),  # Primary key, autoincrement
        ('user_id', 'INTEGER', 0, None, 0),
        ('height', 'INTEGER', 0, None, 0),
        ('weight', 'INTEGER', 0, None, 0),
        ('age', 'INTEGER', 0, None, 0),
        ('notes', 'TEXT', 0, None, 0)
    ]
    
    # Check number of columns
    assert len(columns) == 6, f"Expected 6 columns, found {len(columns)}"
    
    # Check each column's details
    for expected, actual in zip(expected_columns, columns):
        assert actual[1] == expected[0], f"Column name mismatch: expected {expected[0]}, got {actual[1]}"
        assert actual[2] == expected[1], f"Column type mismatch for {actual[1]}"
        assert actual[5] == expected[4], f"Primary key configuration mismatch for {actual[1]}"
    
    connection.close()

# Test that the foreign key constraint is set up correctly
def test_profiles_foreign_key():
    """Verify the foreign key constraint on user_id."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'python_pulse.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Check foreign key constraints
    cursor.execute("PRAGMA foreign_key_list(profiles);")
    foreign_keys = cursor.fetchall()
    
    assert len(foreign_keys) == 1, "Expected one foreign key constraint"
    
    foreign_key = foreign_keys[0]
    assert foreign_key[2] == 'users', "Foreign key should reference users table"
    assert foreign_key[3] == 'user_id', "Foreign key should reference user_id column"
    
    connection.close()

# Test that users data is inserted correctly
def test_users_data():
    """Verify the inserted users data."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'python_pulse.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Fetch all users
    cursor.execute("SELECT username, password, email FROM users ORDER BY username")
    users = cursor.fetchall()
    
    # Expected users data
    expected_users = [
        ('alice_jones', 'alicepassword', 'ajones@yahoo.com'),
        ('bob_brown', 'bobpassword', 'bobby@yahoo.com'),
        ('jane_smith', 'mypassword', 'jane@gmail.com'),
        ('john_doe', 'password123', 'john_doe@gmail.com'),
        ('rebecca_charles', 'rebeccapassword', 'becky123@gmail.com')
    ]
    
    assert len(users) == 5, "Expected 5 users"
    assert sorted(users) == expected_users, "Users data does not match expected values"
    
    connection.close()

# Test that profiles data is inserted correctly
def test_profiles_data():
    """Verify the inserted profiles data."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'python_pulse.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Fetch all profiles
    cursor.execute("SELECT user_id, height, weight, age, notes FROM profiles ORDER BY user_id")
    profiles = cursor.fetchall()
    
    # Expected profiles data
    expected_profiles = [
        (1, 180, 75, 28, 'Loves hiking and outdoor activities.'),
        (2, 165, 60, 25, 'Enjoys painting and art.'),
        (3, 170, 65, 30, 'Passionate about technology and coding.'),
        (4, 175, 80, 22, 'Avid reader and writer.'),
        (5, 160, 50, 27, 'Fitness enthusiast and gym lover.')
    ]
    
    assert len(profiles) == 5, "Expected 5 profiles"
    assert profiles == expected_profiles, "Profiles data does not match expected values"
    
    connection.close()

# Test that the goals table has been created
def test_goals_table_exists():
    """Verify that the goals table exists in the database."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'python_pulse.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='goals';")
    result = cursor.fetchone()
    assert result is not None, "Goals table does not exist"
    
    connection.close()

# Test that the goals table has the correct columns
def test_goals_table_columns():
    """Verify the schema of the goals table."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'python_pulse.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Get table info
    cursor.execute("PRAGMA table_info(goals);")
    columns = cursor.fetchall()
    
    # Expected columns and their types
    expected_columns = [
        ('goal_id', 'INTEGER', 1, None, 1),  # Primary key, autoincrement
        ('name', 'TEXT', 0, None, 0),
        ('target_value', 'INTEGER', 0, None, 0),
        ('user_id', 'INTEGER', 0, None, 0)
    ]
    
    # Check number of columns
    assert len(columns) == 4, f"Expected 4 columns, found {len(columns)}"
    
    # Check each column's details
    for expected, actual in zip(expected_columns, columns):
        assert actual[1] == expected[0], f"Column name mismatch: expected {expected[0]}, got {actual[1]}"
        assert actual[2] == expected[1], f"Column type mismatch for {actual[1]}"
        assert actual[5] == expected[4], f"Primary key configuration mismatch for {actual[1]}"
    
    connection.close()

# Test that the foreign key constraint is set up correctly
def test_goals_foreign_key():
    """Verify the foreign key constraint on user_id."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'python_pulse.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Check foreign key constraints
    cursor.execute("PRAGMA foreign_key_list(goals);")
    foreign_keys = cursor.fetchall()
    
    assert len(foreign_keys) == 1, "Expected one foreign key constraint"
    
    foreign_key = foreign_keys[0]
    assert foreign_key[2] == 'users', "Foreign key should reference users table"
    assert foreign_key[3] == 'user_id', "Foreign key should reference user_id column"
    
    connection.close()

# Test that goals data is inserted correctly
def test_goals_data():
    """Verify the inserted goals data."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'python_pulse.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Fetch all goals
    cursor.execute("SELECT name, target_value, user_id FROM goals ORDER BY goal_id")
    goals = cursor.fetchall()
    
    # Expected goals data
    expected_goals = [
        ('Run 5km', 5, 1),
        ('Lose 10kg', 10, 2),
        ('Lift 100kg 3x', 100, 3),
        ('Meditate daily', 1, 5),
        ('Cycle 100km', 100, 4),
        ('Complete a marathon', 42, 5),
        ('Run 5 km', 5, 5)
    ]
    
    assert len(goals) == 7, "Expected 7 goals"
    assert goals == expected_goals, "Goals data does not match expected values"
    
    connection.close()

# Test that the workouts table has been created
def test_workouts_table_exists():
    """Verify that the workouts table exists in the database."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'python_pulse.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='workouts';")
    result = cursor.fetchone()
    assert result is not None, "Workouts table does not exist"
    
    connection.close()

# Test that the user_workout table has been created
def test_user_workout_table_exists():
    """Verify that the user_workout table exists in the database."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'python_pulse.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='user_workout';")
    result = cursor.fetchone()
    assert result is not None, "User_workout table does not exist"
    
    connection.close()

## Test that the workouts table has the correct columns
def test_workouts_table_columns():
    """Verify the schema of the workouts table."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'python_pulse.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    cursor.execute("PRAGMA table_info(workouts);")
    columns = cursor.fetchall()
    
    expected_columns = [
        ('workout_id', 'INTEGER', 1, None, 1),
        ('name', 'TEXT', 0, None, 0),
        ('description', 'TEXT', 0, None, 0),
        ('duration', 'INTEGER', 0, None, 0)
    ]
    
    assert len(columns) == 4, f"Expected 4 columns, found {len(columns)}"
    
    for expected, actual in zip(expected_columns, columns):
        assert actual[1] == expected[0], f"Column name mismatch: expected {expected[0]}, got {actual[1]}"
        assert actual[2] == expected[1], f"Column type mismatch for {actual[1]}"
        assert actual[5] == expected[4], f"Primary key configuration mismatch for {actual[1]}"
    
    connection.close()

## Test that the user_workout table has the correct columns
def test_user_workout_table_columns():
    """Verify the schema of the user_workout table."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'python_pulse.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    cursor.execute("PRAGMA table_info(user_workout);")
    columns = cursor.fetchall()
    
    expected_columns = [
        ('user_id', 'INTEGER', 0, None, 0),
        ('workout_id', 'INTEGER', 0, None, 0)
    ]
    
    assert len(columns) == 2, f"Expected 2 columns, found {len(columns)}"
    
    for expected, actual in zip(expected_columns, columns):
        assert actual[1] == expected[0], f"Column name mismatch: expected {expected[0]}, got {actual[1]}"
        assert actual[2] == expected[1], f"Column type mismatch for {actual[1]}"
    
    connection.close()

# Test that the foreign key constraints are set up correctly
def test_user_workout_foreign_keys():
    """Verify foreign key constraints in user_workout table."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'python_pulse.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    cursor.execute("PRAGMA foreign_key_list(user_workout);")
    foreign_keys = cursor.fetchall()
    
    assert len(foreign_keys) == 2, "Expected two foreign key constraints"
    
    foreign_key_tables = {fk[2] for fk in foreign_keys}
    assert foreign_key_tables == {'users', 'workouts'}, "Foreign keys should reference users and workouts tables"
    
    connection.close()

# Test that workouts data is inserted correctly
def test_workouts_data():
    """Verify the inserted workouts data."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'python_pulse.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    cursor.execute("SELECT name, description, duration FROM workouts ORDER BY workout_id")
    workouts = cursor.fetchall()
    
    expected_workouts = [
        ('Morning Yoga', 'A refreshing morning yoga session.', 30),
        ('HIIT Workout', 'High-Intensity Interval Training.', 45),
        ('Weightlifting', 'Full body weightlifting session.', 60),
        ('Cycling', 'Outdoor cycling for endurance.', 120),
        ('Meditation', 'Guided meditation for relaxation.', 15)
    ]
    
    assert len(workouts) == 5, "Expected 5 workouts"
    assert workouts == expected_workouts, "Workouts data does not match expected values"
    
    connection.close()

# Test that user_workout data is inserted correctly
def test_user_workout_data():
    """Verify the inserted user_workout data."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'python_pulse.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    cursor.execute("SELECT user_id, workout_id FROM user_workout ORDER BY user_id, workout_id")
    user_workouts = cursor.fetchall()
    
    expected_user_workouts = [
        (1, 1),
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 1),
        (5, 2)
    ]
    
    assert len(user_workouts) == 7, "Expected 7 user_workout entries"
    assert user_workouts == expected_user_workouts, "User_workout data does not match expected values"
    
    connection.close()
