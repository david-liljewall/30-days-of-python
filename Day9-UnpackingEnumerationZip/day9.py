# ---------------------------------------------------------------------------- #
#                 Unpacking, Enumeration, and the zip Function                 #
# ---------------------------------------------------------------------------- #

#* ------------------------- Unpacking (Destructuring) ------------------------ #

movie = ("12 Angry Men", "Sidney Lumet", 1957)

title = movie[0]
director = movie[1]
year = movie[2]

##* The above code can be more succinctly accomplished in the following way, using Unpacking:
movie = ("12 Angry Men", "Sidney Lumet", 1957)
# assign variable using unpacking
title, director, year = movie

print( f"{title}, {director}, {year}" )

## What is happening here is that Python is assigning each variable (in order), to each element of the tuple in order


##* Unpacking in for loops:
movies = [
	(
		"Eternal Sunshine of the Spotless Mind",
		"Michel Gondry",
		2004
	),
	(
		"Memento",
		"Christopher Nolan",
		2000
	),
	(
		"Requiem for a Dream",
		"Darren Aronofsky",
		2000
	)
]

# We can use the same syntax as above, since title, director, year = movie. movie is the iterator normally, but we can substitute for the unpacking iterator
for ( title, director, year )  in movies:
    print( f"{title} ({year}), by {director}" )
    # NOTE: it's important to keep the unpacking iterator IN ORDER, i.e. title = movie[0], director = movie[1], year = movie[2]
    

#* -------------------------------- Enumeration ------------------------------- #

# Say we want to print a numbered list of the movies in the above collection. We could do:
counter = 1

for title, director, year in movies:
	print(f"{counter}. {title} ({year}), by {director}")
	counter += 1

# Brief enumeration example:
names = [ "Harry", "Rachel", "Brian" ]

for counter, name in enumerate( names, start=1 ): 
    print( f"{counter}.) {name}" )
    
## Under the hood:
# enumerate() function adds a counter to an iterable (i.e., names list), and start=1 dictates that we start the counter at 1

    
    
## Enumeration used in original movies list:
for counter, movie in enumerate( movies, start=1 ):
    print( f"{counter}.) {movie[0]} ({movie[2]}), by {movie[1]}" )
# where in enumerate(movies, start=1), a series of two element tuples is created as: (2, ("Memento", "Christopher Nolan", 2000)), where the first itme is the counter variable and the second item is the three element movie tuple


# NOTE: Best way to enumerate over a collection of tuples:
for counter, ( title, director, year ) in enumerate( movies, start=1 ):
    print(f"{counter}. {title} ({year}), by {director}")
# In this way, we are using (title, director, year) to match the format of the second item in the tuple created by the enumerate function




#* ------------------------------- zip Function ------------------------------- #

## The zip function is used to combine two or more iterables into a single iterable

# Let's say we have two lists and want to combine them into one iterable (series of tuples), we could then be put into its own list
pet_owners = ["Paul", "Andrea", "Marta"]
pets = ["Fluffy", "Bubbles", "Captain Catsworth"]

pets_and_owners = zip( pet_owners, pets )

pets_and_owners_list = list( pets_and_owners )
print( pets_and_owners_list )

## Using zip in loops: allows for iteration over two or more iterables at once

for owner, pet in zip( pet_owners, pets ): # _iter_ owner corresponds to pet_owners
    print( f"{owner} owns {pet}." )
    
##* NOTE: when using enumerate and zip, they are CONSUMED when we iterate over them. This means that if you have a variable assigned to enumerate() or zip(), once that variable is used in a loop you will not have access to it any more
    
# Sooooo instead of:
pets_and_owners = zip( pet_owners, pets )
# do:
pets_and_owners = list( zip( pet_owners, pets ) )
# in order to have access to this variable later even after iterating over it



# ---------------------------------------------------------------------------- #
#*                                  EXERCISES                                  #
# ---------------------------------------------------------------------------- #

# 1) Print out the character information with species and actor name
main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]

for ( character, actor, species ) in main_characters:
    print( f"{character} is a {species.lower()} voiced by {actor}" )
    
    
    
    
## FIXME: 2) Unpack the following tuple into 4 variables:

data = ("John Smith", 11743, ("Computer Science", "Mathematics"))

# Unpack info from data into 4 separate variables
name, id_number, ( major, minor ) = data


# 3) Investigate what happens when you try to zip two iterables of different lengths. For example, try to zip a list containing three items, and a tuples containing four items.

three_list = ["list 1", "list 2", "list 3"]
four_tuple = ( "tuple 1", "tuple 2", "tuple 3", "tuple 4" )

zipped_object = zip( three_list, four_tuple )

print( list( zipped_object ) )


## NOTE: when zipping objects of different sizes together - as above - it will only zip to the lowest number of elements. In this case, it only zipped 3 elements since the list only contained 3. The fourth element of the tuple was left out entirely.