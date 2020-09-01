# ---------------------------------------------------------------------------- #
#                            Split, Join, and Slices                           #
# ---------------------------------------------------------------------------- #



#* ------------------- Convering tuples and lists to strings ------------------ #

numbers = [1, 2, 3, 4, 5]
numbers = str( numbers )
print( numbers ) # Redundant because the print() function automatically converts what's inside of it into a string. Equivalent to converting numbers into "[1,2,3,4,5]"

# If we want to print a list out like this: 1, 2, 3, 4, 5 --> We do the following:
project_authors = ["Mike", "Sofia", "Helen"]
project_authors = ", ".join(project_authors) # places the preceding string between the items in the collection we want to glue together

print(f"The people who worked on this project are: {project_authors}.")


## NOTE: For the numbers collection:
numbers = [1, 2, 3, 4, 5]

stringified_numbers = []

for number in numbers:
    stringified_numbers.append( str( number ) )
    
print( ', '.join( stringified_numbers ) )



#* --------------------------- Splitting up a string -------------------------- #

# The split tool allows us to convert a string into another collection of several item.s For example, we might want to do this when processing user input if the user provides multiple values in response to a single prompt.

# Ex: want to get five numbers from the user, request that they be comma separated
user_numbers = input("Please enter 5 numbers separated by commas: ") # 1,2,3,4,5
numbers_list = user_numbers.split( "," ) # "," is the delimeter here because we have to match how the user separated their number inputs

print( "Numbers List:", numbers_list )

# NOTE: split() won't wipe out any whitespace, use strip:

user_numbers = input("Please enter 5 numbers separated by commas: ") # 1, 2, 3, 4, 5
numbers_list = user_numbers.split( "," )

# now use the strip() function to remove the whitespace from each entry
numbers_list_stripped = []

for number in numbers_list:
    numbers_list_stripped.append( number.strip() )
    
print( "Numbers List (Stripped):", numbers_list_stripped )


# Default for split() is using whitespace as the delimeter
user_numbers = input("Please enter 5 numbers separated by whitespace: ") # 1 2 3 4 5
numbers_list = user_numbers.split(  )
print( "Numbers List:", numbers_list )


#* putting different items into list or tuple:
sample_string = "Python"

print(list(sample_string)) # ['P', 'y', 't', 'h', 'o', 'n']
print(tuple(sample_string)) # ('P', 'y', 't', 'h', 'o', 'n')


#* ---------------------------------- Slicing --------------------------------- #

## Slicing is a new way for us to use a subscription expression with sequences. Instead of providing a single index, we specify a range of indices. What we’ll get back is a collection of the same type that we sliced, containing all the items in the specified range. One great thing about slices is that they give us a new collection, leaving the original untouched.

original_string = "Python"

sliced_string = original_string[:3]
print(sliced_string)  # Pyt

sliced_string = original_string[3:]
print(sliced_string)  # hon

# start at 0 (default), end at end (default), step by 3 elements
print(original_string[::-1])  # nohtyP


# ---------------------------------------------------------------------------- #
#*                                  EXERCISE                                   #
# ---------------------------------------------------------------------------- #


# 1) Ask the user to enter their given name and surname in response to a single prompt. Use split to extract the names, and then assign each name to a different variable. For this exercise, you can assume that the user has a single given name and a single surname.

user_name = input( "Please enter your full name: " ) 
user_name = user_name.split() # user_name is now a list of the user input, delimited by whitespace

# assign first name and surname to different variables:
firstname = user_name[0]
lastname = user_name[1]

print( f"First name: {firstname}, Last name: {lastname}" )



# 2) Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using the join method. Remember that you can only join collections of strings, so you’re going to need to do some initial processing of the list of numbers.

num_list = [1, 2, 3, 4, 5]

# initialize empty list to contain string version of above num_list
num_list_stringified = []

# append new list with strings of num_list elements
for num in num_list:
    num_list_stringified.append( str( num ) )

# print final list
print( " | ".join( num_list_stringified ) )



# 3) Each quote is a string, but each string actually contains quote characters at the start and end. Using slicing, extract the text from each string, without these extra quote marks, and print each quote.

quotes = [
    
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'"

]

# using strip(), take away the leading and trailing ' marks
for quote in quotes:
    print( quote.strip( "'" ) )
    

# 4) Ask the user to enter a word, and then print out the length of the word. You should account for any excess whitespace in the user’s input, so you’re going to have to process the string before you find its length. If you want to take this a little bit further, you an ask the user for a long piece of text. You can then tell them how many how many characters are in the text overall, and you can also provide them a word count.

print( "Enter a string of text:")
user_input = input()

# strip trailing whitespace
user_input = user_input.strip()
print( len( user_input ) ) 

# convert string input to a list (each character is an element)
user_input_list = list( user_input )


# a word can be defined as all the characters prior to a whitespace. For character count, count the number of characters before a whitespace. For word count, count the number of whitespaces and add 1 (no whitespace at the end, it was stripped)
char_count = 0
word_count = 0

for char in user_input_list:
    
    if char != " ":
        char_count += 1 # increment count based on number of elements
        
    else:
        word_count += 1

# add extra word_count since there is no trailing whitespace
word_count += 1
    
# Print word and character limits
print( "Character count:", char_count )
print( "Word Count:", word_count )