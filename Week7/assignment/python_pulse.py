import sqlite3
import pytest

connection = sqlite3.connect('tech_talent.db')
cursor = connection.cursor()

# Drop tables if they exist
cursor.execute("DROP TABLE IF EXISTS users;")
cursor.execute("DROP TABLE IF EXISTS profiles;")
cursor.execute("DROP TABLE IF EXISTS goals;")
cursor.execute("DROP TABLE IF EXISTS workouts;")

# Create User and Profile tables
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    email TEXT
);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS profiles (
    profile_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    height INTEGER,
    weight INTEGER,
    age INTEGER,
    notes TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);''')

# Insert sample data
cursor.execute('''INSERT INTO users (username, password, email) VALUES
    ('john_doe', 'password123', 'john_doe@gmail.com'),
    ('jane_smith', 'mypassword', 'jane@gmail.com'),
    ('alice_jones', 'alicepassword', 'ajones@yahoo.com'),
    ('bob_brown', 'bobpassword', 'bobby@yahoo.com'),
    ('rebecca_charles', 'rebeccapassword', 'becky123@gmail.com');
''')

cursor.execute('''INSERT INTO profiles (user_id, height, weight, age, notes) VALUES
    (1, 180, 75, 28, 'Loves hiking and outdoor activities.'),
    (2, 165, 60, 25, 'Enjoys painting and art.'), 
    (3, 170, 65, 30, 'Passionate about technology and coding.'),
    (4, 175, 80, 22, 'Avid reader and writer.'),
    (5, 160, 50, 27, 'Fitness enthusiast and gym lover.');
''')

# Create goals tables
cursor.execute('''CREATE TABLE IF NOT EXISTS goals (
    goal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    target_value INTEGER,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);''')

# Create sample workout goals
cursor.execute('''INSERT INTO goals (name, target_value, user_id) VALUES
    ('Run 5km', 5, 1),
    ('Lose 10kg', 10, 2),
    ('Lift 100kg 3x', 100, 3),
    ('Meditate daily', 1, 5),
    ('Cycle 100km', 100, 4),
    ('Complete a marathon', 42, 5),
    ('Run 5 km', 5, 5);
''')

# Create workout table that a user can take. Many users can take a workout
cursor.execute('''CREATE TABLE IF NOT EXISTS workouts (
    workout_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    duration INTEGER
);''')

# Create intermediate user_workout table to establish many-to-many relationship
cursor.execute('''CREATE TABLE IF NOT EXISTS user_workout (
    user_id INTEGER,
    workout_id INTEGER,
    PRIMARY KEY (user_id, workout_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (workout_id) REFERENCES workouts(workout_id)
);''')

# Commit the changes and close the connection
connection.commit()