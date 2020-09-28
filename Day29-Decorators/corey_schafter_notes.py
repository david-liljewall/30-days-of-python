# Decorators

def outer_function():
    message = "Hi"
    
    def inner_function():
        print( message )
    
    return inner_function

outer_function()