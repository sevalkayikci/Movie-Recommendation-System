import mysql.connector
import tkinter as tk
from tkinter import messagebox

class MovieRecommendationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Recommendation System")
        self.root.geometry("800x400")  # Adjusted window size

        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="19122003",
            database="Movie"
        )

        if self.conn.is_connected():
            print("Database connected")
            self.cursor = self.conn.cursor()

        self.create_widgets()

    def create_widgets(self):
        # Widgets for login
        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack(pady=10)
        
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=10)

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack(pady=10)
        
        self.password_entry = tk.Entry(self.root, show="•")
        self.password_entry.pack(pady=10)

        self.login_button = tk.Button(self.root, text="Enter", command=self.login)
        self.login_button.pack(pady=10)

        # Other buttons
        buttons = [
            ("My List", self.show_user_list),
            ("Don't Know What To Watch?", self.show_suggestion),
            ("Show All Movies", self.show_all_movies),
        ]

        for button_text, command in buttons:
            button = tk.Button(self.root, text=button_text, command=command)
            button.pack(pady=10)

        # User's movie list
        self.user_movies = []

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        query = "SELECT * FROM User WHERE Username = %s AND Password = %s"
        self.cursor.execute(query, (username, password))
        user = self.cursor.fetchone()

        if user:
            user_id = user[0]
            print("Login successful. User ID:", user_id)
            messagebox.showinfo("Successful", f"Welcome, {username}")
        else:
            messagebox.showerror("Entry Error", "Invalid password or username")

    def return_to_main(self, window):
        window.destroy()

    def show_user_list(self):
        user_list_window = tk.Toplevel(self.root)
        user_list_window.title("Film List")
        user_list_window.geometry("600x400")  # Adjusted window size

        username = self.username_entry.get()
        query_user_id = "SELECT User_ID FROM User WHERE Username = %s"
        self.cursor.execute(query_user_id, (username,))
        user_id_result = self.cursor.fetchone()

        if user_id_result:
            user_id = user_id_result[0]
            self.show_user_list_content(user_list_window, user_id)
        else:
            messagebox.showerror("Error", "User not found.")

    def show_user_list_content(self, user_list_window, user_id):
        user_list_window.geometry("600x400")  # Adjusted window size

        user_movie_listbox = tk.Listbox(user_list_window, selectmode=tk.SINGLE)
        user_movie_listbox.pack(expand=True, fill=tk.BOTH)

        query_user_movies = "SELECT Movie.Movie_ID, Movie.Title FROM Movie JOIN My_List ON Movie.Movie_ID = My_List.Movie_ID WHERE My_List.User_ID = %s"
        self.cursor.execute(query_user_movies, (user_id,))
        user_movies = self.cursor.fetchall()

        if not user_movies:
            user_movie_listbox.insert(tk.END, "List Empty.")
        else:
            for movie in user_movies:
                user_movie_listbox.insert(tk.END, movie[1])

            delete_button = tk.Button(user_list_window, text="Delete", command=lambda: self.delete_from_list(user_id, user_movie_listbox))
            delete_button.pack(pady=10)

        return_button = tk.Button(user_list_window, text="Return to Main", command=lambda: self.return_to_main(user_list_window))
        return_button.pack(pady=10)

    def delete_from_list(self, user_id, user_movie_listbox):
        try:
            selected_movie = user_movie_listbox.get(tk.ACTIVE)

            query_movie_id = "SELECT Movie_ID FROM Movie WHERE Title = %s"
            self.cursor.execute(query_movie_id, (selected_movie,))
            result_movie_id = self.cursor.fetchone()

            if result_movie_id:
                movie_id = result_movie_id[0]

                query_delete_movie = "DELETE FROM My_List WHERE User_ID = %s AND Movie_ID = %s"
                self.cursor.execute(query_delete_movie, (user_id, movie_id))
                self.conn.commit()

                messagebox.showinfo("Success", "Movie deleted from your list.")
                user_movie_listbox.delete(tk.ACTIVE)
            else:
                messagebox.showerror("Error", "Movie not found.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def add_to_list(self, movie_title):
        username = self.username_entry.get()

        query_user_id = "SELECT User_ID FROM User WHERE Username = %s"
        self.cursor.execute(query_user_id, (username,))
        result_user_id = self.cursor.fetchone()

        if result_user_id:
            user_id = result_user_id[0]

            try:
                query_movie_id = "SELECT Movie_ID FROM Movie WHERE Title = %s"
                self.cursor.execute(query_movie_id, (movie_title,))
                result_movie_id = self.cursor.fetchone()

                if result_movie_id:
                    movie_id = result_movie_id[0]

                    query_insert_movie = "INSERT INTO My_List (User_ID, Movie_ID) VALUES (%s, %s)"
                    self.cursor.execute(query_insert_movie, (user_id, movie_id))
                    self.conn.commit()
                    messagebox.showinfo("Success", "Movie added to your list.")
                else:
                    messagebox.showerror("Error", "Movie not found.")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")
        else:
            messagebox.showerror("Error", "User not found.")

    def show_suggestion(self):
        suggestion_window = tk.Toplevel(self.root)
        suggestion_window.title("Movie Recommendation")
        suggestion_window.geometry("600x400")

        genres = ["", "Action", "Drama", "Science Fiction", "Fantastic", "Comedy", "Fear",
                  "Romance", "Animation", "Thrillers", "Crime", "Adventure"]
        genre_choice = tk.StringVar(self.root)
        genre_choice.set(genres[0])

        tk.Label(suggestion_window, text="Select Genre:").pack(pady=10)
        genre_menu = tk.OptionMenu(suggestion_window, genre_choice, *genres)
        genre_menu.pack(pady=10)

        recommended_label = tk.Label(suggestion_window, text="")
        recommended_label.pack(pady=10)

        get_suggestion_button = tk.Button(
            suggestion_window,
            text="Recommend Me!",
            command=lambda: self.generate_suggestion(recommended_label, genre_choice.get())
        )
        get_suggestion_button.pack(pady=10)

        add_button = tk.Button(suggestion_window, text="Add to My List",
                               command=lambda: self.add_to_list(recommended_label.cget("text")))
        add_button.pack(pady=10)

        return_button = tk.Button(suggestion_window, text="Return to Main", command=lambda: self.return_to_main(suggestion_window))
        return_button.pack(pady=10)

    def generate_suggestion(self, recommended_label, genre):
        recommended_label.config(text="")

        query = "SELECT Movie.Title FROM Movie WHERE Genre_ID IN (SELECT Genre_ID FROM Genre WHERE Genre_Name = %s) ORDER BY RAND() LIMIT 1"
        params = (genre,)
        self.cursor.execute(query, params)
        suggested_movie = self.cursor.fetchone()

        if suggested_movie:
            recommended_label.config(text=suggested_movie[0])
        else:
            recommended_label.config(text="No movies found.")

    def show_all_movies(self):
        all_movies_window = tk.Toplevel(self.root)
        all_movies_window.title("All Movies")
        all_movies_window.geometry("800x400")

        movie_listbox = tk.Listbox(all_movies_window, selectmode=tk.SINGLE)
        movie_listbox.pack(expand=True, fill=tk.BOTH)

        self.cursor.execute("SELECT Movie.Title FROM Movie")
        all_movies = self.cursor.fetchall()

        for movie in all_movies:
            movie_listbox.insert(tk.END, movie[0])

        add_button = tk.Button(all_movies_window, text="Add to My List", command=lambda: self.add_to_list(movie_listbox.get(tk.ACTIVE)))
        add_button.pack(pady=10)

        return_button = tk.Button(all_movies_window, text="Return to Main", command=lambda: self.return_to_main(all_movies_window))
        return_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = MovieRecommendationSystem(root)
    root.mainloop()
