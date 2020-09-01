# ---------------------------------------------------------------------------- #
#                           CONDITIONALS AND BOOLEANS                          #
# ---------------------------------------------------------------------------- #



#* "Truthy" vs "Falsy" values
# If we pass a string into a bool, and it returns True, it's a "Truthy" value. Otherwise it's a "falsy" value

print( bool( "Hello" ) ) # returns true because it's a populated string, i.e. not empty

print( bool( [] ) ) # returns false because the list is empty




#* Comparing with the "is" operator keyword
a = [1, 2, 3]
b = [1, 2, 3]
# Though they contain the same values and are the same size, a and b are stored in different memory locations. 
print( a is b ) # False since mem_location of a is not mem_location of b. 
# i.e. a and b are different objects, therefore point to different memory locations
print( "id of a:", id(a), "id of b:", id(b) )

# NOTE: To get two objects pointing to the same location
a = [1, 2, 3]
b = a # now b and a point to same memory location
print( a is b )
print( "id of a:", id(a), "id of b:", id(b) )




# ---------------------------------------------------------------------------- #
#*                                   EXERCISE                                   *#
# ---------------------------------------------------------------------------- #

print( "\n\nEXERCISE!!!" )
# 1) Approximate the behavior of the "is" operator using ==
numbers = [1, 2, 3, 4]
numbers1 = [1, 2, 3, 4]

if id( numbers ) == id( numbers1 ):
    print( True )
else:
    print( False )

# 2)  
numbers = [1, 2, 3, 4]

new_numbers = numbers + [5] # numbers is unaffected, new_numbers is a new object

print( id(numbers), id(new_numbers) )

print( id(numbers) )
numbers.append( 5 )
print( id(numbers ) )

# 3) Ask the user to enter a number. Tell the user whether the number is positive, negative, or zero.

print( "Please enter a number:" )
num = int( input() )

if num % 2 == 0:
    #if even
    print( "even" )
else:
    print("odd")

# 4) overtime?

print( "How many hours worked?" )
hours = int( input( ) )
print( "Hourly wage?" )
wage = float( input( ) )

if hours >= 40:
    print("employee due:", 1.10*hours*wage )
else:
    print("employee due:", hours*wage)