# ---------------------------------------------------------------------------- #
#*                                  FUNCTIONS!!                                 #
# ---------------------------------------------------------------------------- #
# ------------------------------------ -- ------------------------------------ #



## Defining our First Function:
def get_even_numbers( amount ):
    for number in range( 2, amount + 1, 2 ):
        print( number )
        
# Calling the function:
get_even_numbers( 22  ) 
        

#* ---------------------- Specifying multiple parameters ---------------------- #

# Define a function x_print() which accepts a string to print, and a number of times to print that string:

def x_print( string, number ):
    print( "\n" ) # add whitespace before printing
    for _ in range( 0, number ):
        print( string )
        
# Call function to print "Hello!" 5 times:
x_print( "Hello", 5 )

# Call function to print "Hello, world" to print 10 times:
string_to_print = "Hello, world"
times_to_print = 10
x_print( string_to_print, times_to_print )


## DEFAULT-VALUED FUNCTION:
def x_print_default( string="Hello!", number=2 ):
    print( "\n" ) # add whitespace before printing
    for _ in range( 0, number ):
        print( string )

x_print_default(  )
x_print_default( "WAZZAP", 5 )



## KEYWORD ARGUMENTS:   

# We can directly tie an argument's value to a parameter name, AND THE ORDER DOESN'T MATTER!
x_print( string="Hello", number=5 )
x_print( number=5, string="Hello" )


# NOTE: If we want to mix positional and keyword arguments, you MUST keep them in order:
x_print( "Hello", number=5 )


print( "\n\n" )
# ---------------------------------------------------------------------------- #
#*                                   Exercises                                  #
# ---------------------------------------------------------------------------- #

## 1) Define four functions: add, subtract, divide, and multiply. Each function should take two arguments, and they should print the result of the arithmetic operation indicated by the function name.

def add( number1, number2 ):
    print( f"{number1} + {number2} = {number1 + number2}" )
    
def subtract( number1, number2 ):
    print( f"{number1} - {number2} = {number1 - number2}" )
    
def multiply( number1, number2 ):
    print( f"{number1} * {number2} = {number1 * number2}" )
    
def divide( number1, number2 ):
    if number2 != 0:
        print( f"{number1} / {number2} = {number1 / number2}" )
    else:
        print( "Warning - you are trying to divide by zero and destroy the universe" )
        
        
        
var_range = range( 0, 5 )

for _ in var_range:
    add( _, _ )
    subtract( _, _ )
    multiply( _, _ )
    divide( _, _ )
    
    
## 2) Define a function called print_show_info that has a single parameter. The argument passed to it will be a dictionary with some information about a T.V. show. 

def print_show_info( show=dict ):   
    print( f"{ show.get('title') } ({ show.get('initial_release') }) - { show.get('seasons') } seasons " )
    
      
tv_show = {
"title": "Breaking Bad",
"seasons": 5,
"initial_release": 2008
}

print_show_info( tv_show )



## 3) Use your function, print_show_info, and a for loop, to iterate over the series list, and call your function once for each iteration, passing in each dictionary. You should end up with each series printed in the appropriate format.

series = [
    
    {"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
    {"title": "Fargo", "seasons": 4, "initial_release": 2014},
    {"title": "Firefly", "seasons": 1, "initial_release": 2002},
    {"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
    {"title": "True Detective", "seasons": 3, "initial_release": 2014},
    {"title": "Westworld", "seasons": 3, "initial_release": 2016},

]

## NOTE: IMPORTANT USAGE RIGHT HERE
for show in series:
    print_show_info( show )
    


## 4) Create a function to test if a word is a palindrome. A palindrome is a string of characters that are identical whether read forwards or backwards. For example, “was it a car or a cat I saw” is a palindrome.


# WAY 1:
def palindrome_test( string=str ):

    # First, process the input: strip whitespace, convert to lower case for comparison:
    string = string.strip().lower()
    
    # get rid of whitespace between letters for proper string comparison:
    processed_string = ""
    
    for character in string:
        if character != " ":
            processed_string += character  
            print( processed_string )      
    
    # String comparison:
    if processed_string == processed_string[ ::-1 ]:
        print( f"{string} IS a palindrome!" )
    else:
        print( f"{string} IS NOT a palindrome!" )
        

# test:
word = "was it a car or a cat I saw"
palindrome_test( word )




# ---- NOTE: the following string comparison using "is" WILL NOT WORK!!!! ---- #
string = "hannah"
print( string is string[ ::-1 ] ) #* False --> "is" checks if they point to the same OBJECT, not that they are equivalent strings. 

string = "hannah"
string2 = "hannah"
print( string is string2 ) # TRUE --> string and string2 actually do point to the same object, therefore this test works
print( id( string ), id( string2 ) )