# ---------------------------------------------------------------------------- #
#                              FIZZ BUZZ PROJECT!                              #
# ---------------------------------------------------------------------------- #

# play 100 rounds off fizz buzz

for number in range( 1, 100 ):
    
    if number % 3 == 0 and number % 5 == 0:
        print( "Fizz Buzz" )
    elif number % 3 == 0:
        print( "Fizz" )
    elif number % 5 == 0:
        print( "Buzz" )
    else:
        print( number )
        
    
        