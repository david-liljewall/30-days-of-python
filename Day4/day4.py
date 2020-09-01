# ---------------------------------------------------------------------------- #
#                                     LISTS                                    #
# ---------------------------------------------------------------------------- #

#* Lists are like arrays in C++, except you can have mixed types
movie_titles = [
    "Eternal Sunshine of the Spotless Mind", 29,
    "Memento", 30,
    "Requiem for  Dream", 40
]

print( movie_titles[0], movie_titles[2] )

# access the last element, then second to last
print( movie_titles[-1], movie_titles[-2])


# -------------------------- Adding items to a list -------------------------- #

names = [ "John", "Alice", "Sarah", "George" ]
names.append( "Simon" )
print( names[-1] )

#OR
names = names + [ "Simon2" ] # you can ADD LISTS TOGETHER, without modifying the original list. A new list called names is created
print( names )

names = [ "John", "Alice", "Sarah", "George" ]
names1 = ["Simon2"]
names.extend( names1 ) # NOTE: Cleaner way of doing the above
print( names )


# ------------------- Inserting/removing items from a list ------------------- #

numbers = [ 1, 2, 4, 5 ]
# we are missing the # 3, insert it to a specified index location: 
numbers.insert( 2, 3 )
print( numbers )


# Now if we want start the list from 2, i.e. remove #1, do:
numbers.remove( 1 )
print( numbers )
# OR
numbers = [ 1, 2, 4, 5 ]
numbers.pop( 0 )
print( numbers )


# To remove EVERYTHING in a list:
numbers.clear()
print( numbers ) # now an empty list


# ---------------------------------------------------------------------------- #
#                                    TUPLES                                    #
# ---------------------------------------------------------------------------- #

#* Tuples are different from lists in that they are IMMUTABLE. We can't change them once we define them. We can add tuples together, but the original tuples remain unchanaged. We cannot use pop or append like we can with lists


# Lists can store tuples, as follows:
movies = [
    (
        "Eternal Sunshine of the Spotles Mind", 
        "Michael Gondry",
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
] # This represents a table in tuple form

#* Accesing tuple data:

print( movies[0] ) # print first row of 'movie table'
print( movies[0][0] ) # prints first row and column


# ---------------------------------------------------------------------------- #
#*                                   EXERCISE                                   *#
# ---------------------------------------------------------------------------- #

# 1) Initial tuple
movies = [
    (
        "The Shawshank Redemption",
        "Frank Darabont",
        1994,
        25e6
    )
]

# 2) User input for another film
print( "Enter a movie title:" )
title = input()
print( "Enter the director's name:" )
director = input()
print( "Enter the release year:" )
release_year = int( input() )
print( "Enter the movie's budget:" )
budget = int( input() )

# 3) Create new tuple from user input
user_movie = [
    (
        title,
        director,
        release_year,
        budget
    )
]

# 4) Use f-string to print movie name and release year by accessing user tuple
output = f"Title: {user_movie[0][0]}, Release year: {user_movie[0][1]}"
print( "User Film:", output )

# 5) Add new movie tuple to movies collection
# NOTE: though the tuple WITHIN movies is immutable, the list can be altered via append, etc.
movies.append( user_movie )

# 6) Print both movies in the movies collection
print( movies )

# 7) Remove the first movie from movies. Any method
movies.pop( 0 )
print( movies )



