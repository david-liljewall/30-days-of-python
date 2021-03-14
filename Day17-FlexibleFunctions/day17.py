# ---------------------------------------------------------------------------- #
#*                  Flexible Functions with *args and **kwargs                  #
# ---------------------------------------------------------------------------- #

## How do we make a function that accepts as many arguments as the user provides? So far we need to know how many values we're going to accept in advance. But, take the print() function for example -- you can write print( a, b, c, d, etc... ) and it will work just fine regardless of the number of parameters passed into it.



#* ----------- Accepting an arbitrary number of positional arguments ---------- #



##* To accept any number of positional arguments, we use the "args" parameter, denoted by "*". Python gathers any unassigned positional arguments when we call the function and puts them all in a tuple, assigned to the * parameter

# NOTE: Since we know we want to print names, we should use *names. If we wanted more general inputs, then *args would be more appropriate
def multigreet( *names ):
    for name in names:
        print( f"Hello, {name}!" )
        
# We can now pass in any arbitrary number of parameters!
multigreet( "Rolf", "Bob", "Anne" )
multigreet( "Billy", "Bob", "Jaundice", "Karen" )




#* ------------------------ Parameter Order with *args ------------------------ #

## When we use a parameter like *args, order of parameters is paramount. ANY PARAMETER WE DEFINE AFTER THE *args CANNOT ACCEPT POSITIONAL ARGUMENTS.
    # i.e. --> Put the *args keyword AFTER other predefined parameters for functions
    
def multigreet( other, *names ):
    for name in names:
        print( f"Hello, {other} {name}!" )

## NOTE: this "flexible" function can also be used in the form multigreet( *names ) without ever using the "other" paraemeter
multigreet( "other", "Billy", "Bob" )



#* ------------ Accepting an arbitrary number of keyword arguments ------------ #



## Let's look at an example of using dict() with keyword arguments:
dictionary = dict( name="Phil", age=29, city="Budapest", nationality="British" )
print( dictionary )

# The dict() function doesn't know how many keys and values we're going to enter, therefore it is flexible w.r.t. keyword arguments


##* We can accomplish the same flexibility as above using the "**" parameter, or "**kwargs" parameter

def pretty_print( **kwargs ):
    for key, value in kwargs.items():
        print( f"{key}: {value}" )

pretty_print( title="The Matrix", director="Wachowski", year=1999 )

# NOTE: The **kwargs parameter collects all unassigned keyword arguments and creates a dictionary with them that you can use in your function. That's why we use kwargs.items



#* ------------------------ Other uses for "*" and "**" ----------------------- #

## What if we want to unpack (destructure) an iterable so that we can pass many values to *args? We just put a "*" before the iterable we're passing in as an argument.

# Ex: take a list of numbers and print them on a single line with the "|" character in between each number:
numbers = [1,2,3,4,5]
print( *numbers, sep=" | " )

# Ex 2: Destructure a dictionary with **kwargs
def print_movie( **kwargs ):
    for key, value in kwargs.items():
        print( f"{key}: {value}" )
        
movie = {
    "title": "The Matrix",
    "director": "Wachowski",
    "year": 1999
}
# Remember to pass in the ** parameter before the argument of the function, just like it is defined above
print_movie( studio="Warner Bros", **movie ) # this takes an initial keyword argument to add to the dictionary, then the **movie argument collects the rest of the arguments into the same dictionary


#* Ex 3: Merging Dictionaries:
def show_books( books ):
    print() # whitespace
    
    for book in books:
        print( "{title}, by {author} ({year})".format( **book ) )
        
    print() # extra whitespace
    
books = [{
    "title": "1Q84",
    "author": "Haruki Murakami",
    "year": "2004"
}]

show_books( books )

# we could even define the string template placeholder elsewhere:
book_template = "{title}, by {author} ({year})"

def show_books( books ):
    print() # whitespace
    
    for book in books:
        print( book_template.format( **book ) )
        
    print() # extra whitespace
    
show_books( books )



# ---------------------------------------------------------------------------- #
#*                                   Exercises                                  #
# ---------------------------------------------------------------------------- #

## 1) Create a function that accepts any number of numbers as positional arguments and prints the sum of those numbers. Remember that we can use the sum function to add the values in an iterable.

def sum_numbers( *nums ):
    sum_num = sum( nums )
    print( sum_num )
    
sum_numbers(1,2,3,4,5)

## 2) Create a function that accepts any number of positional and keyword arguments, and that prints them back to the user. Your output should indicate which values were provided as positional arguments, and which were provided as keyword arguments.

def print_args( *args, **kwargs ):
    print( f"Positional Arguments: {args}" )
    print( f"Keyword Arguments: {kwargs}" )
    
print_args( "Hi ", "Billy", key1="key1", key2="key2" )


## 3) Print the following dictionary using the format method and ** unpacking.
country = {
"name": "Germany",
"population": "83 million",
"capital": "Berlin",
"currency": "Euro"
}

def print_country( country ):
    print( "{name} has a population of {population}, capital is {capital}, and the currency is the {currency}".format( **country ) )

    
print_country( country )

## 4) Using * unpacking and range, print the numbers 1 to 20, separated by commas. You will have to provide an argument for print function's sep parameter for this exercise.

print( *range(1, 21 ), sep = ", " )


## 5) Modify your code from exercise 4 so that each number prints on a different line. You can only use a single print call.

print( *range(1, 21 ), sep = "\n" )
