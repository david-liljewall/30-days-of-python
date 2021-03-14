# ---------------------------------------------------------------------------- #
#*                              EXCEPTION HANDLING                              #
# ---------------------------------------------------------------------------- #


#* ---------------------------- The "try" statement --------------------------- #

# The following code will loop till the user enters a valid whole number, i.e., does not receive a ValueError

while True:
    try:
        number = int( input( "Please enter a whole number: " ) )
        break
    except ValueError:
        print( "You didn't enter a valid integer!" )
        



     
#* ----------------------- Handling multiple exceptions ----------------------- #

## Let's imagine that we have two different exceptiuons that might occur, and we want to do different things depending on what happens. In this case we should have TWO except clauses where each one describes the course of action for that specific exception case


# Ex: create a function that calcs the mean from a collection of numbers. We don't know what the user will pass in.
    # Potential Issues:
    # 1.) User may pass in an empty collection, so len() = 0, leading to a ZeroDivisionError
    # 2.) User may pass something that isn't a collection, giving a TypeError since fsum() and len() expect a collection
    # 3.) User may pass in a collection which contains things that are not numbers - TypeError
    
import math

def average( numbers ):
    try:
        mean = math.fsum( numbers ) / len( numbers )
        print( mean )
    except ZeroDivisionError:
        print( 0 )
    except TypeError:
        print( "You provided invalid values!" )

# ZeroDivisionError:
numbers = []
average( numbers )

# Type Error:
numbers = [1,2,3,4,"Billy"]
average( numbers )



# NOTE: We can also capture multiple exceptions like so!:
def average( numbers ):
    try:
        mean = math.fsum( numbers ) / len( numbers )
        print( mean )
    except ( ZeroDivisionError, TypeError ):
        print( "An average cannot be calculated for the values you provided." )
        
# ZeroDivisionError:
numbers = []
average( numbers )

# Type Error:
numbers = [1,2,3,4,"Billy"]
average( numbers )



#* ------------------------------ The ELSE clause ----------------------------- #

## In addition to the try and except clauses, we can also use an else clause with our try statements. The code under the else clause only runs if no exceptions occur while executing the code in the try clause.

# When finding out about else I know a lot of students think it's totally useless. Can't we just put more code in the try block?

# We can, but here are a couple of reasons why this can be a really bad idea.

#     We may accidentally catch exceptions we didn't anticipate. The more code that ends up in the try clause, the more likely this is to happen. This may make our handling of the exception inappropriate, because we're left dealing with a situation which didn't actually occur.
#     It harms readability. The try clause expresses what we expect to fail, and the except clauses express the ways that we plan to handle specific failures in that code. The more code that gets added to the try clause, the less clear it is what we're actually trying, and that can make the whole structure more difficult to understand.
    
    
# NOTE: TL;DR ---> Since the TRY portion of the code holds code we expect to fail, the ELSE portion will hold the end goal of the portion of code assuming no exceptions had to be handled.

# In the case of the above average() code, we can rewrite it like:

import math

def average( numbers ):
    try:
        mean = math.fsum( numbers ) / len( numbers )
    except ZeroDivisionError:
        print( 0 )
    except TypeError:
        print( "You provided invalid values!" )
    
    else:
        print( mean ) # --> This is the end goal of this function
        
# ZeroDivisionError:
numbers = []
average( numbers )

# Type Error:
numbers = [1,2,3,4,"Billy"]
average( numbers )

# No error:
numbers = [1,2,3,4]
average( numbers )






#* ---------------------------- The FINALLY clause ---------------------------- #

## The "finally" clause WILL ALWAYS RUN!!
    # If an unhandled exception occurs, it doesn't matter. finally will still run its code BEFORE that exception terminates the program!

def finally_flex( number ):
    try:
        print( number )
    finally:
        print( "You return when I say you can return..." )
        
finally_flex( 20.25425 ) # it prints the number, then prints "You return..."




# ---------------------------------------------------------------------------- #
#*                                   EXERCISES                                  #
# ---------------------------------------------------------------------------- #

## 1) Create a short program that prompts the user for a list of grades separated by commas. Split the string into individual grades and use a list comprehension to convert each string to an integer. You should use a try statement to inform the user when the values they entered cannot be converted.

def grade_list( grades=str ):
    # Create list from entered string
    grade_list = grades.strip().split( "," )
    
    try:
        # In case there is whitespace BETWEEN each grade, do .strip() on each grade:
        grade_list = [ int( grade.strip() ) for grade in grade_list ]
        
    except ValueError:
        # Handles the following exceptions: not a string, empty string
        print( "The data you have entered is not a string." )
        
    else:
        print( "Grade List:", grade_list )


grades = input( "Enter a list of grades separated by commas: " )        

grade_list( grades )


## 2) Investigate what happens when there is a return statement in both the try clause and finally clause of a try statement.

def try_finally_return(a, b):
    try:
        return a + b
    except ValueError:
        print( "oops" )
    finally:
        return a / b
    
c = try_finally_return( 1, 2 )

print( c )

## NOTE: We see that because the finally clause always runs and interrupts the return statement in the try clause - it puts the try clause return statement on hold and only returns what's in the finally clause.



## 3) Imagine you have a file named data.txt with this content:

def open_data( file ):
    try:
        with open( file, mode="r") as f:
            data = f.readlines()
            
            print( data )
            
    except FileNotFoundError:
        print( "File specified was not found..." )
        
# After deleting the file, we see the exception thrown
open_data( "./data.txt" )