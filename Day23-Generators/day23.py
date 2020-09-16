# ---------------------------------------------------------------------------- #
#*                     GENERATORS AND GENERATOR EXPRESSIONS                     #
# ---------------------------------------------------------------------------- #





#* ----------------------------- The iter function ---------------------------- #

## The iter function takes an iterable as an argument and returns an iterator:
numbers = [1,2,3,4,5]
numbers_iter = iter( numbers )

print( numbers_iter ) # <list_iterator object>

print( next( numbers_iter ) ) # 1
print( next( numbers_iter ) ) # 2

## If we take an iter of an already created iterator, it returns itself -- this is because an iterator is a means by which we can access values of an iterable, and since this iterator already does that, the function returns the iterator!
print( numbers_iter is iter( numbers_iter ) ) # True



#* ---------------------- Replicating for loops with iter --------------------- #

numbers = [1,2,3,4,5]
numbers_iter = iter( numbers )

while True:
    try:
        number = next( numbers_iter )
    except StopIteration:
        break
    else:
        print( number )
        
    # The loop variable "number" is defined  inside the try clause, the the loop body is defined inside the else clause
    


#* -------------------------------- Generators -------------------------------- #
print( "\n\n" )

def first_hundred():
    for number in range( 1, 101 ):
        yield number
        
g = first_hundred()

print( next( g ) ) # 1
print( next( g ) ) # 2

    # We have returned an iterator as the variable g!
    



#* ----------------------------- The yield keyword ---------------------------- #

# NOTE: Yield creates a pause in the execution of the function body. When we call next and pass our generator iterator, the code in the function body is going to run until we hit that yield keyword. 
# The value after the yield keyword is what we want to provide before we pause the execution of the function body --> yield is like a non-terminating return statement

def first_hundred():
	print("First value requested\n")
	
	for number in range(1, 101):
		print("Starting new iteration")
		yield number
		print("Ending this iteration\n")

# If we just call the generator function and return the iterator "g", we see that nothing has printing
g = first_hundred()

# Now we see that we are accessing the print statements 
print( next( g ) )
print( next( g ) )
    # when we call next the second time, we continue from where we left off (printing the Ending this iteration string) and move onot the new iteration for the for loop.
    
print( next( g ) )
    # we see that we now print "Ending this iteration" again and then go on to return the third value from range via the variable "number"


#* --------------------------- Generator Expressions -------------------------- #

# NOTE: Generator expression syntax is very similar to comprehension syntax, only we use () instead of [] or {} to wrap the expression


# Ex: Create a generator that squares every number in a range:
squares = ( number ** 2 for number in range( 1, 11 ) )
print( squares ) # <generator object <genexpr> >

# To get values out, we can destructure it, or use next for manual iteration:
print( *squares, sep=", " )

squares = ( number ** 2 for number in range( 1, 11 ) )
print( next( squares ) )
print( next( squares ) )




## Style NOTE: we can forego the parentheses when we use the generator expression as the sole argument in a function or method, e.g.:
total = sum( number ** 2 for number in range( 1, 11 ) )
print( total ) #385






# ---------------------------------------------------------------------------- #
#*                                   EXERCISES                                  #
# ---------------------------------------------------------------------------- #

## 1) Write a generator that generates prime numbers in a specified range. You can make use of your solution to exercise 3 from day 8 as a starting point.

def prime_generator( limit ):
    for dividend in range( 2, limit + 1 ):
        # iterates dividend from 2 to 100
        for divisor in range( 2, dividend ):
            # iterates divisor from 2 to dividend
            if dividend % divisor == 0:
                # if NOT PRIME
                break
            
        else:
            # if PRIME
            yield dividend

prime = prime_generator( 100 )
print( "Primes - 2 thru 100:" )
print( *prime, sep=", " )


## 2) Below we have an example where map is being used to process names in a list. Rewrite this code using a generator expression.

names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy    "]
names = map(lambda name: name.strip().title(), names)

names = ( name.strip().title() for name in names )

print( *names, sep=", " )

# Now, to test that the iterator was consumed fully by the above expression:
try:
    print( next( names ) )
except StopIteration:
    print( "Iteration stopped, iterator was already consumed" )

print( "\n\n" )



## 3) Texas Hold'em
from random import shuffle

ranks = [ "ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king" ]
suits = [ "clubs", "spades", "diamonds", "hearts" ]

def create_deck( suits=list, ranks=list ):
    deck = []
    # Map each card to the suit till each suit holds all 13 cards
    for suit in suits:
        for card in ranks:
            deck.append( ( card, suit ) )
            
    return deck

# NOTE: a = shuffle( deck ) will return a as being NoneType, which doesn't allow you to do anything. You must shuffle the original list, not create via shuffle = shuffle( deck ). 
deck = create_deck( suits, ranks )
shuffle( deck )

# Create iterator from shuffled deck
shuffled_deck = iter( deck )

# # Could also use a generator expression to create a similar iterable object:
# shuffled_deck_gen = ( list( card ) for card in deck )



## GAME START:
n_players = int( input( "How many players are there? " ).strip() )

player_list = []
for n in range( 1, n_players + 1 ):
    player_list.append( n )

for n in player_list:
    print( f"Player {n} was dealt: {next(shuffled_deck)}, {next(shuffled_deck)}" )

print() # extra whitespace


# Flop:
print( f"The flop: {next(shuffled_deck)}, {next(shuffled_deck)}, {next(shuffled_deck)}" )

# Turn:
print( f"The turn: {next(shuffled_deck)}" )

# River:
print( f"The river: {next(shuffled_deck)}" )

