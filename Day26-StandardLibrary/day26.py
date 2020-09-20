# ---------------------------------------------------------------------------- #
#                        Leveraging the Standard Library                       #
# ---------------------------------------------------------------------------- #


#* -------------------------- The namedtuple function ------------------------- #

from collections import namedtuple

Book = namedtuple( "Book", [ "title", "author", "year" ] )

book = Book( "The Color of Magic", author="Terry Pratchett", year=1983 )

print( f"{book.title} ({book.year}), by {book.author}" )

# NOTE: A good place to make use of namedtuple might have been working with iris data for day 14:
with open("iris.csv", "r") as iris_file:
	iris_data = iris_file.readlines()

irises = []

for row in iris_data[1:]:
	sepal_length, sepal_width, petal_length, petal_width, species = row.strip().split(",")

	irises.append({
		"sepal_length": sepal_length,
		"sepal_width": sepal_width,
		"petal_length": petal_length,
		"petal_width": petal_width,
		"species": species
	})

# INTO:
from collections import namedtuple

Iris = namedtuple("Iris", ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"])

with open("iris.csv", "r") as iris_file:
	iris_data = iris_file.readlines()

irises = []

for row in iris_data[ 1: ]:
	iris = Iris( *row.strip().split(",") )
	irises.append( iris )

print( irises )


#* --------------------------- The partial function --------------------------- #

# the partial function allows us to create a new version of a function with some portion of the arguments already given.

from functools import partial

def exponentiate( base, exponent ):
	return base ** exponent

# Create square function that squares the base
square = partial( exponentiate, exponent=2 )
# Create cube function that cubes the base
cube = partial( exponentiate, exponent=3 )

a = 2
b = 3

print( exponentiate( a, b ) )
print( square( a ) )
print( cube( a ) )



#* --------------------------- The defaultdict type --------------------------- #

# defaultdicts allow us to specify a default value to return when we attempt to access a key which doesn't exist. This saves us a ton of time without having to call get and specify a default value in each case
from collections import namedtuple, defaultdict

User = namedtuple("User", ["name", "username", "location"])

users = defaultdict(
    lambda: "Could not find a user matching that user id.",
    {
	"0001": User("Phil", "pbest", "Hungary"),
	"0002": User("Jose", "jslvtr", "Scotland"),
	"0003": User("Luka", "lukamiliv", "Serbia")
    }
)

user_id = input( "Please enter a user id: " )
print( users[ user_id ] )

## We can also use default dictionaries is as a sort of counter
    # To demonstrate this, let's say we're trying to keep track of an inventory for a character in an RPG of some kind. We're using a dictionary to store what is in the character's inventory, with the keys being the item names, and the values being a count of how many of this item the character has.
    # I'm also going to create a function which is going to modify this dictionary, allowing the user to add new items.

from collections import defaultdict

inventory = defaultdict(int)

def add_item(item, amount):
	inventory[item] += amount
    # NOTE: when int is called without any arguments, it returns 0, meaning that the right hand inventory[item] of a = a + amount is replaced with a 0, allowing us to create a new key with a starting value equal to the amount of that item added.

add_item("bow", 1)
add_item("arrow", 20)
add_item("arrow", 20)
add_item("bracer", 2)

print(inventory)  # defaultdict(<class 'int'>, {'bow': 1, 'arrow': 40, 'bracer': 2})



# ---------------------------------------------------------------------------- #
#*                                   Exercises                                  #
# ---------------------------------------------------------------------------- #

## 1) Define a Movie tuple using namedtuple that accepts a title, a director, a release year, and a budget. Prompt the user to provide information for each of these fields and create an instance of the Movie tuple you defined.

from collections import namedtuple

Movie = namedtuple( "Movie", [ "title", "director", "release_year", "budget" ] )

user_input = input( "Please enter a movie title, director, release year, and budget: " ).strip()
title, director, release_year, budget = [ entry for entry in user_input.split( ", " ) ]

user_movie = Movie( title, director, release_year, budget )

print( user_movie )


## 2) Use a defaultdict to store a count for each character that appears in a given string. Print the most common character in this dictionary.

from collections import defaultdict

test_string = "onomatopoeia"

char_counter = defaultdict( int )

for char in test_string:
    char_counter[ char ] += 1 # increment count for specific characte

most_common_character = max(char_counter, key=lambda key: char_counter[key])

print( most_common_character )


## 3) Use the mul function in the operator module to create a partial called double that always provides 2 as the first argument.
from operator import mul

double = partial( mul, 2 )

print( double( 3 ) )

# NOTE: for positional arguments, we just have to list them in order, where a=2, b=3
two_times_three = partial( mul, 2, 3 )
print( two_times_three() )

## 4) Create a read function using a partial that opens a file in read ("r") mode.

read = partial( open, mode="r" )

def read_file( filename ):   
    with read( filename ) as file:
        line_info = file.readlines()
    
    for line in line_info:
        print( line )
        
read_file( "./test_file.txt" )
