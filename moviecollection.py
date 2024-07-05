"""
Movies Assignment-2
MovieCollection Class
"""

import json
from movie import Movie
from operator import attrgetter


class MovieCollection:
    """Movie collection class to perform different methods"""

    def __init__(self):
        """Construct a MovieCollection with a name and empty movie's collection."""
        self.movies = []

    def __str__(self):
        """Return a string representation of a movies."""
        movies_strings = [str(movie) for movie in self.movies]
        return ', '.join(movies_strings)

    def __repr__(self):
        """Returns movie collection representation to string format."""
        return f'Title: {self.title}, Year: {self.year}, Category: {self.category}, Watched: {self.is_watched}'

    def add_movie(self, movie):
        """Add a movie to the movies collection"""
        self.movies.append(movie)

    def get_number_unwatched_movies(self):
        """Count the number of unwatched movies"""
        unwatched_number = sum([1 for movie in self.movies if not movie.is_watched])
        return unwatched_number

    def get_number_watched_movies(self):
        """Count the number of watched movies"""
        watched_number = sum([1 for movie in self.movies if movie.is_watched])
        return watched_number

    def load_movies(self, filename="movies.json"):
        """Load the movies from a json file and append it in movies collection"""
        in_file = open(filename, "r")
        movies_data = json.load(in_file)
        for movie_data in movies_data:
            movie = Movie(movie_data['title'], movie_data['year'], movie_data['category'], movie_data['is_watched'])
            self.movies.append(movie)
        in_file.close()

    def save_movies(self, filename="movies.json"):
        """Saves the movies collection to a json file"""
        with open(filename, "w") as out_file:
            json_string = json.dumps(self.movies, default=vars)
            print(json_string, file=out_file)

    def sort(self, key):
        """Filter and sort movies by the date"""
        self.movies.sort(key=attrgetter(key, "title"))
