# ---------------------------------------------------------------------------- #
#*                    Class Functions and Lambda Expressions                    #
# ---------------------------------------------------------------------------- #

##* What are first class functions?
# A programming language is said to have first class functions when functions in that language are treated like any other type. They're said to be "first class citizens" of the language.

# Generally speaking, this means we can pass functions in as arguments to other functions, return them from functions, and assign them to variables.

# When we define a function, we are simultaneously naming the function according to our specification (function name), and the functino name becomes part of the representation for this function (that exists in memory)

def add( a, b ):
    print( a + b )

adder = add # assign a different variable name to the already named add() func.

# We see that both variable names point to the same function object in memory
print( add )
print( adder )
# NOTE: also note that even though we assigned adder = add, when we print out the variable name we see that the function is still called add, not adder ****

# if we delete add, we cannot call this func again, we can only call adder
del add
adder( 1, 2 )



#* -------------------------- Functions as Arguments -------------------------- #

## Since we can assign variables to functions, we can also pass in functions as arguments --> Parameters are really just variables, and arguments are the values we assign to those variables, therefore we can assign a function to a variable and pass that variable as a parameter to a different function.

numbers = [56, 3, 45, 29, 102, 30, 73]
highest_number = max(numbers)

print(highest_number)  # 102

# If we wanted to find the max grade_average in this dictionary, the max() function alone won't cut it
students = [
	{"name": "Hannah", "grade_average": 83},
	{"name": "Charlie", "grade_average": 91},
	{"name": "Peter", "grade_average": 85},
	{"name": "Rachel", "grade_average": 79},
	{"name": "Lauren", "grade_average": 92}
]

# In cases like this, we can help the max function out by providing a function to a keyword only parameter called key. This function gets called for every item in the iterable, and each item is passed to the function, one at a time

def get_grade_average( student ):
    return student[ "grade_average" ]
# pass the function result into the key parameter for the max function
valedictorian = max( students, key=get_grade_average )
print( valedictorian )


## sort students list by gpa via sort function:
sorted_students_ascending = sorted( students, key=get_grade_average )
print( sorted_students_ascending )
sorted_students_descending = sorted( students, key=get_grade_average, reverse=True )
print( sorted_students_descending )




#* ----------------- Returning Functions from Other Functions ----------------- #
def add(a, b):
	print(a + b)

def subtract(a, b):
	print(a - b)

def multiply(a, b):
	print(a * b)

def divide(a, b):
	if b == 0:
		print("You can't divide by 0!")
	else:
		print(a / b)
  
# Create dictionary of operations
operations = {
    "a": add,
    "s": subtract,
    "m": multiply,
    "d": divide
}

# selected_option = input( """Please select one of the following options:

# a: add
# s: subtract
# m: multiply
# d: divide

# What would you like to do? """ )

# operation = operations.get( selected_option )

# if operation:
#     a = int( input( "Please enter a value for a: " ) )
#     b = int( input( "Please enter a value for b: " ) )
	
#  	## NOTE: pass the user-selected operation as a function with a and b as its parameters 
#     operation( a, b )
# else:
#     print( "Invalid selection" )
    
    
    
# #* ---------------------------- Lambda Expressions ---------------------------- #

# ## Lambda expressions are a useful way to define simple functions. They are especially useful because they are EXPRESSIONS and are evaluate the function that we want to create

# # Example: use a lambda expression to evaluate to the add function
# lambda a, b: a + b

# students = [
# 	{"name": "Hannah", "grade_average": 83},
# 	{"name": "Charlie", "grade_average": 91},
# 	{"name": "Peter", "grade_average": 85},
# 	{"name": "Rachel", "grade_average": 79},
# 	{"name": "Lauren", "grade_average": 92}
# ]

# ##* Since the key= parameter for max() requires a function, we can use the lambda expression to signify that we want to sort via the "grade_average" key for each student within the students iterable list
# valedictorian = max( students, key=lambda student: student["grade_average"] )
# print( valedictorian )


# ## We can make good use of lambda expressions for the simpler arithmatic operations used above:
# def divide(a, b):
# 	if b == 0:
# 		return "You can't divide by 0!"
# 	else:
# 		return a / b
		
# ##NOTE: can use lambda expressions for the simpler functions w/o if statements
# operations = {
# 	"a": lambda a, b: a + b,
# 	"s": lambda a, b: a - b,
# 	"m": lambda a, b: a * b,
# 	"d": divide
# }

# selected_option = input("""Please select one of the following options:

# a: add
# s: subtract
# m: multiply
# d: divide

# What would you like to do? """)

# operation = operations.get(selected_option)

# if operation:
# 	a = int(input("Please enter a value for a: "))
# 	b = int(input("Please enter a value for b: "))

# 	print(operation(a, b))
# else:
# 	print("Invalid selection")


# ## NOTE: We can also assign variables to lambda expressions since functions ( and therefore lambda expressions ) are "first class functions"

# add = lambda a, b: a + b
# print( add( 7,8 ) )


# ---------------------------------------------------------------------------- #
#*                                   Exercises                                  #
# ---------------------------------------------------------------------------- #

## 1) Use the sort method to put the following list in alphabetical order with regards to the students' names:
students = [
	{"name": "Hannah", "grade_average": 83},
	{"name": "Charlie", "grade_average": 91},
	{"name": "Peter", "grade_average": 85},
	{"name": "Rachel", "grade_average": 79},
	{"name": "Lauren", "grade_average": 92}
]

sorted_students = sorted( students, key=lambda student: student[ 'name' ] )

print( sorted_students )


## 2) Convert the following function to a lambda expression and assign it to a variable called exp.
def exponentiate(base, exponent):
	return base ** exponent

exp = lambda base, exponent: base ** exponent

print( exp( 3, 2 ) )


## 3) Print the function you created using a lambda expression in previous exercise. What is the name of the function that was created?

## NOTE: when printing the object, it is contained as a <lambda> function
print( exp )

"""
	Lambda Functions are also called ANONYMOUS FUNCTIONS since they do not have a name associated with them
"""


