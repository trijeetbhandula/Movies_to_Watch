"""
Movies Assignment-2
Movie Class
"""


class Movie:
    """Movie class for storing details of a movie."""

    def __init__(self, title="", year=0, category="", is_watched=False):
        """Initialise a Movie."""
        self.title = title
        self.year = year
        self.category = category
        self.is_watched = is_watched

    def __str__(self):
        """Return a string representation of a Movie."""
        return f'{self.title}, {self.year}, {self.category}, {self.is_watched}'

    def __repr__(self):
        """Returns movie representation to string format."""
        return str(self)

    def mark_watched(self):
        """Marks movie as watched."""
        self.is_watched = True

    def mark_unwatched(self):
        """Marks movie as unwatched."""
        self.is_watched = False
