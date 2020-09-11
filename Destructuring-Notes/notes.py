
#* -------------------- Standard Destructuring Assignments -------------------- #

# Assign two variables :
x, y = ( 1, 2 )

print(f"x = {x}, y = {y}")

## What's going on under the hood:
# Python is creating a tuple with two elements, 1 & 2, and then deconstructing (unpacking) the tuple to its constituent parts and assigning each one to the variables on the left of the = sign




#* ------------------------ Destructuring in for loops ------------------------ #

example_list = ["A", "B", "C"]

for counter, letter in enumerate( example_list ):
    print( f"{counter}: {letter}" )
    

people = [
	("Bob", 42, "Mechanic"),
	("James", 24, "Artist"),
	("Harry", 32, "Lecturer")
]

for (name, age, profession) in people:
	print(f"Name: {name}, Age: {age}, Profession: {profession}")
 
 


#* ------------------------------ Ignoring Values ----------------------------- #

## What do we do if we have a collection of values and we don't want to assign all of them? We use "_" in place of a variable name

person = ( "Bob", 42, "mechanic" )
name, _, profession = person

print( f"{name} is a {profession}" )

# NOTE: Useful for ensuring a specific number of operations without having to define the values iterated over:
for _ in range( 10 ):
    # <do stuff>
    pass



#* ------------------------ Using "*" to collect values ----------------------- #

## Recall that we use the *args operator to collect leftover values when performing a destructuring assignment. 

# Let's say we have a list of numbers and we want to grab the first number and then assign the remaining numbers to a second variable:
head, *tail = [1,2,3,4,5]
print( head ) # 1
print( tail ) # [2,3,4,5]

*head, tail = [1,2,3,4,5]
print( head ) # [1,2,3,4]
print( tail ) # 5


# NOTE: We can assign ANY number of variables, then gather up the remainder:
head, *middle, tail = [1,2,3,4,5]
print( head ) # 1
print( middle ) # [2,3,4]
print( tail ) # 5

first, second, third, *rest = [1,2,3,4,5]
print( rest ) # [4,5]

