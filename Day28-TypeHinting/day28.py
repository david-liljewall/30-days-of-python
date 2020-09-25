# ---------------------------------------------------------------------------- #
#                                 TYPE HINTING                                 #
# ---------------------------------------------------------------------------- #


#* ---------------------------- Basic Type Hinting ---------------------------- #

# Correct type hinting:
name: str = "Phil"
age: int = 29
height_metres: float = 1.87
loves_python: bool = True

# Incorrect type hinting (mypy will catch this):
name: str = 29
age: int = 1.87
height_metres: float = "Phil"


#* -------------------------- Adding some flexibility ------------------------- #
from typing import Union, Any

name: str = "Phil"
age: int = 29
height_metres: Union[ int, float ] = 1.87
    # NOTE: the above syntax means we can accept ints or floats

# We can also use "Any" which indicates to the user that any type can be used:
height_metres_any: Any = 1.87



#* -------------------------- Annotating Collections -------------------------- #
from typing import List

names: List[ str ] = [ "Rick", "Morty", "Summer", "Beth", "Jerry" ]
    # Hinting that we are creating a list containing only string types
    # NOTE: If we leave the brackets off, it's the same as writing List[ Any ]
    

from typing import List, Union

random_values: List[ Union[ str, int ] ] =  [ "x", 13, "camel", 0 ]


## For tuples, we can specify a type for each item in sequence, since tuyples are of fixed length and are immutable

from typing import Tuple

movie: Tuple[ str, str, int ] = ( "Toy Story 3", "Lee Unkrich", 2010 )



#* --------------------------- Creating Type Aliases -------------------------- #
from typing import List, Tuple

# Create an alias for what kind of tuple we're creating
Movie = Tuple[ str, str, int ]

movies: List[ Movie ] = [
	( "Finding Nemo", "Andrew Stanton", 2005 ),
	( "Inside Out", "Pete Docter", 2015 ),
	( "Toy Story 3", "Lee Unkrich", 2010 )
]


#* --------------------------- Annotating Functions --------------------------- #
from typing import List, Tuple

Movie = Tuple[str, str, int]

# NOTE: Type hinting done directly to the function parameter:
def show_movies( movies: List[ Movie ] ):
    for title, director, year in movies:
		print(f"{title} ({year}), by {director}")


movies: List[Movie] = [
	("Finding Nemo", "Andrew Stanton", 2005),
	("Inside Out", "Pete Docter", 2015),
	("Toy Story 3", "Lee Unkrich", 2010)
]

show_movies(movies)


#* ------------------------- Annotating return values ------------------------- #
from typing import List, Tuple, Union

Movie = Tuple[str, str, int]

# NOTE: The "->" annotates the return type (either a Movie tuple, or None)
def find_movie(search_term: str, movies: List[Movie]) -> Union[ Movie, None ]:
	for title, director, year in movies:
		if title == search_term:
			return (title, director, year)


def show_movies(movies: List[Movie]):
	for movie in movies:
		print_movie(movie)


def print_movie(movie: Movie):
	title, director, year = movie
	print(f"{title} ({year}), by {director}")


movies: List[Movie] = [
	("Finding Nemo", "Andrew Stanton", 2005),
	("Inside Out", "Pete Docter", 2015),
	("Toy Story 3", "Lee Unkrich", 2010)
]

show_movies(movies)

search_result: Union[Movie, None] = find_movie("Finding Nemo", movies)

if search_result:
	print_movie(search_result)
else:
	print("Couldn't find movie.")


#* ------------------------------ Using Optional ------------------------------ #

# In cases where one of the types in a Union is None, we can use a tool called "Optional".
# Writing Optional[ Movie ] is the same thing as Union[ Movie, None ]

def find_movie(search_term: str, movies: List[Movie]) -> Optional[Movie]:
	for title, director, year in movies:
		if title == search_term:
			return (title, director, year)

	return None

