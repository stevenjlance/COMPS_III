DROP TABLE IF EXISTS cities;

CREATE TABLE cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name STRING,
    population INTEGER,
    country STRING
);

INSERT INTO cities (name, population, country) VALUES
("New York", 8398745, "United States"),
("Tokyo", 13515271, "Japan"),
("Cairo", 9500000, "Egypt"),
("Sydney", 5312163, "Australia"),
("Sao Paulo", 12252023, "Brazil"),
("Paris", 2140526, "France"),
("Lagos", 14368332, "Nigeria"),
("Mumbai", 12442373, "India"),
("Osaka", 2752123, "Japan"),
("Beijing", 21542000, "China");

SELECT * FROM cities;

SELECT * FROM cities WHERE country = "Japan";

UPDATE cities SET population = 1542000 WHERE name = "Beijing"; 
SELECT * FROM cities WHERE name = "Beijing"; 

DELETE FROM cities WHERE name = "New York";
DELETE FROM cities WHERE name = "Cairo";
DELETE FROM cities WHERE name = "Paris";

SELECT * FROM cities;