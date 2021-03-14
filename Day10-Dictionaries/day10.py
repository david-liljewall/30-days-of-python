# ---------------------------------------------------------------------------- #
#*                                 Dictionaries                                 #
# ---------------------------------------------------------------------------- #

##* Dictionaries in python are a version of "associative arrays"

# The collections so far - lists, tuples, strings - are all "sequence types" and are accessed by index (i.e., they are iterable). These are limited in the fact if things are rearranged, the index we use to refer to an item changes with it.

## Associative array values are associated with another term, not an index, so reordering the array will not cause confusion with associations

##  Dictionary Keys:
#  A key is a little bit like a variable is that it's a thing which we can use to refer to some value. Unlike variables, keys are themselves values, as they're written as strings, integers, etc.
# In a single dictionary, each key must be unique, but different dictionaries can have the same keys as each other. 


#* --------------------------- Creating a dictionary -------------------------- #
student = {"name": "John Smith"} #* The key here is "name"

# two keys: one for name; one for grades
student = {
	"name": "John Smith",
	"grades": [88, 76, 92, 85, 69]
}

#* --------------------- Accessing values in a dictionary --------------------- #

# let's say we want to acess all the values in a dictionary associated with a specific key:

print( student[ "grades" ] ) # use the string key to access


# NOTE: if we're unsure a key exists and don't want an error, use get():
print( student.get( "grade" ) ) # returns None since "grade" is not a dictionary key

print( student.get( "grade", [] ) ) # returns an empty list if "grade" key NOT found



#* -------------------------- Modifying a dictionary -------------------------- #

## Adding new key value pairs
student = {
	"name": "John Smith",
	"grades": [88, 76, 92, 85, 69]
}

student["age"] = 17 # adds a new key "age", and adds an item association with that key

print( student )


## Using update() method
movie = {
	"title": "Avengers: Endgame",
	"directors": ["Anthony Russo", "Joe Russo"],
	"year": 2019
}
# secondary info about the film:
meta_info = {
	"runtime": 181,
	"budget": "$356 million",
	"earnings": "$2.798 billion",
	"producer": "Kevin Feige"
}

movie.update( meta_info )
print( movie )


## Modifying existing items in a dictionary
student[ "age" ] = 18

# NOTE: Can also create a dictionary this way:
name_key = "name"
grade_key = "grade"

student = {
    name_key: "John Smith",
    grade_key: [ 88, 76, 92, 85, 69 ]
}


#* --------------------- Deleting items from a dictionary --------------------- #

movie = {
	"title": "Avengers: Endgame",
	"directors": ["Anthony Russo", "Joe Russo"],
	"year": 2019,
	"runtime": 181
}

del movie["runtime"]
# OR:
movie.pop( "title" )
print( movie )

## to CLEAR/EMPTY an entire dictionary:
movie.clear()


#* ------------------------ Iterating over dictionaries ----------------------- #

movie = {
	"title": "Avengers: Endgame",
	"directors": ["Anthony Russo", "Joe Russo"],
	"year": 2019
}

# to print values:
for value in movie.values():
    print( value )
    
# to print keys:
for key, value in movie.items():
    print( f"{key}: {value}" )



# ---------------------------------------------------------------------------- #
#*                                   EXERCISES                                  #
# ---------------------------------------------------------------------------- #
  
## 1) convert the given tuple to a dictionary with 4 keys
pink_tuple = (
    
    "The Dark Side of the Moon",
    "Pink Floyd",
    1973,
    (
        "Speak to Me",
 		"Breathe",
 		"On the Run",
 		"Time",
 		"The Great Gig in the Sky",
 		"Money",
 		"Us and Them",
 		"Any Colour You Like",
 		"Brain Damage",
 		"Eclipse"
    )
)

pink_dictionary = {
    
    "album": pink_tuple[ 0 ],
    "artist": pink_tuple[ 1 ],
    "release year": pink_tuple[ 2 ],
    "track list": pink_tuple[ 3 ]
}

print( pink_dictionary )



## 2) Iterate over the keys and values of the dictionary you create in exercise 1. For each key and value, you should print the name of the key, and then the value alongside it.

for key, value in pink_dictionary.items():
    print( f"{key}: {value}" )
    
    
    
## 3) Delete the track list and year of release from the dictionary you created. Once you've done this, add a new key to the dictionary to store the date of release. The date of release for The Dark Side of the Moon was March 1st, 1973.
del pink_dictionary[ "track list" ]
del pink_dictionary[ "release year" ]

pink_dictionary.update( { "release date": "March 1st, 1973" } )

print( pink_dictionary )

## 4) Try to retrieve one of the values you deleted from the dictionary. This should give you a KeyError. Once you've tried this, repeat the step using the get method to prevent the exception being raised.

# get track list key:

print( pink_dictionary.get("track list" ))
print( pink_dictionary.get( "release year" ) )
