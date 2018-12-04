-- Lists all Cali cities that is in the database
SELECT cities.id, cities.name
FROM states, cities
WHERE states.name = 'California'
ORDER BY cities.id ASC;
