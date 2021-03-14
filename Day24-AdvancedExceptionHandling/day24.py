# ---------------------------------------------------------------------------- #
#              Advanced Exception Handling and Raising Exceptions              #
# ---------------------------------------------------------------------------- #



#* LookupError 
	# Used any time a key or index is not found (KeyError, IndexError)
numbers = [1, 2, 3, 4, 5]

try:
	print(numbers[100])  # <- Out of range index
except IndexError:
	print("The requested index is out of range")
except LookupError:
	print("Could not retrieve that value.")
 
	# NOTE: Useful exception to handle when working with sequences and mapping types like dictionaries. Is a good fallback if we don't catch specific exceptions
	
person = {
	"name": "Phil",
	"city": "Budapest"
}

try:
	print(person["age"])  # <- Referencing an undefined key
except IndexError:
	print("The requested index is out of range")
except LookupError:
	print("Could not retrieve that value.")
 
 
 
#* --------------------- Accessing the original Exception --------------------- #

## You can access the original exception message, 
numbers = [1, 2, 3, 4, 5]

try:
	print(numbers[100])  # <- Out of range index
except LookupError as ex:
	print(f"Error: {ex}")
 
print( "\n\n" ) # extra whitespace
 
 
#* --------------------------- Raising an Exception --------------------------- #

# When building our applications, we may encounter situations where we're unable to recover from an exception that we've tried to handle, or where we know in advance that an operation we want to perform is going to be impossible.

# In situations like these, it's important that we know how to raise exceptions ourselves, so that we can terminate the program with a meaningful error message.

# raise ValueError("I raised this ValueError for no reason!")


#* -------------------------- Reraising an Exception -------------------------- #

# We can also use raise in another way inside an except clause. By writing raise without specifying an exception, we can reraise the exception we caught in our except clause.

# This is very useful in cases where we don't actually want to stop an exception from happening, we just want to do something with the exception before the exception terminates the application.

# Once again, logging is a good example here. We may want to use information from the original exception for our logs so that we have a permanent record of what went wrong, and then we can allow the exception to terminate the program.

## You can access the original exception message, 
# numbers = [1, 2, 3, 4, 5]

# try:
# 	print(numbers[100])  # <- Out of range index
# except LookupError as ex:
#     print(f"\n\n<< [Insert things to do before exception terminates the program]>>")
#     raise ex
# NOTE: As we can see, the print statement is given befoer the exceptions are raised. We could do something like print that statement to a log file before the program terminates.


#* --------------------------- Nested try statements -------------------------- #
#* --------------------------- Controlling Traceback -------------------------- #

# Let's say that I'm going to be reading a very large number of numbers from a file, and I want to convert the string representation of each of these numbers to an integer. I'm fairly certain that nearly all of the numbers are going to be integers, but every now and again, I may run across a string representation of a float instead.

# If we try to pass a string representation of a float to the int function, for example "93.2", the program is going to terminate, because a ValueError will be raised by int.

# To get around this, I'm going to define a function that is going to do the conversion for us. Inside this function I'm first going to try to convert the number to an integer using int, and if this fails, I'm going to try to convert it to a float instead.

# Should the integer conversion go well, I'm just going to return the new integer. If we get a float, I'm going to round that float using the round function, and then I'm going to return the resulting integer

# def intify(number):
# 	try:
# 		return int(number)
# 	except ValueError:
# 		try:
# 			f_number = float(number)
# 		except ValueError:
# 			raise ValueError(f"could not convert string to an integer: {number}") from None
#                 # NOTE: the from keyword lets us specify a point from whihc we want to start the traceback information. We can either write the exception name, or write None which gets rid of all the excess traceback information from the try statement, and leaves the most recent exception
# 		else:
# 			return round(f_number)


# with open( "./numbers.txt", mode="r" ) as numbers_file:
# 	numbers = [ intify(number) for number in numbers_file ]
 




# ---------------------------------------------------------------------------- #
#*                                   Exercises                                  #
# ---------------------------------------------------------------------------- #


## 1) Ask the user for an integer between 1 and 10 (inclusive). If the number they give is outside of the specified range, raise a ValueError and inform them that their choice was invalid.

user_input = int( input( "Enter an integer between 1 and 10: " ) )

if user_input not in range( 1, 11 ):
	raise ValueError( f"Your entry of {user_input} is outside the range!" )


## 2) Below you'll find a divide function. Write exception handling so that we catch ZeroDivisionError exceptions, TypeError exceptions, and other kinds of ArithmeticError.

def divide( a, b ):
	try:
		print( a / b )
	except ZeroDivisionError:
		print( f"You entered {b} for b, and the universe explodes!" )
	except TypeError:
		print( f"You entered " )
		
		
## 3) Below you'll find an itemgetter function that takes in a collection, and either a key or index. Catch any instances of KeyError or IndexError, and write the exception to a file called log.txt, along with the arguments that caused this issue. Once you have written to the log file, reraise the original exception.

def log_exception(exception, fn, **kwargs):
    values = ", ".join( f"{key}={value!r}" for key, value in kwargs.items() )
		

def itemgetter(collection, identifier):
    try:
        return collection[ identifier ]
    except ( IndexError, KeyError, TypeError ) as ex:
        log_exception( ex, "itemgetter", collection=collection, identifier=identifier )
        raise
    
test_dictionary = { "key1": 1, "key2": 2 }

# IndexError Test:
test_dictionary[ "key1" ]

# KeyError Test:
test_dictionary[ "key3" ]
