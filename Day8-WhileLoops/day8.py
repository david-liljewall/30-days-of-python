# ---------------------------------------------------------------------------- #
#                                  WHILE LOOPS                                 #
# ---------------------------------------------------------------------------- #




#* ----------------------------- Continue Keyword ----------------------------- #

# NOTE: the CONTINUE keyword allows us to skip the remainder of the loop body for the current iteration. Ex:

# If odd, skip printing number. i.e, only print even numbers
for number in range(10):
	if number % 2 != 0:
		continue
	print(number)
# is equivalent to:
for number in range( 10 ):
    if number % 2 == 0:
        print( number )


#* ----------------------------------- Else ----------------------------------- #

# For example, let's write a loop to determine whether or not a number is prime. A prime number is a number divisible only by itself and 1. For example, 2, 3, 5, 7, 11, and 13 are prime numbers.
# You can check if a number is prime by whether or not it is divisible by the numbers before it. If an integer result is not produced, the number IS prime

# Get a number to test from the user, and set the initial divisor to 2
dividend = int(input("Please enter a number: "))
divisor = 2

# Keep looping until the divisor equals the number we're testing
while divisor < dividend:
	# If user's number is divisible by the curent divisor, break the loop
	if dividend % divisor == 0:
		print(f"{dividend} is not prime!")
		break
		
	# Increment the divisor for the next iteration
	divisor = divisor + 1
else:
	# This line only runs if no divisors produced integer results
	print(f"{dividend} is prime!")


# ---------------------------------------------------------------------------- #
# *                                  Exercises                                  #
# ---------------------------------------------------------------------------- #

# 1) Write a short guessing game program using a while loop. The user should be prompted to guess a number between 1 and 100, and you should tell them whether their guess was too high or too low after each guess. The loop should keeping running until the user guesses the number correctly.

correct_number = 42

# Loop until user guesses the correct  number
# NOTE: see use of :=, THE WALRUS OPERATOR here. Whatever is after the operator is what the expression is evaluated to. Here, the user_number entered is what the expression evaluates to (i.e., an integer), and then that is compared with correct_number in a logical statement

while ( user_number := int( input( "Guess an integer:" ) )  != correct_number ):
    print( "WRONG! Guess again." )

print( "You guessed the correct number!" )
    
    
# 2) Use a loop and the continue keyword to print out every character in the string "Python", except the "o".

word = "Python"

for char in word:
    
    if char == "o":
        continue
    print( char )
    

# 3) Using one of the examples from earlier—or a solution entirely of your own—create a program that prints out every prime number between 1 and 100.

for dividend in range( 2, 101 ):
    # iterates dividend from 2 to 100
    for divisor in range( 2, dividend ):
        # iterates divisor from 2 to dividend
        if dividend % divisor == 0:
            # if NOT PRIME
            break
        
    else:
        # if PRIME
        print( dividend )
