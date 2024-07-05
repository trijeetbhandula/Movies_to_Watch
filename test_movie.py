"""Tests for Movie class."""
from movie import Movie


def run_tests():
    """Test Movie class."""

    # Test empty movie (defaults)
    print("Test empty movie:")
    default_movie = Movie()
    print(default_movie)
    assert default_movie.title == ""
    assert default_movie.category == ""
    assert default_movie.year == 0
    assert not default_movie.is_watched

    # Test initial-value movie
    initial_movie = Movie("Thor: Ragnarok", 2017, "Comedy", True)
    print(initial_movie.is_watched)

    # Write tests to show this initialisation works
    print(initial_movie.title)
    print(initial_movie.year)
    print(initial_movie.category)
    print(initial_movie.is_watched)

    # Add more tests, as appropriate, for each method
    initial_movie.mark_unwatched()
    print(initial_movie)


run_tests()
