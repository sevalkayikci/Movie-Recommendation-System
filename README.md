# 🎬 Movie Recommendation System 📽️

A Python-based application using Tkinter for the GUI and MySQL for the database to manage and recommend movies. Users can log in, add movies to their list, get random movie recommendations, and view all available movies.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **🔑 User Login**: Secure login for users with their username and password.
- **📝 Add Movies to List**: Add movies to your personal list from recommendations or from the complete movie list.
- **🎥 Movie Recommendations**: Get random movie recommendations based on selected genres.
- **📋 View All Movies**: Display all movies available in the database.
- **❌ Delete Movies from List**: Remove movies from your personal list.
- **🔍 Search Functionality**: Quickly search for movies within your list.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/sevalkayikci/movie-recommendation-system.git
    cd movie-recommendation-system
    ```

2. **Install the required Python packages**:

    ```bash
    pip install mysql-connector-python
    ```

3. **Set up the MySQL database**:

    - Create a database named `Movie`.
    - Create the necessary tables (`User`, `Movie`, `My_List`, `Genre`) and populate them with data.

4. **Run the application**:

    ```bash
    python movie_recommendation_system.py
    ```

## Usage

1. **Launch the Application**:

    ```bash
    python movie_recommendation_system.py
    ```

2. **Log In**:
    - Enter your username and password to log in.

3. **Manage Your Movie List**:
    - Use the "My List" button to view and manage your personal movie list.
    - Add movies from the "Show All Movies" list or from recommendations.

4. **Get Recommendations**:
    - Click on "Don't Know What To Watch?" and select a genre to get a random movie recommendation.

5. **View All Movies**:
    - Click on "Show All Movies" to see all movies in the database.

## Contributing

1. **Fork the repository**.
2. **Create a new branch**:

    ```bash
    git checkout -b feature-branch
    ```

3. **Make your changes**.
4. **Commit your changes**:

    ```bash
    git commit -m 'Add some feature'
    ```

5. **Push to the branch**:

    ```bash
    git push origin feature-branch
    ```

6. **Open a pull request**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

*This is a school project by Seval Kayikci and Elif Ergün[https://github.com/elferg].*

Seval Kayikci - [sevalkayikci@gmail.com](mailto:sevalkayikci@gmail.com)

Project Link: [https://github.com/sevalkayikci/movie-recommendation-system](https://github.com/sevalkayikci/movie-recommendation-system)
