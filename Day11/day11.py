# ---------------------------------------------------------------------------- #
#                                     SETS                                     #
# ---------------------------------------------------------------------------- #


## Sets are similar to collections, but they are not reliably ordered. Think of it like a dictionary that only contains keys, since it can only contain unique elements

# Defining a set:
vegetables = {"carrot", "lettuce", "broccoli", "onion", "carrot"}
#NOTE: since "carrot" is in there twice, it will delete the duplicate

# for an empty set:
set()


##* Sets cannot contain any mutable types, or immutable types containing mutable types. Nor can we include a set within another set (nested sets) since sets can be modified.


#* ------------------------------ Modifying Sets ------------------------------ #

## Adding an item to a set:
vegetables = {"carrot", "lettuce", "broccoli", "onion"}

vegetables.add("potato") 

print( vegetables ) # NOTE: note how the order is not the same as entered when printing

## Deleting an item from a set:
vegetables.remove("lettuce")

print( vegetables ) # note again how the order changed after printing.

# BETTER TO USE SINCE IT CHECKS FOR EXISTENCE OF THE ITEM IN THE SET BEFORE DELETION
vegetables.discard( "potato" )

print( vegetables )

# To remove one item at random, use pop()
vegetables.pop()
print( vegetables ) 


#* ------------------------------ Set Operations ------------------------------ #

## Sets provide unique operations that can efficiently compare collections

## UNION: combines two sets, includes all the members of both sets and includes duplicate members only once
letters = {"a", "b", "c"}
numbers = {1, 2, 3}

letters_and_numbers = letters.union(numbers)

print(letters_and_numbers)  # {'a', 'c', 1, 2, 3, 'b'}


## INTERSECTION: creates a new set containing the elements common to both sets.
mod_2 = {2, 4, 6, 8, 10, 12, 14, 16, 18}
mod_3 = {3, 6, 9, 12, 15, 18}

mod_6 = mod_2.intersection(mod_3)

print(mod_6)  # {18, 12, 6}


## DIFFERENCE: order matters!!! See below
bundle_1 = {"Resident Evil 3", "Final Fantasy VII", "Cyberpunk 2077"}
bundle_2 = {"Doom Eternal", "Halo Infinite", "Resident Evil 3"}

print( bundle_1.difference(bundle_2) )  # {'Final Fantasy VII', 'Cyberpunk 2077'}
print( bundle_2.difference(bundle_1) )  # {'Halo Infinite', 'Doom Eternal'}
# set1.difference(set2) will print all elements of set1 that ARE NOT CONTAINED within set2


## SYMMETRIC DIFFERENCE: gives all of the items which only feature in one of the sets. Unlike difference(), the order does not matter 

bundle_1 = {"Resident Evil 3", "Final Fantasy VII", "Cyberpunk 2077"}
bundle_2 = {"Doom Eternal", "Halo Infinite", "Resident Evil 3"}

print(bundle_1.symmetric_difference(bundle_2)) # {'Cyberpunk 2077', 'Final Fanstay VII', 'Halo Infinite', 'Doom Eternal'} includes everything from both sets except what is contained in both


#* ------------------- Set Operations With Other Collections ------------------ #

# We can combine a list with a set:
letters = {"a", "b", "c"}
numbers = [1, 2, 3]

letters_and_numbers = letters.union(numbers)

print(letters_and_numbers)  # {'a', 'c', 1, 2, 3, 'b'}

# Combining a set with a tuple:
letters = { "a", "b", "c" }
numbers = (1, 2, 3)

letters_and_numbers = letters.union(numbers)

print(letters_and_numbers)  # {'a', 'c', 1, 2, 3, 'b'}


#* ------------------- Checking if items are in Collections ------------------- #

# To check if a value is in a collection, we can use the "in" keyword which returns True if the value specified is found:

numbers = {1, 2, 3, 4, 5}

print(3 in numbers)  # True
print(7 in numbers)  # False

# We can do this for any collection, such as a string:
print( "j" in "Python" ) # False
print( "n" in "Python" ) # True


# We can use "in" to check if a key is in a dictionary!:
student = {
	"name": "Eric Cartman",
	"age": 10,
	"school": "South Park Elementary"
}

print( "grades" in student )  # False
print( "school" in student )  # True

# or among its values:

print(10 in student.values())  # True




# ---------------------------------------------------------------------------- #
#*                                   Exercises                                  #
# ---------------------------------------------------------------------------- #

