import psycopg2
try:
    # Connect to postgres database in container
    connection = psycopg2.connect(user = "postgres",
                                 # password = "NEW_PASSWORD",
                                  host = "localhost",
                                  port = 54320,
                                  database = "db")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    # Returns an error if unable to connect
    print ("Error while connecting to PostgreSQL", error)

 
#to query
# SQL Query; Use inner join to join the various tables
cursor.execute("SELECT actor.actor_id, actor.first_name, actor.last_name, \
    film_actor.film_id, film.title, film.description, film.release_year \
    FROM film \
        INNER JOIN film_actor ON film_actor.film_id = film.film_id \
        INNER JOIN actor ON film_actor.actor_id = actor.actor_id ")
# cursor.execute("SELECT * from actor LIMIT 10")
rows = cursor.fetchmany(10)
print("\nShow me the databases:\n")
for row in rows:
    print("ACTOR_ID:   ", row[0])
    print("FIRST_NAME:   ", row[1])
    print("LAST_NAME:    ", row[2])
    print("FILM_ID:   ", row[3])
    print("TITLE:   ", row[4])
    print("DESCRIPTION:   ", row[5])
    print("RELEASE_YEAR:   ", row[6], "\n")