import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    password="19122003",
    user="root",
    database="Movie"
)


if conn.is_connected():
    print("database connected")

    cursor = conn.cursor()

    # user
    user_table = """
    CREATE TABLE IF NOT EXISTS User (
        User_ID INT(30) PRIMARY KEY,
        Username VARCHAR(50),
        Password VARCHAR(50)
    )
    """
    cursor.execute(user_table)

    # director

    director_table = """
        CREATE TABLE IF NOT EXISTS Director (
            Director_ID INT(30) PRIMARY KEY,
            Director_Name VARCHAR(50)
        )
        """
    cursor.execute(director_table)

    # genre

    genre_table = """
            CREATE TABLE IF NOT EXISTS Genre (
                Genre_ID INT(30) PRIMARY KEY,
                Genre_Name VARCHAR(50)
            )
            """
    cursor.execute(genre_table)

    # movie

    movie_table = """
    CREATE TABLE IF NOT EXISTS Movie (
        Movie_ID INT(30) PRIMARY KEY,
        Title VARCHAR(50),
        Release_Date DATE,
        Duration INT(10),
        Director_ID INT(30),
        Genre_ID INT(30),
        FOREIGN KEY (Director_ID) REFERENCES Director(Director_ID),
        FOREIGN KEY (Genre_ID) REFERENCES Genre(Genre_ID)
    )
    """
    cursor.execute(movie_table)

    # list_table

    my_list_table = """
    CREATE TABLE IF NOT EXISTS My_List (
        List_ID INT(30) PRIMARY KEY AUTO_INCREMENT,
        User_ID INT(30),
        Movie_ID INT(30),
        FOREIGN KEY (User_ID) REFERENCES User(User_ID),
        FOREIGN KEY (Movie_ID) REFERENCES Movie(Movie_ID)
    )
    """
    cursor.execute(my_list_table)

    conn.commit()
    print("tables created")

    


    cursor.close()
    conn.close()
