-- SQL script that lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id cities.name states.name
FROM hbtn_0d_usa
ORDER BY cities.id ASC;