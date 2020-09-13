# ---------------------------------------------------------------------------- #
#*                  map, filter, and Conditional Comprehensions                 #
# ---------------------------------------------------------------------------- #

## Recall that list comprehensions go like:
    # list_to_create = [ (operation on item) for item in collection ]
# Recall a list comprehensions example:
names = [ "tom", "richard", "harold" ]
names = [ name.title() for name in names ]
print( names )




#* ---------------------------- The "map" function ---------------------------- #

## map is a function that allows us to call some other function on every item in an iterable. THIS IS POWERFUL. I.e., map a function to each item in an iterable, e.g. a collection

def cube( number ):
    return number ** 3

numbers = [1,2,3,4,5]
# NOTE: only pass in the name of the function (cube), not cube()
cubed_numbers = map( cube, numbers )

# A "map" object is created, whereby the values inside of it are only calculated when we need them making it very memory efficient. More memory efficient than the comprehensions we've used so far.

# To access the cubed_numbers, treat it like a collection:
for number, cubed_number in zip( numbers, cubed_numbers ):
    print( f"{number}^3 is {cubed_number}" )
    
# Since they're iterable, we can also unpack them using the * operator:
def cube(number):
	return number ** 3


numbers = [1, 2, 3, 4, 5]
cubed_numbers = map(cube, numbers)

print(*cubed_numbers, sep=", ")

# Can also convert them to a normal collection if we like:
def cube(number):
	return number ** 3


numbers = [1, 2, 3, 4, 5]
cubed_numbers = list(map(cube, numbers))
print( cubed_numbers )





#* ------------------------ map with Multiple Iterables ----------------------- #

# When we provide more than one iterable, map takes a value from each one when it calls the provided function, meaning the function gets called with multiple arguments. THE ORDER OF ARGUMENTS MATCHES THE ORDER IN WHICH WE PASSED THE ITERABLES TO map

def add( a, b ):
    return a + b

odds = [1,3,4,5,9]
evens = [2,4,6,8,10]

totals = map( add, odds, evens )

print( *totals, sep=", " ) # 3, 7, 10, 13, 19



#* ------------------------ map with lambda expressions ----------------------- #

# map is most often used for simple operations, meaning that lambda expressions can be utilized here!

numbers = [1,2,3,4,5]
cubed_numbers = map( lambda number: number ** 3, numbers )

print( *cubed_numbers, sep=", " )




#* ---------------------------- The operator module --------------------------- #

# The operator module in the standard library contains function versions of all the operators ( *, +, etc. ) which can be used in map() functions succinctly instead of writing out a whole lambda expression:
from operator import add, mul

odds = [1,3,5,7,9]
evens = [2,4,6,8,10]

added_totals = map( add, odds, evens )
print( *added_totals, sep=", " )

multiplied_totals = map( mul, odds, evens )
print( *multiplied_totals, sep=", " )


# There is a also a useful function in the operator module called "methodcaller". It allows us to easily define a function that calls a method for us. We just have to provide the method name as a string.

from operator import methodcaller

names = ["tom", "richard", "harold"]
title_names = map( methodcaller("title"), names )






#* ------------------------ Conditional Comprehensions ------------------------ #

# Let's say we have a set of numbers and only want the even values:
numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_numbers = [ number for number in numbers if number % 2 == 0 ]
even_numbers = { number for number in numbers if number % 2 == 0 }



#* ---------------------------- the filter function --------------------------- #
 
# We can rewrite the above conditional comprehension expression as:
numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_numbers = filter( lambda number: number % 2 == 0, numbers )

# or:
def is_even( number ):
    return number % 2 == 0

even_numbers = filter( is_even, numbers )

# NOTE: The filter function can only handle ONE ITERABLE AT A TIME


#* If we use None with filter --> we only get back the truthy values (e.g. non-empty collections)
values = [0, "Hello", [], {}, 435, -4.2, ""]
truthy_values = filter(None, values)

print(*truthy_values, sep=", ")  # Hello, 435, -4.2




# ---------------------------------------------------------------------------- #
#*                                   Exercises                                  #
# ---------------------------------------------------------------------------- #

## 1) Use map to call the strip method on each string in the following list:
humpty_dumpty = [
	"  Humpty Dumpty sat on a wall,  ",
	"Humpty Dumpty had a great fall;     ",
	"  All the king's horses and all the king's men ",  
	"    Couldn't put Humpty together again."
]

humpty_dumpty = list( map( lambda string: string.strip(), humpty_dumpty ) )

print( humpty_dumpty )


## 2) Below you'll find a tuple containing several names:
    # Use a list comprehension with a filtering condition so that only names with fewer than 8 characters end up in the new list. Make sure that every name in the new list is in title case.
names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine")

names = [ name.title() for name in names if len( name ) < 8 ]
print( names )


## 3) Use filter to remove all negative numbers from the following range: range(-5, 11). Print the remaining numbers to the console.

# Way 1:
new_range = filter( lambda number: number > 0, range( -5, 11 ) )

for number in new_range:
    print( number )

# Way 2:
def is_positive( number ):
    return number > 0

new_range = filter( is_positive, range( -5, 11 ) )

for number in new_range:
    print( number )
    
    
    
###### NOTE: There is version of filter in the itertools module called filterfalse which will only return for which the predicate (filtering function) returns a falsy value

# Ex: return only the negative values from range( -5,11 )
from itertools import filterfalse

new_range = filterfalse( lambda number: number >= 0, range( -5, 11 ) )

for number in new_range:
    print( number )