# ---------------------------------------------------------------------------- #
#*                                   EXERCISES                                  #
# ---------------------------------------------------------------------------- #

# Make a decorator which calls a given function twice. You can assume the functions don't return anything important, but they may take arguments.

# Imagine you have a list called books, which several functions in your application interact with. Write a decorator which causes your functions to run only if books is not empty.

# Write a decorator called printer which causes any decorated function to print their return values. If the return value of a given function is None, printer should do nothing.
from typing import Callable, List, Union
from functools import wraps


# ------------------- Decorator that calls a function twice ------------------ #
def call_twice( func: Callable ) -> Callable:
    @wraps( func )
    def inner( *args, **kwargs ):
        print( f"First call of {func.__name__}..." )
        func()
        print( f"Second call of {func.__name__}..." )
        func()
        
    return inner

@call_twice
def called_function():
    print( "Hello sailor" )

called_function()



# ------ Decorator that runs a function only if books list is not empty ------ #
def run_if_not_empty( func: Callable ) -> Callable:
    @wraps( func )
    def inner( books: List[ str ] ):
        if books:
            func( books )
                
    return inner

@run_if_not_empty
def print_list( gen_list: List[ str ] ):
    for counter, item in enumerate( gen_list, start=1 ):
        print( f"Item {counter}: {item}" )

        
non_empty_books: List[ str ] = [ "To Kill a Mockinbird", "Absalom! Absalom!" ]
empty_books: List[ None ] = []

print_list( non_empty_books )
print_list( empty_books )




## Decorator which causes any decorated function to print their return values. If the return value of a function is None, do nothing
def printer( func: Callable ) -> Callable:
    @wraps( func )
    def inner( *args, **kwargs ):
        return_value = func( *args, **kwargs )
        
        if return_value is not None:
            print( return_value )
        else:
            print( "Do nothing -> function doesn't return anything" )   
        
    return inner
    
Real = Union[ int, float ]

@printer
def add( a: Real, b: Real ) -> Real:
    return a + b
    
add( 1, 2 )

@printer
def empty_func():
    pass # don't return anything
    
empty_func() # triggers the else statement within the inner function the print decorator