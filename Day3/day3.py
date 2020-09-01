
# ---------------------------------------------------------------------------- #
#                               STRING FORMATTING                              #
# ---------------------------------------------------------------------------- #

string1 = "John is 24 years old"

#* to get this format this string, we can use:
string1_formatted = "{} is {} years old!".format( "John", 24 )
# the int 24 is automatically changed into a string


#* Format Function:
output = "{0} is {1} years old, and {0} works as a {2}."
print( output.format( "John", 24, "web developer"  ) )
# The placeholders (in brackets) will take the index of what's in the format function and fill the output string with that. (Good for repetitive replacements)

# You can also use the format function as follows:
output = "{name} is {age} years old, and {name} works as a {job}"
print( output.format( name="John", age=24, job="web developer" ) )


# -------------------- String Interpolation with f-strings ------------------- #
#* This method is an updated version of the above format function

name = "John"
age = 24

#* the f prior the string tells python to format automatically in the same way as above method
string = f"{name} is {age} years old!" 
print( "\nf-string is:" ), print( string )

# NOTE: we can do calculations DIRECTLY in the f-string:
string = f"{name} is {age*12} months old!"
print("\n", string)




# ---------------------------------------------------------------------------- #
#                            BASIC STRING PROCESSING                           #
# ---------------------------------------------------------------------------- #

string = "Hello, world!"

# lower case func:
print( "\n", string.lower() )

# upper case tool:
print( string.upper( ) )

# capitalize the first letter of a sentence:
print( string.capitalize( ) )

# title - every word starts with capital letter
print( "hello, world!".title( ) )


#* Removing white space from the end of a string (useful for user input)
string = " Hello, World! "
string_stripped = string.strip()
print( "String stripped:", string_stripped )


# ---------------------------------------------------------------------------- #
#*                                   EXERCISE                                   #
# ---------------------------------------------------------------------------- #

# 3) Concatenation
string = "I am"
integer = 29
new_string = string + " " + str(integer) #* Type Conversion!
print( new_string )

# 4) String Interpolationt
title = "Joker"
director = "Todd Phillips"
release_year = 2019

output = f"{title} ({release_year}), directed by {director}"
print( output )
