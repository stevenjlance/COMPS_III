DROP TABLE IF EXISTS companies;
DROP TABLE IF EXISTS candidates;

CREATE TABLE companies (
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name STRING,
    industry STRING,
    location STRING
);

CREATE TABLE candidates (
    candidate_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name STRING,
    last_name STRING,
    email STRING,
    years_experience INTEGER,
    primary_skill STRING
);

INSERT INTO companies (company_name, industry, location) VALUES
    ('TechCorp', 'Software', 'San Francisco'),
    ('DataDynamics', 'Data Analytics', 'Boston'),
    ('CloudNine', 'Cloud Computing', 'Seattle');

INSERT INTO candidates (first_name, last_name, email, years_experience, primary_skill) VALUES
    ('John', 'Smith', 'john.smith@email.com', 5, 'Python'),
    ('Sarah', 'Johnson', 'sarah.j@email.com', 3, 'Data Science'),
    ('Michael', 'Lee', 'michael.lee@email.com', 7, 'Cloud Architecture'),
    ('Emma', 'Wilson', 'emma.w@email.com', 2, 'Frontend Development'),
    ('James', 'Brown', 'james.b@email.com', 4, 'Python');

-- Select all the values in the companies and candidates tables
SELECT "Company Table";
SELECT * FROM companies;
SELECT "";
SELECT "Candidate Table";
SELECT * FROM candidates;

-- Find Python developers
SELECT "";
SELECT "Python Developers";
SELECT * FROM candidates WHERE primary_skill = "Python";

-- Find Companies in the Software industry
SELECT "";
SELECT "Software Companies";
SELECT * FROM companies WHERE industry = "Software";

-- 3. Find all candidates with more than 3 years of experience
SELECT "";
SELECT "Candidates with more than 3 years of experience";
SELECT * FROM candidates WHERE years_experience > 3;

-- Update the email of a candidate
UPDATE candidates SET email = "john.smith@gmail.com" WHERE candidate_id = 1;
SELECT "";
SELECT "Updated Email for John Smith";
SELECT * FROM candidates WHERE candidate_id = 1;

-- Update a companies location and a candidates primary skill
UPDATE companies
SET location = 'New York'
WHERE company_name = 'TechCorp';

SELECT "";
SELECT "Updated Location for TechCorp";
SELECT * FROM companies WHERE company_name = 'TechCorp';

UPDATE candidates
SET primary_skill = 'Python, SQL'
WHERE candidate_id = 5;
SELECT "";
SELECT "Updated Primary Skill for James Brown";
SELECT * FROM candidates WHERE candidate_id = 5;

-- Delete a candidate and a company
DELETE FROM companies WHERE company_name = "CloudNine";
SELECT "";
SELECT "Deleted CloudNine Company";
SELECT * FROM companies;

-- Delete a candidate
DELETE FROM candidates WHERE primary_skill = "Cloud Architecture";
SELECT "";
SELECT "Deleted Michael Lee From Candidates";
SELECT * FROM candidates;