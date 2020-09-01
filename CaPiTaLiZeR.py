# ---------------------------------------------------------------------------- #
#                              CaPiTaLiZeR Program                             #
# ---------------------------------------------------------------------------- #

## This program takes an entered string and returns it in an alternating caps format

import random # for random number generator, used in rand_capitalizer() func.


# ---------------------------- Function Definition --------------------------- #
def rand_capitalizer( ):
    
    rand_capitalized_string = ""
    
    for char in user_input:
        
        rand_int = random.randint( 1, 101)
        
        if rand_int % 2 != 0:
            # if odd, upper case
            rand_capitalized_string += char.upper()

        else:
            # if even, lower case    
            rand_capitalized_string += char.lower()
                
    print( rand_capitalized_string ) 
   
   
def alt_capitalizer( ):
    
    alt_capitalized_string = ""

    count = 1
    
    for char in user_input:
        
        if count % 2 == 0:
            # if odd, upper case
            alt_capitalized_string += char.upper()
            
        else:
            # if even, lower case    
            alt_capitalized_string += char.lower()
            
        count += 1  

    print( alt_capitalized_string )


# ------------------------------- Main Program: ------------------------------ #
user_input = input( "Enter text from someone that you'd like to mock: " )

option = input( "Enter 'r' for random capitalization or 'a' for alternating capitalization, or 'b' for both: "  )

print( "\n\n" ) # extra whitespace

if option == "r":
    rand_capitalizer( )
elif option == "a":
    alt_capitalizer( )
elif option == "b":
    rand_capitalizer()
    print("\n")
    alt_capitalizer()

