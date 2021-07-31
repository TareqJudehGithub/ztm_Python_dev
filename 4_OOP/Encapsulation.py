"""
 - The four pillars of OOP are:
        1. Encapsulation
            The binding of data and functions that manipulate that data. Like we
            encapsulate the class with its attributes and methods (data). For example
            I can create methods to use attributes defined. Here, I'm encapsulating
            the functionality. Also in strings methods, we encapsulate these methods
            to use with the string. like using .upper() with a string object.

"""


class Movie:

    def __init__(self, title, year, IMDB):
        self.title = title
        self.year = year
        self.IMDB = IMDB
        self.favorites = list()
        print(self.mov_details())
    @classmethod
    def fav_movie(cls, title, year, IMDB):
        return cls(title, year, IMDB)

    def mov_details(self):
        return f'Title: {self.title}, Year: {self.year}, IMDB rating: {self.IMDB}'


mov_001 = Movie(title='Back to the future', year=1984, IMDB=8.7)
mov_002 = Movie('Alien', 1979, 7.8)
mov_003 = Movie.fav_movie("Lord of the rings: The Fellowship", 2000, 9)

print('')
# calling a class method
print(mov_003.title, mov_003.year, mov_003.IMDB)
print('')

