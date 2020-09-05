# ---------------------------------------------------------------------------- #
#*                              WORKING WITH FILES                              #
# ---------------------------------------------------------------------------- #



example_file = open( "./example.txt" ) # "./" means current working directory

print( f"Example file contents:", example_file.read( ) )

# NOTE: WWHEN DONE WORKING WITH A FILE, MAKE SURE TO CLOSE IT!
example_file.close()

## Reasons why:
    # It puts your program in the garbage collectors hands - though the file in theory will be auto closed, it may not be closed. Python 3 and Cpython generally do a pretty good job at garbage collecting, but not always, and other variants generally suck at it.
    # It can slow down your program. Too many things open, and thus more used space in the RAM, will impact performance.
    # For the most part, many changes to files in python do not go into effect until after the file is closed, so if your script edits, leaves open, and reads a file, it won't see the edits.
    # You could, theoretically, run in to limits of how many files you can have open.
    # As @sai stated below, Windows treats open files as locked, so legit things like AV scanners or other python scripts can't read the file.
    # It is sloppy programming (then again, I'm not exactly the best at remembering to close files myself!)
    
    

#* --------------------- Opening Files in Different Modes --------------------- #

## Read access mode:
example_file = open( "./example.txt", mode="r" )
print( example_file.read( ) )
example_file.close()


## Write access mode: NOTE --> This mode deletes whatever was already in the before open()
write_file = open( "write_example.txt", mode="w" ) # now a new file called is created
write_file.write( "Welcome to the world, write_example.txt!" ) 
write_file.close()


## Append Mode: Add data to an existing file
write_file = open("write_example.txt", "a")
write_file.write("\nNow you have two lines! You're growing up so fast!")
write_file.close()




#* ------------------ Context Managers for working with files ----------------- #

## NOTE: context managers allow you to aallocate and release resources precisely when you want to. It will try your block of code and see it has errors, and if it does, it will do garbage collection and proceed. In the case of working with files, if there is an error opening the file, the context manager will automatically close it.

with open( "./example.txt", mode="r" ) as example_file:
    print( example_file.read( ) )
    
# The above code is equivalent to:
    # example_file = open("example.txt", "r")
    # print(example_file.read())
    # example_file.close()
    



#* --------------------------------- CSV Data --------------------------------- #
 
## Working iris.csv data set:

# Get data from file, and split into rows:
with open( "./iris.csv", mode="r" ) as iris_file:
    iris_data = iris_file.readlines() 

irises = [] # list where we will place the dictionaries for each iris

for row in iris_data[ 1: ]:
    sepal_length, sepal_width, petal_length, petal_width, species = row.strip().split( "," )
    
    irises.append( {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
        "species": species
    } )    
    
    
    
## ALTERNATIVE WAY:
with open("iris.csv", "r") as iris_file:
	iris_data = iris_file.readlines()

headers = iris_data[0].strip().split(",") # create list of headers by stripping whitespace, and getting rid of commas between header names

irises = [] # empty list to hold iris data (minus headers)

# start loop at first row (since we already captured the headers)
for row in iris_data[1:]:
	iris = row.strip().split(",") # create list where each element is an element from 1 row
	iris_dict = dict(zip(headers, iris)) # matches each header item to a value in a given row using zip(), converts to a dictionary

	irises.append(iris_dict)

