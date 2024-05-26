import mysql.connector
conn = mysql.connector.connect(host='root', password='19122003', user='root', database='Movie')
cursor = conn.cursor()

if conn.is_connected():
     print("connected")

# INSERT TO GENRE
try:
       insert_query = "INSERT INTO genre (genre_id, genre_name) VALUES (%s, %s)"
       insert_genre = (11, 'Adventure')
       cursor.execute(insert_query, insert_genre)
       result = cursor.fetchall()
       conn.commit()
       print("Data inserted successfully")
except Exception as e:
      print(f"Error: {e}")
finally:
      cursor.close()
      conn.close()

# SHOW GENRE
try:
      # SELECT query
      select_query = "SELECT * FROM genre"
      # Execute query
      cursor.execute(select_query)
      # Take results
      result = cursor.fetchall()
      # Print results
      for row in result:
         print(row)
# Find errors if there is, and print the error messages
except Exception as e:
     print(f"Error: {e}")
finally:
     # Close connection
     cursor.close()
     conn.close()

# INSERT TO DIRECTOR
try:
      insert_query = "INSERT INTO director (director_id, director_name) VALUES (%s, %s)"
      insert_director = ('122', 'Roberto Benigni')
      cursor.execute(insert_query, insert_director)
      result = cursor.fetchall()
      conn.commit()
      print("Data inserted successfully")
except Exception as e:
     print(f"Error: {e}")
finally:
     cursor.close()
     conn.close()

# SHOW DIRECTOR
try:
      select_query = "SELECT * FROM director"
      cursor.execute(select_query)
      result = cursor.fetchall()
      for row in result:
         print(row)
except Exception as e:
     print(f"Error: {e}")
finally:
     cursor.close()
     conn.close()

# INSERT TO MOVIE
try:
       insert_query = "INSERT INTO movie (director_id, duration, genre_id, movie_id, release_date, title) VALUES (%s, %s, %s, %s, %s, %s)"
       insert_movie= (121, 106, 8, 757, 2011, 'Cars 2')
       cursor.execute(insert_query, insert_movie)
       result = cursor.fetchall()
       conn.commit()
       print("Data inserted successfully")
except Exception as e:
      print(f"Error: {e}")
finally:
      cursor.close()
      conn.close()

# SHOW MOVIE
try:
      select_query = "SELECT * FROM movie"
      cursor.execute(select_query)
      result = cursor.fetchall()
      for row in result:
         print(row)
except Exception as e:
     print(f"Error: {e}")
finally:
     cursor.close()
     conn.close()

# INSERT TO USER
try:
       insert_query = "INSERT INTO user (user_id, username, password) VALUES (%s, %s, %s)"
       insert_user = (123, 'salman', 'salman123')
       cursor.execute(insert_query, insert_user)
       result = cursor.fetchall()
       conn.commit()
       print("Data inserted successfully")
except Exception as e:
      print(f"Error: {e}")
finally:
      cursor.close()
      conn.close()

# SHOW USER
try:
      select_query = "SELECT * FROM user"
      cursor.execute(select_query)
      result = cursor.fetchall()
      for row in result:
         print(row)
except Exception as e:
     print(f"Error: {e}")
finally:
     cursor.close()
     conn.close()

# INSERT TO MY_LIST
try:
       insert_query = "INSERT INTO my_list (list_id, user_id,) VALUES (%s, %s)"
       insert_user = (10123, 123)
       cursor.execute(insert_query, insert_user)
       result = cursor.fetchall()
       conn.commit()
       print("Data inserted successfully")
except Exception as e:
      print(f"Error: {e}")
finally:
      cursor.close()
      conn.close()

# SHOW MY_LIST
try:
      select_query = "SELECT * FROM my_list"
      cursor.execute(select_query)
      result = cursor.fetchall()
      for row in result:
         print(row)
except Exception as e:
     print(f"Error: {e}")
finally:
     cursor.close()
     conn.close()

# SORTING AS DRAMA
def drama(cursor):
      try:
            select_query = "SELECT * FROM movie WHERE genre_id = '2'"
            cursor.execute(select_query)
            result = cursor.fetchall()
            for row in result:
                  print(row)
      except Exception as e:
            print(f"Error: {e}")
      finally:
            cursor.close()
            conn.close()

drama(cursor)

# SORTING AS RELEASE DATE
x = int (input( "Enter year: "))
def release(cursor):
      try:
            select_query = f"SELECT * FROM movie WHERE release_date > {x}"
            cursor.execute(select_query)
            result = cursor.fetchall()
            for row in result:
                  print(row)
      except Exception as e:
            print(f"Error: {e}")
      finally:
            cursor.close()
            conn.close()

release (cursor)
     
# DELETION 
cursor.execute("DELETE FROM movie WHERE movie_id ='727'")
conn.commit()

# UPDATING
cursor.execute("UPDATE movie SET release_date = '2002' WHERE movie_id = '712'")
conn.commit()


