#   Task 5
****
##  Task5A
### 1. Pull the Postgres imge from DockerHub
-   Go to the [Postgres DockerHub page](https://hub.docker.com/_/postgres)
-   In a Terminal, enter the following command line:
    `docker pull postgres`

### 2. Clone the DB scripts from GitHub
-   Go to the [Sakila Database](https://github.com/jOOQ/jOOQ/tree/master/jOOQ-examples/Sakila/postgres-sakila-db) on GitHub
-   Clone the jOOQ repo onto local machine
    `git clone https://github.com/jOOQ/jOOQ.git`
-   Extract out the Sakila DB from local repository. Navigate to Sakila postgres folder and copy schema and data-insert into a separate folder. The SQL files are located in ~\jOOQ\jOOQ-examples\Sakila\postgres-sakila-db

### 3. Run the SQL scripts to create a database and insert rows
-   `cd` to the folder you've copied the schema and indert-data SQL files
-   Start the Postgres container using the `docker run` command
    `docker run --rm [CONTAINER_NAME] -d -p 54320:4532 -v /var/lib/postgresql/data  postgres`
-   Create a database in the container
    ```    
    docker exec -it [CONTAINER_NAME] psql -U postgres
    postgres=# CREATE DATABASE db
    postgres=# quit
    ```
-   Copy the Sakila schema and insert-data SQL files into the container
    For schema: `docker cp ./postgres-sakila-schema.sql [CONTAINER_NAME]:/postgres-sakila-schema.sql` <br />
    For insert-data: `docker cp ./postgres-sakila-insert-data.sql [CONTAINER_NAME]:/postgres-sakila-insert-data.sql`

-   Execute the SQL files in the container. Execute the schema first then populate with data.
    Execute the schema SQL: `docker exec -it [CONTAINER_NAME] psql -U postgres -a db -f /postgres-sakila-schema.sql` <br />
    Execute the data SQL:`docker exec -it [CONTAINER_NAME] psql -U postgres -a db -f /postgres-sakila-insert-data.sql`

****
##  Task 5B
### Provide a code segment in Python to query database
Using the database created in Task 5A, provide a code segment in Python to :
1. Combine the tables **actor**, **film_actor**, and **film**
2. Query the first 10 rows of **ACTOR_ID, FIRST_NAME, LAST_NAME, FILM_ID, TITLE, DESCRIPTION** and **RELEASE_YEAR**

-   Create a Python file and open in a code editor
-   Enter the following:
    ```
    # Import PostgreSQL database adapter for Python programming
        import psycopg2
    try:
    # Connect to postgres database in container
        connection = psycopg2.connect(user = "postgres",
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
        print ("Error while connecting to PostgreSQL", error)


    #Use SQL features to combine tables using INNER JOIN and select columns using SELECT
    cursor.execute("SELECT actor.actor_id, actor.first_name, actor.last_name, \
    film_actor.film_id, film.title, film.description, film.release_year \
    FROM film \
        INNER JOIN film_actor ON film_actor.film_id = film.film_id \
        INNER JOIN actor ON film_actor.actor_id = actor.actor_id ")
    # cursor.execute("SELECT * from actor")
    rows = cursor.fetchmany(10)

    # Print SQL query results
    print("\nShow me the databases:\n")
    for row in rows:
        print("ACTOR_ID:   ", row[0])
        print("FIRST_NAME:   ", row[1])
        print("LAST_NAME:    ", row[2])
        print("FILM_ID:   ", row[3])
        print("TITLE:   ", row[4])
        print("DESCRIPTION:   ", row[5])
        print("RELEASE_YEAR:   ", row[6], "\n")

    ```
-   Save the file. `cd` to folder containing script
-   Run the script in Terminal
    `python [FILE_NAME].py`
