from functools import wraps

#* --------------------------- Classes as decorators -------------------------- #
class decorator_class( object ):
    
    def __init__( self, original_function ):
        self.original_function = original_function
        
        
    def __call__( self, *args, **kwargs ):
        print( f"decorator_class call method called this before {self.original_function.__name__} function..." )
        return self.original_function( *args, **kwargs )
    

@decorator_class
def display_info( name, age ):
    print( f"display_info ran with arguments ({name}, {age})" )
    
display_info( "John", 21 )




# -------------------------- Functions as Decorators ------------------------- #
print( "\n\n" )

def decorator_function( original_function ):
    def wrapper_function( *args, **kwargs ):
        print( f"wrapper executed this before {original_function.__name__} function..." )
        return original_function( *args, **kwargs )
        
    return wrapper_function


@decorator_function
def display():
    print( "display function ran" )
    
display()


@decorator_function
def display_info( name, age ):
    print( f"display_info ran with arguments ({name}, {age})" )
    
display_info( "John", 21 )


# ---------------------------------------------------------------------------- #
#                       PRACTICAL EXAMPLES OF DECORATORS                       #
# ---------------------------------------------------------------------------- #

# Keeps track of how many times a function was run and what arguments were passed to it
def my_logger( orig_func ):
    import logging
    logging.basicConfig( filename=f"{orig_func.__name__}.log", level=logging.INFO )
    
    @wraps( orig_func )
    def wrapper( *args, **kwargs ):
        logging.info(
            f"Ran with args: {args} and kwargs: {kwargs}"
        )
        return orig_func( *args, **kwargs )
    
    return wrapper

# Times
def my_timer( orig_func ):
    import time
    
    @wraps( orig_func )
    def wrapper( *args, **kwargs ):
        t1 = time.time()
        result = orig_func( *args, **kwargs )
        t2 = time.time() - t1
        print( f"{orig_func.__name__} ran in: {t2:.20f} seconds" ) 
        
        return orig_func( *args, **kwargs )
    
    return wrapper


@my_logger
def display_info( name, age ):
    print( f"display_info ran with arguments ({name}, {age})" )
    
display_info( "Billy", 202 )

@my_timer
def display_info( name, age ):
    print( f"display_info ran with arguments ({name}, {age})" )
    
display_info( "Billy", 202 )




#* ------------- Using multiple decorators with a single function ------------- #

@my_timer
@my_logger
def display_info( name, age ):
    print( f"display_info ran with arguments ({name}, {age})" )
    
display_info( "johnny", 12 )







#* ---------------------- Decorator that takes arguments ---------------------- #
# NOTE: This is rare, but sometimes used. Used in some Flask library functions

def prefix_decorator( prefix ):
    #Adds a prefix to each wrapper_function print statement
    def decorator_function( func ):
        # Add functiocnality of printing the func name before and after execution
        def wrapper_function( *args, **kwargs ):
            print( f"{prefix} Executed before {func.__name__}" )
            result = func( *args, **kwargs )
            print( f"{prefix} Executed after {func.__name__}\n" )
            
            return result
        
        return wrapper_function
    
    return decorator_function


@prefix_decorator( "TESTING:" )
def display_info( name, age ):
    print( f"display info ran with arguments ({name} and {age})" )
    
display_info( "John", 25 )
display_info( "Travis", 30 )