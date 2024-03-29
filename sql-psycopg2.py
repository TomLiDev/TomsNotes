import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1
# cursor.execute('SELECT * FROM "Artist"')

# Query 2
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - select all tracks where the composer is "Queen" from the "Track"
# table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Aerosmith"])

# fetch the results (multiple)
results = cursor.fetchall()


connection.close()


for result in results:
    print(result)
