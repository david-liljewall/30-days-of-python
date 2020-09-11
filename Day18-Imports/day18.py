# ---------------------------------------------------------------------------- #
#*                                    IMPORTS                                   #
# ---------------------------------------------------------------------------- #


import math

print( math.pi * (5 ** 2) ) # pi * 5^2

## fsum() --> adds together floating point numbers. If we use just sum(), we will get weird results because of the nature of floating point numbers.
    # See: https://blog.tecladocode.com/decimal-vs-float-in-python/ for more information
    
numbers = [ 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ]
print( math.fsum( numbers ) ) # we get exactly 1.0




#* ------------------ Importing specific things from modules ------------------ #

## We can import specific parts of a module - let's say we just want the constant pi:
from math import pi, tau

# NOTE: now when we want to call those constants above, we do not need the math. prior to it:
print( pi, tau )



#* -------------------------- Modules and Namespaces -------------------------- #

import math
print( globals() ) # NOTE: we can see that the functions/parameters live only in the math namespace, which means we need to access them via the . (dot) operator. I.e., math.pi, math.fsum(), etc.


from math import pi, tau
print( globals() ) # NOTE: we can see here that pi and tau are included in the global namespace and are used as variables just like if we defined them




#* ------------------------------ Aliased Impots ------------------------------ #

## We can import modules as an alias we define, to make accessing it more streamlined. A common convention for numpy is to import as "np". Now when we call the module, we just do np._
import numpy as np




# ---------------------------------------------------------------------------- #
#*                                   Exercises                                  #
# ---------------------------------------------------------------------------- #

## 1) Import the fractions module and create a Fraction from the float 2.25. You can find information on how to create fractions in the documentation.
import fractions as fr

print( fr.Fraction( 2.25 ) )

## 2) Import only the fsum function from the math module and use it to find the sum of the following series of floats:
from math import fsum

numbers = [1.43, 1.1, 5.32, 87.032, 0.2, 23.4]

print( fsum( numbers ) )

## 3) Import the random module using an alias, and find a random number between 1 and 100 using the randint function. You can find documentation for this function here.
import random as rand

print( rand.randint( 1, 100 ) )

## 4) Use the randint function from the exercise above to create a new version of the guessing game we made in day 8. This time the program should generate a random number, and you should tell the user whether their guess was too high, or too low, until they get the right number.

rand_int = rand.randint( 1, 20 )
print( rand_int )

while True:
    guess =  int( input( "Guess an integer between 1 and 20: " ) )
    
    if guess == rand_int:
        print( "You guessed the correct number!" )
        break
    else:
        print( "Nope, try again" )