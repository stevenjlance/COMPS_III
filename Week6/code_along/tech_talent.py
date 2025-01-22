# 2. At the top of the file, import the `sqlite3` module.
import sqlite3

# 3. Create a connection variable and call `.connect()` to connect to the `tech_talent.db` file.
connection = sqlite3.connect('tech_talent.db')

# 4. Create a cursor by calling `.cursor()` on the connection you created the previous step.
cursor = connection.cursor()

# 5. The `companies` and `candidates` tables may already exist in the database. Using `.execute()`, call the `DROP TABLE IF EXISTS` SQL command.
cursor.execute("DROP TABLE IF EXISTS companies;")
cursor.execute("DROP TABLE IF EXISTS candidates;")

# 6. Create the `companies` and `candidates` tables using `.execute()` and `CREATE TABLE`.
cursor.execute('''CREATE TABLE companies (
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name STRING,
    industry STRING,
    location STRING
);''')

cursor.execute('''CREATE TABLE candidates (
    candidate_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name STRING,
    last_name STRING,
    email STRING,
    years_experience INTEGER,
    primary_skill STRING
);''')

# 7. Insert values into the `companies` and `candidates` tables using `.execute()` and `INSERT INTO...VALUES`.
cursor.execute('''INSERT INTO companies (company_name, industry, location) VALUES
    ('TechCorp', 'Software', 'San Francisco'),
    ('DataDynamics', 'Data Analytics', 'Boston'),
    ('CloudNine', 'Cloud Computing', 'Seattle');
''')

cursor.execute('''INSERT INTO candidates (first_name, last_name, email, years_experience, primary_skill) VALUES
    ('John', 'Smith', 'john.smith@email.com', 5, 'Python'),
    ('Sarah', 'Johnson', 'sarah.j@email.com', 3, 'Data Science'),
    ('Michael', 'Lee', 'michael.lee@email.com', 7, 'Cloud Architecture'),
    ('Emma', 'Wilson', 'emma.w@email.com', 2, 'Frontend Development'),
    ('James', 'Brown', 'james.b@email.com', 4, 'Python');
''')

# 8. Using a `SELECT` command and `.execute()` get the data stored in each table. Call `.fetchall()` on the returned values. Print out the values in each table.
print("Companies Data:")
companies = cursor.execute("SELECT * FROM companies;").fetchall()
print(companies)
print("\nCandidates Data:")
candidates = cursor.execute("SELECT * FROM candidates;").fetchall()
print(candidates)

# Go to bash.sh file for syntax instructions

# 10. Print out the 2nd and 3rd candidates that were returned.
print(candidates[1:3])

# 11. What data type is in this list? Use `type()` command on the data that was returned to show that it is a tuple.
print(type(candidates[0]))

# 12. We can access values the exact same way we access values in a list. Print out the 2nd candidates name to show this.
print(f'{candidates[1][1]} {candidates[1][2]}')

# 13. Create a SQL query so that you can print out only candidates that have a primary skill of `"Python"`.
print("\nCandidates with Python skill:")
python_candidates = cursor.execute("SELECT * FROM candidates WHERE primary_skill = 'Python';").fetchall()
print(python_candidates)

# 14. Iterate through the data you got in the last step and print out candidates email that have Python has a skill.
print("\nCandidates with Python skill:")
python_candidates = cursor.execute("SELECT * FROM candidates WHERE primary_skill = 'Python';").fetchall()
for candidate in python_candidates:
    print(candidate[3])

# 15. Create a SQL query so that you can print out only the `companies` name that are in an `industry` of `"Software"`.
print("\nSoftware Companies:")
software_companies = cursor.execute("SELECT * FROM companies WHERE industry = 'Software';").fetchall()
for software_company in software_companies:
    print(software_company[1])

# 16. Create a SQL query so that you can print out only those `candidates` name and primary skill that have more than 3 years of experience.
print("\nCandidates with more than 3 years of experience:")
experienced_candidates = cursor.execute("SELECT * FROM candidates WHERE years_experience > 3;").fetchall()
for experienced_candidate in experienced_candidates:
    print(f'Name: {experienced_candidate[1]}')
    print(f'Primary Skill: {experienced_candidate[5]}')

# 17. Create a SQL query to update John's email to the correct value of `john.smith@gmail.com`.
print("\nUpdating John's email:")
cursor.execute("UPDATE candidates SET email = 'john.smith@gmail.com' WHERE candidate_id = 1;")

# 18. Update the candidate with a `candidate_id` of 5 wants to update their `primary_skill` to be `Python, SQL`
print("\nUpdating candidate_id 5's primary skill:")
cursor.execute("UPDATE candidates SET primary_skill = 'Python, SQL' WHERE candidate_id = 5;")

# 19. Print updated candidates table
print("\nUpdated Candidates Data:")
candidates = cursor.execute("SELECT * FROM candidates;").fetchall()
print(candidates)

# 20. Delete the 'Cloud Nine' row from the `companies` table.
print("\nDeleting 'Cloud Nine' company:")
cursor.execute("DELETE FROM companies WHERE company_name = 'Cloud Nine';")

# 21. Delete all `candidates` that have a `primary_skill` of `"Cloud Architecture"`. 
print("\nDeleting candidates with Cloud Architecture skill:")
cursor.execute("DELETE FROM candidates WHERE primary_skill = 'Cloud Architecture';")

# 22. Print out the remaining values in the `candidates` table. 
print("\nRemaining Companies Data:")
companies = cursor.execute("SELECT * FROM companies;").fetchall()
print(companies)

# 23. Close the connection.
connection.close()