# ---------------------------------------------------------------------------- #
#                                  DECORATORS                                  #
# ---------------------------------------------------------------------------- #


## Decorators take in a function and return a NEW FUNCTION which can do something more than the function we passed in.
    
    # Decorators allow us to easily provide additional functionality to functions in our applications. They are used often in standard library and third party modules
    

#* ------------------------ Defining a simple decorator ----------------------- #

from typing import Callable

def example_decorator( func: Callable ) -> Callable:
    def inner():
        print( f"Now calling {func.__name__}..." )
        func()
        print( f"{func.__name__} has ended." )
        
    return inner

    # We have a single parameter for the decorator which is a function. Inside the function body, we've defined a new function which prints a line to the terminal, then calls func (the parameter function for the decorator), then prints another line to the terminal. __name__ lets us find a name of a funcition. At the end, we return a reference to the inner function
    

def greeter():
    print( "Hello!" )

print( greeter ) # reference to above function

greeter = example_decorator( greeter )
    # We've called the example_decorator function and passed in a REFERENCE to the greeter function. We've then assigned the return value (the reference to inner function) to greeter, replacing the old greeter function. Now the name greeter refers to something completely different.
print( greeter ) # reference to new greeter function, which refers to the returned inner function reference

greeter() # NOTE: Now when we call greeter(), we are now calling inner() from the decorator



#* ------------------------------ The "@" syntax ------------------------------ #

## Instead of doing greeter = example_decorator( greeter ), we can do:

@example_decorator
def greeter():
    print( "Hello!" )

    # We "decorate" a function by putting this syntax above the function we want to decorate
    
greeter()



#* -------------------- Decorating Functions with Arguments ------------------- #

## How would we decorate a function like this:
def add( a, b ):
    print( a + b )
    
    # If we tried our above method, we'd end up with a TypeError because when we call func in in the inner function, we've been calling it without arguments
    
    
# NOTE: To fix this, we have to define a set of parameters for our "inner" function, and we can pass the arguments on when we call func. We will use *args and **kwargs to accept any set of arguments we like for inner() and then pass them right along to the func()
 
from typing import Callable, Union

Real = Union[ int, float ] # i.e. a Real number

def calculate( func: Callable ) -> Callable:
	def inner( *args, **kwargs ):
		print( "Calculating..." ) 
		func( *args, **kwargs )
	
	return inner


@calculate
def add( a: Real, b: Real ) -> Real:
	print( a + b )

add( 1, 5 )

@calculate
def summation( *args: Real ) -> Real:
    print( f"The sum of {args} is:", sum( args ) )

summation( 1, 2, 3, 4 )




#* ------------------ Decorating functions with return values ----------------- #
print( "\n\n" )
## What if the function we're decorating returns a value?

# Ex: a silly decorator which gives the wrong answer for our calculations:
from typing import Callable, Union

Real = Union[ int, float ]

def wrong_answer( func: Callable ) -> Callable:
    def inner( *args, **kwargs ):
        return func( *args, **kwargs ) + 1 #* Return this value

    return inner #* Still return reference to inner function

@wrong_answer
def add( a: Real, b: Real ) -> Real:
    return a + b
    # NOTE: This decorated function add() will be substituted into inner() in wrong_answer(). Therefore instead of returning a + b, it will return (a + b) + 1

print( add( 1, 5 ) ) # returns 7 instead of 6


#* ---------------------------- The wraps function ---------------------------- #

from functools import wraps

## Wraps allows us to decorate our inner functions while preserving the original name of the function we passed into the decorator. Wraps is a decorator factory --> IT RETURNS A DECORATOR

from functools import wraps
from typing import Callable

def example_decorator(func: Callable) -> Callable:
	@wraps(func) # WRAPS SYNTAX IS JUST LIKE THE ABOVE DECORATOR SYNTAX
	def inner():
		print(f"Now calling {func.__name__}...")
		func()
		print(f"{func.__name__} has ended.")
	
	return inner


def greeter():
    print("Hello!")


greeter = example_decorator(greeter)
print(greeter)  # NOTE: <function greeter at 0x7fcce99a8830>, instead of <function example_decorator.<locals>.inner at 0x7f6e06326830>




#* ---------------------------- REAL WORLD EXAMPLE ---------------------------- #
print( "\n\n" )
##* We will be creating a decorator that will time our code for us --> this allows us to test several implementations to see which is faster on average

from functools import wraps
from math import fsum
from time import perf_counter
from typing import Callable, List, Set


# Define decorator function to time our code:
def stopwatch( func: Callable ) -> Callable:
    @wraps( func )
    def inner( *args, **kwargs ):
        times = []
        
        for _ in range( 10 ):
            start_time = perf_counter() # marks time right before function call
            func( *args, **kwargs )
            stop_time = perf_counter() # marks time right after function completion
            
            elapsed = stop_time - start_time
            times.append( elapsed )
        
        average_time = fsum( times ) / len( times )
        
        print( f"{func.__name__} ran in {average_time:.5f}s on average" )
            
    return inner

# Let's test if it is faster to make a list of 100,000 numbers with a 1) List or 2) Set

@stopwatch
def make_list( size: int ) -> List:
    return list( range( size ) )

@stopwatch
def make_set( size: int ) -> Set:
    return set( range( size ) )

make_list( 100_000 )
make_set( 100_000 )




