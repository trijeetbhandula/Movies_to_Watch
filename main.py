"""
Name: Trijeet Bhandula
Date: 22nd November, 2022
Brief Project Description:
This app interacts with user to perform various functions like adding movie, displaying movies and buttons
to change them to watch or unwatched. While it has error checking for adding movies to get valid movie details.
GitHub URL: https://github.com/cp1404-students/a2-movies-trijeetbhandula
"""

from kivy.app import App
from moviecollection import MovieCollection
from movie import Movie
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class MoviesToWatchApp(App):
    """Main program - Kivy app to demo combining classes and Kivy widget."""
    status_text = StringProperty()
    status_movie = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.movies_data = MovieCollection()
        self.movies_data.load_movies()
        self.status_movie = f"To watch: {self.movies_data.get_number_unwatched_movies()} Watched: {self.movies_data.get_number_watched_movies()}"

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Movies To Watch 2.0"
        self.root = Builder.load_file('app.kv')
        self.movies_data.sort("category")
        self.create_movie_buttons()
        return self.root

    def create_movie_buttons(self):
        """Create buttons from list of objects and add them to the GUI."""
        self.root.ids.entries_box.clear_widgets()
        for movie in self.movies_data.movies:
            temp_button = Button(text=f"{movie.title} ({movie.category} from {movie.year})")
            temp_button.bind(on_release=self.press_entry)
            temp_button.movie = movie
            self.decide_color(movie, temp_button)
            self.root.ids.entries_box.add_widget(temp_button)

    def decide_color(self, movie, temp_button):
        """Decides colors of buttons for watched and unwatched movies."""
        if movie.is_watched:
            temp_button.background_color = (1, 1, 0, 1)
        else:
            temp_button.background_color = (1, 1, 1, 1)
        return self, movie, temp_button

    def press_entry(self, instance):
        """Handle pressing movie buttons."""
        movie = instance.movie
        if movie.is_watched:
            movie.mark_unwatched()
            instance.background_color = (1, 1, 1, 1)
            self.status_text = f"You need to watch {movie.title}"
        else:
            movie.mark_watched()
            instance.background_color = (1, 1, 0, 1)
            self.status_text = f"You have watched {movie.title}"
        self.sort_by_options(self.root.ids.category_selection.text)
        self.status_movie = f"To watch: {self.movies_data.get_number_unwatched_movies()} Watched: {self.movies_data.get_number_watched_movies()}"

    def sort_by_options(self, value):
        """Sort movies buttons by selected value"""
        sort_by = value.lower()
        self.movies_data.sort(sort_by)
        self.create_movie_buttons()

    def press_add_movie(self, entered_title, entered_year, entered_category):
        """Handle pressing add movie button"""
        self.movies_data.add_movie(Movie(entered_title, int(entered_year), entered_category, False))
        self.sort_by_options(self.root.ids.category_selection.text)
        self.clear_fields()

    def get_valid_input(self, entered_title, entered_category, entered_year):
        """Gets valid input for adding a movie"""
        if entered_title == "" or entered_category == "" or entered_year == "":
            self.status_text = f"All fields must be completed"
        else:
            self.get_valid_year(entered_year, entered_category, entered_title)
            # self.press_add_movie(entered_title, entered_year, entered_category)

    def get_valid_year(self, entered_year, entered_category, entered_title):
        """Performs error checking for the entered year"""
        try:
            entered_year = int(entered_year)
            if entered_year <= 0:
                self.status_text = "Year must be >=0"
            else:
                self.get_valid_category(entered_category, entered_title, entered_year)
        except ValueError:
            self.status_text = f"Please enter a valid number"

    def get_valid_category(self, entered_category, entered_title, entered_year):
        """Performs error checking for the entered category"""
        categories = ["Action", "Comedy", "Documentary", "Drama", "Fantasy", "Thriller"]
        entered_category = entered_category.title()
        if entered_category in categories:
            self.press_add_movie(entered_title, entered_year, entered_category)
        else:
            self.status_text = f"Category must be one of {(', '.join(categories))}"

    def clear_fields(self):
        """Clear the text input fields for movie title, year and category."""
        self.root.ids.entered_title.text = ""
        self.root.ids.entered_category.text = ""
        self.root.ids.entered_year.text = ""


if __name__ == '__main__':
    MoviesToWatchApp().run()
