# ---------------------------------------------------------------------------- #
#                               IDIOMATIC PYTHON                               #
# ---------------------------------------------------------------------------- #



#* ------------------------ Truth values as conditions ------------------------ #

## Instead of doing this:
my_list = []

if len(my_list) == 0:
	print("The list is empty")
else:
	values = ', '.join(str(value) for value in my_list)
	print("The list contains: {values}")
 
## "pythonic" code looks like this:
my_list = []

if my_list:
	values = ', '.join(str(value) for value in my_list)
	print("The list contains: {values}")
else:
	print("The list is empty")


## NOTE: This approach is especially useful for checking whether or not a function or method returned None:
from operator import add, mul, sub, truediv

operations = {
	"add": add,
	"divide": truediv,
	"multiply": mul,
	"subtract": sub
}

selected_option = input("Select the operation to perform: ").strip().lower()

operation = operations.get(selected_option)  # returns None if the key is invalid

if operation:
	a = input("Please enter a value for the first operand: ")
	b = input("Please enter a value for the second operand: ")

	print(operation(a, b))
else:
	print("Invalid operation")


#* -------------------- Boolean Operators for Control Flow -------------------- #

x = int(input("Please enter a number between 1 and 10: "))

if x < 1 or x > 10:
	print("Invalid selection")
else:
	print(x)
 
## NOTE:for "and" --> we get the first operand back if that operand is falsy; otherwise we get the second operands.
print( 4 and 0 ) # 0 since first operand is truthy
print( [] and 3 ) # [] since first operand is falsy
print( True and False ) # False since first operand is truthy
print( True and True ) # True since first operand is truthy
print( 4 and 5 ) # 5 since first operand is truthy

    # If both the first value is truthy, we must check the second value for falsiness. If both are true, then when the second is evaluated we get True back.

## NOTE: for "or" --> returns the first operand if it's truthy, otherwise it returns the second
print( 4 or 0 ) # 4 since first operand is truthy
print( [] or 3 ) # 3 since first operand is falsy
print( False or None ) # None since first operand is falsy
print( True or False ) # True since first operand is truthy
print( 4 or 5 ) # 4 since first operand is truthy


#* -------------------- Using "or" to replace falsy values -------------------- #

# Let's consider a case where we want to enter a default name when the user fails to provide one

name = input( "Please enter your name: " ).strip().title() or "John Doe"
    # Assign name to user input if not empty string, otherwise assign the string "John Doe"
    

#* ------------- Using "and" to change how we handle return values ------------ #

def divide( a, b ):
    try:
        return a / b
    except ZeroDivisionError:
        return
    
a = 6
b = int( input( "Enter a number for b: " ).strip() )

result = divide( a, b )

if result and result.is_integer():
    print( f"{a} / {b} produces an integer result." )
else:
    print( result )
    
    
#* -------------------------- Truncation over slicing ------------------------- #

# Let's say we have a list, and we want to discard some values from that list. An example might be a case where we've somehow filtered a list, but we only want the first ten values.

numbers = [1, 54, 2, -4, -65, 23, 97, 45, 14, 19, 73, -6, 31, 92, 3]

positive_numbers = sorted( number for number in numbers if number > 0 )

# Take only first ten values (delete all values after index 9):
del positive_numbers[ 10: ]

print( positive_numbers )




#* ------------------- Check for multiple values using "in" ------------------- #

proceed = input("Would you like to continue? ").strip().lower()

# Instead of:
if proceed == "y" or proceed == "yes" or proceed == "continue":
	pass

# DO:
if proceed in ("y", "yes", "continue"):
    pass



# ---------------------------------------------------------------------------- #
#*                                   Exercises                                  #
# ---------------------------------------------------------------------------- #


## 1) Write a function that prompts the user for their name and then greets them. You should process the string by removing any whitespace and converting the string to title case.
    # If after processing the string you're left with an empty string, the function should replace the empty string with "World" in the output.
    
def user_name():
    name = input( "Please enter your name: " ).strip().title() or "World"
    
    print( f"Hello, {name}" )

user_name()

print() # Extra whitespace

## 2) Write a function to determine whether or not a string contains exclusively ASCII letters (a to z in either upper or lowercase).

from string import ascii_letters

def ascii_or_not( test_string ):
    return all( character in ascii_letters for character in test_string )
    
ascii_or_not( "3" ) # False
ascii_or_not( "A" ) # True


## 3) Use the sample function in the random module to create three lists, each containing fifteen numbers from 1 to 100 (inclusive). Sort each of these lists into descending order (largest first), and then truncate each list so that only 5 items remain in each.

from random import sample

def random_sample( k ):
    sample_list = range( 1, 101 )
    
    return sample( sample_list, k )

list1 = sorted( random_sample( 15 ), reverse=True )
list2 = sorted( random_sample( 15 ), reverse=True  )
list3 = sorted( random_sample( 15 ), reverse=True ) 

del list1[ :10 ]
del list2[ :10 ]
del list3[ :10 ]

print( list1 )
print( list2 )
print( list3 )