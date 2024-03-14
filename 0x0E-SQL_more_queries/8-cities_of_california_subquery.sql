-- SQL script that lists all the cities of California
-- that can be found in the database hbtn_0d_usa.
SELECT cities.id cities.name
FROM hbtn_0d_usa
ORDER BY cities.id  ASC
WHERE states.name = 'California';
