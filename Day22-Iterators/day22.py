# ---------------------------------------------------------------------------- #
#*                                   ITERATORS                                  #
# ---------------------------------------------------------------------------- #


##* Iterables definition:
    # any value we can iterate over with something like a for loop. We can also destructure iterables, and we can create collections from them by passing the value to functions like "list" or "tuple"
    
    # Anything that we can get one value out of at a time
    
    # Here are some examples:
        # strings, lists, tuples, dictionaries, setes, range objects, zip objects, enumerate objects, map objects, filter objects
    
    
    
# NOTE: iterators are "lazy" types, meaning they don't calculate their values until our program specifically asks for them --> this is memory efficient


from operator import methodcaller

words = [ "anaconda", "peach", "gravity", "cattle", "anime", "addition" ]
a_words = filter( methodcaller( "startswith", "a" ), words )
    # we can't determine the length of a_words until we actually perform the filtering operation, and filter() is going to wait until we ask it for values to calculate anything. It's therefore impossible for us to get any indication of how long a_words actually is.
    # it's also impossible to see what values the filter object contains
    

#### NOTE: ITERATOR VALUES ARE CONSUMED!!!
for word in a_words:
    print( word )
    
print( a_words, ",list of filter object:", list( a_words ) )
    # we see that this is now an empty list. The object still exists, but it contains nothing now
    
    


#* ----------- Changes to mutable collections can affect an iterator ---------- #


words = ["anaconda", "peach", "gravity", "cattle", "anime", "addition"]
a_words = filter(methodcaller("startswith", "a"), words)

words.append("apple")

for word in a_words:
	print(word)
 
# NOTE: we see that even though we created the filter iterator before modifying words, the "apple" still gets added to the filter object. This is because the filter object only references the words list, so if we change after a filter statement, the filter object is still referencing words which has now been appended. Think of it in terms of pointers - the filter object a_words points to something that it will do on words (points to a thing that points to words), so if we modify words, it will point to the modified words list object



#* ------------------ Manual iteration with the next function ----------------- #

words = ["anaconda", "peach", "gravity", "cattle", "anime", "addition"]
a_words = filter(methodcaller("startswith", "a"), words)

first_word = next(a_words)
print(first_word)  # "anaconda"

print( next( a_words ) ) # "anime"






#* -------------------------- StopIteration Exception ------------------------- #

# The "StopIteration" exception is handled when we use a for loop, but not when doing manual iteration (using next() ). It happens when we try to manually iterate past the length of the iterator

# Ex:
words = ["anaconda", "peach", "gravity", "cattle", "anime", "addition"]
a_words = filter(methodcaller("startswith", "a"), words)

print(next(a_words))  # "anaconda"
print(next(a_words))  # "anime"
print(next(a_words))  # "addition"

try:
    print(next(a_words))  # StopIteration
except StopIteration:
    print( "StopIteration exception thrown!" )
    
    
    
# ---------------------------------------------------------------------------- #
#*                                   Exercises                                  #
# ---------------------------------------------------------------------------- #

numbers = [(23, 3, 56), (98, 1034, 54), (254, 344, 5), (45, 2), (122, 63, 74)]

## 2) Use the map function to find the sum of the numbers in each tuple. Use manual iteration to print the first two results provided by the resulting map object.

totals = map( sum, numbers )

print( next( totals ) )
print( next( totals ) )

for triplet in numbers:
    print( sum( triplet ) )

## 3) Imagine you have 3 employees and it's been agreed that the employees will take it in turns to lock up the shop at night. This means that for employees A, B, and C, employee A will close the shop on day 1, then B will close the shop on day 2, C will close the shop on day 3, and then we start the cycle again with employee A.
    # Write a program to create a schedule that lists which of your employees will lock up the shop on a given day over a 30 day period. You should list the day number, the employee name, and the day of the week. You can choose any employee to lock the shop on day 1, and you can also choose which day of the week day 1 corresponds to

import itertools

employees = itertools.cycle( [ "A", "B", "C" ] )

weekdays = itertools.cycle(
    [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]
)

# loop till 30 days have been reached
for day in range( 1, 31 ):
    print( f"Day {day} ({next(weekdays)}): {next(employees)} cleans" )
    
    

    
# ------------------------------------- - ------------------------------------ #

students = [ "matt", "steve", "bob", "sam", "john", "joe" ]

# two teams
num = itertools.cycle( range( 1, 3 ) )

team = []

for student in range( len( students ) ):    
    team.append( ( next(num), students[student] ) )

print( team )
team = dict( team )

print( team )
    
