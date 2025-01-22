# Code Demo Instructions

## Overview

Last week we created `candidates` and `companies` databases using SQL for our Tech Talent recruiting firm. This week, we'll be taking that file and converting it into a Python file using the `sqlite3` module. You don't need to install sqlite3 separately as it comes pre-installed with Python! The values that will be stored in each of these tables are represented in the entity diagrams shown below (this is the same as last week).

![ER Diagram](Recruiting_W2.png)

By the end of this code along, our recruiting firm will be able to store information in a Python file so that it can be manipulated and utilized as part of a broader program.

> This week’s code utilizes SQLite3 to implement the commands. This should have been installed last week, but here are the directions again if needed:
> - **Windows**: [Follow these directions](https://www.tutorialspoint.com/sqlite/sqlite_installation.htm).
> - **Apple**: Nothing at all! SQLite comes installed on all Macs. If for some reason you don’t have it, you can download it using [Homebrew](https://formulae.brew.sh/formula/sqlite).
> - **Linux**: Follow [these directions](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-sqlite-on-ubuntu-20-04).

## Local Terminal - bash.sh has syntax instructions
1. Navigate to the folder you created last week and create one python file. Open the `tech_talent.python` python file. 

## VS Code - tech_talent.python has syntax instructions
2. At the top of the file, import the `sqlite3` module.
3. Create a connection variable and call `.connect()` to connect to the `tech_talent.db` file.
4. Create a cursor by calling `.cursor()` on the connection you created the previous step.
5. The `companies` and `candidates` tables may already exist in the database. Using `.execute()`, call the `DROP TABLE IF EXISTS` SQL command.
6. Create the `companies` and `candidates` tables using `.execute()` and `CREATE TABLE`.
7. Insert values into the `companies` and `candidates` tables using `.execute()` and `INSERT INTO...VALUES`.
8. Using a `SELECT` command and `.execute()` get the data stored in each table. Call `.fetchall()` on the returned values. Print out the values in each table.

## Local Terminal - bash.sh has syntax instructions
9. In the directory, run the command `python3 tech_talent.py` in the terminal and observe the output. You should run this after every few commands after this to verify you don't have any syntax errors and to model debugging if you do!

## VS Code - tech_talent.python has syntax instructions
10. Print out the 2nd and 3rd candidates that were returned.
11. What data type is in this list? Use `type()` command on the data that was returned to show that it is a tuple.
12. We can access values the exact same way we access values in a list. Print out the 2nd candidates name to show this.
13. Create a SQL query so that you can print out only candidates that have a primary skill of `"Python"`.
14. Iterate through the data you got in the last step and print out candidates email that have Python has a skill.
15. Create a SQL query so that you can print out only the `companies` name that are in an `industry` of `"Software"`.
16. Create a SQL query so that you can print out only those `candidates` name and primary skill that have more than 3 years of experience.
17. Create a SQL query to update John's email to the correct value of `john.smith@gmail.com`.
18. Update the candidate with a `candidate_id` of 5 wants to update their `primary_skill` to be `Python, SQL`
19. Print updated candidates table
20. Delete the 'Cloud Nine' row from the `companies` table.
21. Delete all `candidates` that have a `primary_skill` of `"Cloud Architecture"`. 
22. Print out the remaining values in the `candidates` table. 
23. Close the connection