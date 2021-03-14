# ---------------------------------------------------------------------------- #
#*                   Scope and Returning Values from Functions                  #
# ---------------------------------------------------------------------------- #


# Scope determines where a variable is accessible within a program


# Ex:
def greet( name ):
    greeting = f"Hello, {name}!"
    print( greeting )
    
# if we try and use the string variable greeting outside of the function body, we get an error. Since greeting is defined only within the function greet(), it is only accessible within that function




#* -------------------------------- Namespaces -------------------------------- #

## Python keeps a record of the variables we've defined, and the values that are associated with those names. The "stack" stores the references to variables (and their values) which are stored in the heap.

# we can see the record of these variables as follows:
print( globals( ) ) # can see the object for the function greet() and its hexadecimal memory address

global_variable = 10
print( globals() ) # now we can see that an int global_variable has been added to the global namespace

# NOTE: when we use a variable in our application, Python just looks inside the namespace to see if it's defined. If it is within the current namespace scope that it's being used in, then it can reference that value. But in the case of the string greeting, it is only within the scope of the function, not the global scope, so the global namespace does not contain it and therefore it cannot be accessed.




print( "\n\n" )
#* --------------------- Returning values from a Function --------------------- #

## Since variables defined within the scope of a function are not accessible, we would like to be able to access the result of a function and get values back.

# a and b are only defined within the function, but we can return the result a + b:
def add( a, b ):
    return a + b

print( add( 1, 2 ) )

# NOTE: if no return statement is defined for a function, Python automatically returns None



#* ------------------------ Multiple Return Statements ------------------------ #

## NOTE: Multiple return statements can only be used with if conditional logic is used to direct us towards a specific return value

def divide(a, b):
	if b == 0:
		return "You can't divide by 0!"

	return a / b





# ---------------------------------------------------------------------------- #
#*                                   EXERCISES                                  #
# ---------------------------------------------------------------------------- #


## 1) Define a exponentiate function that takes in two numbers. The first is the base, and the second is the power to raise the base to. The function should return the result of this operation. Remember we can perform exponentiation using the ** operator.
def exponentiate( base, power ):
    return base**power

print( exponentiate( 2, 3 ) )


## 2) Define a process_string function which takes in a string and returns a new string which has been converted to lowercase, and has had any excess whitespace removed.
def process_string( string=str ):
    return string.strip().lower() 

print( process_string( "   Hello, Billy  " ) )


## 3) Write a function that takes in a tuple containing information about an actor and returns this data as a dictionary. Data is in the following format: ("Tom Hardy", "English", 42)  # name, nationality, age
def actor_dictionary( actor=tuple ):
    actor_dictionary = {
        "name": actor[0],
        "nationality": actor[1],
        "age": actor[2]
    }
    
    return actor_dictionary
# OR:
def dictify( actor=tuple ):
    name, nationality, age = actor
    
    return {
        "name": name,
        "nationality": nationality,
        "age": age
    }

print( actor_dictionary( ( "Tom Hardy", "English", 42 ) ) )
print( dictify( ( "Tom Hardy", "English", 42 ) ) )


## 4) Write a function that takes in a single number and returns True or False depending on whether or not the number is prime. If you need a refresher on how to calculate if a number is prime, we show one method in day 8 of the series.

def is_prime( dividend ):
    
    divisor = 2
    
    while divisor < dividend:
        # If user's number is divisible by the curent divisor, break the loop
        if dividend % divisor == 0:
            return False
            break
            
        # Increment the divisor for the next iteration
        divisor = divisor + 1
    else:
        # This line only runs if no divisors produced integer results
        return True
    
print( is_prime( 73 ) ) # True
print( is_prime( 20 ) )