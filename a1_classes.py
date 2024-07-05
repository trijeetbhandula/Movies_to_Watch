"""
CP1404
Rewriting Assignment-1 to use Movie Class
"""

from movie import Movie
from moviecollection import MovieCollection


def main():
    """To show different option of menu to manage movie list"""
    filename = "movies.json"
    movies_data = MovieCollection()
    movies_data.load_movies(filename)
    for movie in movies_data.movies:
        if movie.is_watched:
            movie_status = "w"
        else:
            movie_status = "u"
        print(f"{movie.title}, {movie.year}, {movie.category}, {movie_status} ")
    print("Movies To Watch 1.0 - by Trijeet Bhandula")
    print(f"{len(movies_data.movies)} movies loaded from {filename}")
    choice = display_menu()
    while choice != "Q":
        if choice == "D":
            display_movies(movies_data)
        elif choice == "A":
            add_new_movie(movies_data)
        elif choice == "W":
            if movies_data.get_number_unwatched_movies() == 0:  # to check if there is any movie to watch or not
                print("No more movies to watch!")
            else:
                print("Enter the number of a movie to mark as watched")
                watch(movies_data)
        else:
            print("Invalid menu choice")
        choice = display_menu()
    movies_data.sort("year")
    movies_data.save_movies(filename)
    print(f"{len(movies_data.movies)} movies saved to {filename}")
    print("Have a nice day :)")


def display_menu():
    """Display Menu options"""
    print("Menu:\nD - Display movies\nA - Add new movie\nW - Watch a movie\nQ - Quit")
    choice = input(">>> ").upper()
    return choice


def display_movies(movies_data):
    """Display movies using movie class"""
    movies_data.sort("year")
    for index, movie in enumerate(movies_data.movies, start=1):
        max_movie_length = max(len(movie.title) for movie in movies_data.movies)
        max_year_length = max(len(str(movie.year)) for movie in movies_data.movies)
        if movie.is_watched:
            movies_status = " "
        else:
            movies_status = "*"
        print(
            f"{index}. {movies_status} {movie.title:{max_movie_length}} - {movie.year:{max_year_length}} ({movie.category})")
    print(
        f"{movies_data.get_number_watched_movies()} movies watched, {movies_data.get_number_unwatched_movies()} still to watch")


def get_valid_title():
    """Getting a valid title from the user"""
    title = input("Title: ")
    while title == "":
        print("Input can not be blank")
        title = input("Title: ")
    return title


def get_valid_year():
    """Getting a valid year from the user"""
    try:
        year = int(input("Year: "))
        while year < 1:
            print("Number must be >= 1")
            year = int(input("Year: "))
        return year
    except ValueError:
        print("Invalid input; enter a valid number")
        return get_valid_year()


def get_category():
    """Getting a valid category from the user"""
    categories = ["Action", "Comedy", "Documentary", "Drama", "Thriller", "Other"]
    print("Categories available: ", end="")
    print(*categories, sep=", ")
    category = input("Category: ").title()
    if category not in categories:
        print("Invalid category; using Other")
        category = "Other"
    return category


def add_new_movie(movies_data):
    """To add a new movie in the list of movies"""
    title = get_valid_title()
    year = get_valid_year()
    category = get_category()
    movies_data.add_movie(Movie(title, year, category, False))
    print(f"{title} ({category} from {year}) added to movie list")


def watch(movies_data):
    """To watch a movie by getting a valid index of the movie the user"""
    try:
        index_watched = int(input(">>> "))
        while index_watched < 1:
            print("Number must be >= 1")
            index_watched = int(input(">>> "))
        movie = movies_data.movies[index_watched - 1]
        if movie.is_watched:
            print(f"You have already watched {movie.title}")
        else:
            movie.is_watched = True
            print(f"{movie.title} from {movie.year} watched")
    except IndexError:
        print("Invalid movie number")
        watch(movies_data)
    except ValueError:
        print("Invalid input; enter a valid number")
        watch(movies_data)


main()
