# ---------------------------------------------------------------------------- #
#                                   FOR LOOPS                                  #
# ---------------------------------------------------------------------------- #


# ------------------------------ NOTE: ITERATORS ----------------------------- #

#* when we use an iterator, i.e., for iterator in iterable, what is happening in the background via Python is the following:
nums = [1, 2, 3]
iter_nums = nums.__iter__() # creates an iterator object for the list nums, which is created when we do:
for iter_nums in nums:
    pass
# here, iter_nums is automatically assigned to nums.__iter__() when we use it in a for loop like that


# ------------------------------------ -- ------------------------------------ #
movies = [
	(
		"Eternal Sunshine of the Spotless Mind",
		"Michel Gondry",
		2004
	),
	(
		"Memento",
		"Christopher Nolan",
		2000
	),
	(
		"Requiem for a Dream",
		"Darren Aronofsky",
		2000
	)
]

# print entire list of movies:
for movie in movies:
    # NOTE: movie = loop variable, movies = iterable (what we're iterating over)
    print( f"{movie[0]} ({movie[1]}), by {movie[2]}" )
    
    
#* What's happening under the hood:
# during each loop, the loop variable 'movie' is assigned to the value of the iterable at each index defined (0, 1, 2)


# NOTE: if we print the first index of the movie variable, we see that it has only stored the first index of the last tuple (since that was the last tuple assigned to movie from the loop)
print( "\n\n", movie[0], movie[1], movie[2], "\n\n" )



# ------------------------------ Break Statement ----------------------------- #

for movie in movies:
    if movie[0] == "Memento":
        print( "Memento is in the movie library!" )
        break
    
    
    
# ------------------------------ Range Function ------------------------------ #

r = range( 10 )
print( r )
#* instead of printing 0, 1, 2, etc., it just prints range(0,10). 
#* Range is a LAZY TYPE, meaning that it doesn't contain all the values in the sequence, it figures out what the next number should be wehen we ask for it. This makes the range function MEMORY EFFICIENT!

# Create a list of numbers using the range function
numbers = list( range(10) )
print( numbers )

# range used in a for loop
for i in range(10):
    print( i )
    
    
    
    
# ---------------------------------------------------------------------------- #
#*                                   EXERCISES                                  *#
# ---------------------------------------------------------------------------- #

# 1) Below we've provided a list of tuples, where each tuple contains details about an employee of a shop: their name, the number of hours worked last week, and their hourly rate. Print how much each employee is due to be paid at the end of the week in a nice, readable format.

employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

for employee in employees:
    print( f"Employee: {employee[0]}, End of week pay: {employee[1]*employee[2]}" )
    
# 2) For the employees above, print out those who are earning an hourly wage above average.

# Calculate total wage:
tot_h_wage = 0

for employee in employees:
	tot_h_wage += employee[2]

# Calculate average hourly wage
avg_h_wage = tot_h_wage / len( employees ) 

# Find employees that are making above average hourly wage
for employee in employees:
    if employee[2] > avg_h_wage:
        print( f"Employee earning above avg: {employee[0]}" )