# ---------------------------------------------------------------------------- #
#                                COMPREHENSIONS                                #
# ---------------------------------------------------------------------------- #

## Comprehensions allow us to create a collection from some other iterable in a very succint way.


#* ---------------------------- List Comprehensions --------------------------- #

## Used to create a new list from some other iterable - another list, a zip object, etc.

names = ["mary", "Richard", "Noah", "KATE"]

# Want data in a consistent format, we would so something like:
processed_names = []

for name in names:
    processed_names.append( name.title( ) )
    
##* LIST COMPREHENSION WAY:
# Meaning -->  put name.title() in the new list for every name in names 
processed_names = [ name.title() for name in names ]
# or we can just reprocess the original names list: 
names = [ name.title() for name in names ]

print( names )


# We can do list comprehensions for more complicated variables, like a zip:
names = ("mary", "Richard", "Noah", "KATE")
ages = (36, 21, 40, 28)

people = []

for name, age in zip(names, ages):
	person_data = (name.title(), age)
	people.append(person_data)
# Recall that zip( names, ages ) combines the two lists into a list of tuples, where each element of names gets matched with the same index element in ages
 
##* List Comprehension way:
# Meaning --> put name.title(), age in new people list object for every name, age in zip
people = [ ( name.title(), age ) for name, age in zip( names, ages ) ]

print( people )


# Style NOTE: try and break things up like this if they get long:
people = [
	(name.title(), age)
	for name, age in zip(names, ages)
]



#* ---------------------------- Set Comprehensions ---------------------------- #

## Functions just like a list comprehension, but creates a set instead

names = ["mary", "Richard", "Noah", "KATE"]
names = { name.title() for name in names }




#* ------------------------- Dictionary Comprehensions ------------------------ #

student_ids = (112343, 134555, 113826, 124888)
names = ("mary", "Richard", "Noah", "KATE")

students = {}

for student_id, name in zip(student_ids, names):
	student = {student_id: name.title()}
	students.update(student)
 
##* Dictionary Comprehension way:
# Create a dictionary of tuples
students = {
    ## NOTE: key syntax --> key: value
    student_id: name.title( ) 
    for student_id, name in zip( student_ids, names )
}

print( students )



#* ------------------------- Comprehensions and Scope ------------------------- #


## NOTE: unline for loops (i.e., for name in names:) we cannot refer to list comprehension variables OUTSIDE of the comprehensions statement itself. They are scoped only within the statement. 
## This is because LIST COMPREHENSIONS ARE FUNCTIONS, so just like with user-defined functions, the variables defined within the function scope cannot be accessed within any other scope.

## Inside the comprehension function, we're actually creating an entirely new list, and we're assigning this list to a temporary name. We're therefore not modifying the original iterable while we populate our new list. Only when we're done do we return the new list and potentially replace the existing value assigned to the variable.



# ---------------------------------------------------------------------------- #
#*                                   Exercises                                  #
# ---------------------------------------------------------------------------- #

## 1) Convert the following for loop into a comprehension:
    # numbers = [1, 2, 3, 4, 5]
    # squares = []

    # for number in numbers:
    # 	squares.append(number ** 2)numbers = [1, 2, 3, 4, 5]
    # squares = []

    # for number in numbers:
    # 	squares.append(number ** 2)
    
numbers = [ 1, 2, 3, 4, 5 ]

squares = [ ( number ** 2 ) for number in numbers ]
print( squares )

## 2) Use a dictionary comprehension to create a new dictionary from the dictionary below, where each of the values is title case.

movie = {
	"title": "thor: ragnarok",
	"director": "taika waititi",
	"producer": "kevin feige",
	"production_company": "marvel studios"
}
    
movies = {
    key: value.title()
    for key, value in movie.items()
}

print( movies )


## 