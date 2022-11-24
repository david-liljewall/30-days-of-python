# ---------------------------------------------------------------------------- #
#                                     SETS                                     #
# ---------------------------------------------------------------------------- #


# Sets are similar to collections, but they are not reliably ordered. Think of it like a dictionary that only contains keys, since it can only contain unique elements

# Defining a set:
vegetables = {"carrot", "lettuce", "broccoli", "onion", "carrot"}
# NOTE: since "carrot" is in there twice, it will delete the duplicate

# for an empty set:
set()


# * Sets cannot contain any mutable types, or immutable types containing mutable types. Nor can we include a set within another set (nested sets) since sets can be modified.


# * ------------------------------ Modifying Sets ------------------------------ #

# Adding an item to a set:
vegetables = {"carrot", "lettuce", "broccoli", "onion"}

vegetables.add("potato")

# NOTE: note how the order is not the same as entered when printing
print(vegetables)

# Deleting an item from a set:
vegetables.remove("lettuce")

print(vegetables)  # note again how the order changed after printing.

# BETTER TO USE SINCE IT CHECKS FOR EXISTENCE OF THE ITEM IN THE SET BEFORE DELETION
vegetables.discard("potato")

print(vegetables)

# To remove one item at random, use pop()
vegetables.pop()
print(vegetables)


# * ------------------------------ Set Operations ------------------------------ #

# Sets provide unique operations that can efficiently compare collections

# UNION: combines two sets, includes all the members of both sets and includes duplicate members only once
letters = {"a", "b", "c"}
numbers = {1, 2, 3}

letters_and_numbers = letters.union(numbers)

# OR:
letters_and_numbers = letters | numbers


print(letters_and_numbers)  # {'a', 'c', 1, 2, 3, 'b'}


# INTERSECTION: creates a new set containing the elements common to both sets.
mod_2 = {2, 4, 6, 8, 10, 12, 14, 16, 18}
mod_3 = {3, 6, 9, 12, 15, 18}

mod_6 = mod_2.intersection(mod_3)

# OR:
mod_6 = mod_2 & mod_3

print(mod_6)  # {18, 12, 6}


# DIFFERENCE: order matters!!! See below
bundle_1 = {"Resident Evil 3", "Final Fantasy VII", "Cyberpunk 2077"}
bundle_2 = {"Doom Eternal", "Halo Infinite", "Resident Evil 3"}

print(bundle_1.difference(bundle_2))  # {'Final Fantasy VII', 'Cyberpunk 2077'}
print(bundle_2.difference(bundle_1))  # {'Halo Infinite', 'Doom Eternal'}
# set1.difference(set2) will print all elements of set1 that ARE NOT CONTAINED within set2

# OR:
print(bundle_1 - bundle_2)
print(bundle_2 - bundle_1)


# SYMMETRIC DIFFERENCE: gives all of the items which only feature in one of the sets. Unlike difference(), the order does not matter

bundle_1 = {"Resident Evil 3", "Final Fantasy VII", "Cyberpunk 2077"}
bundle_2 = {"Doom Eternal", "Halo Infinite", "Resident Evil 3"}

# {'Cyberpunk 2077', 'Final Fanstay VII', 'Halo Infinite', 'Doom Eternal'} includes everything from both sets except what is contained in both
print(bundle_1.symmetric_difference(bundle_2))


# * ------------------- Set Operations With Other Collections ------------------ #

# We can combine a list with a set:
letters = {"a", "b", "c"}
numbers = [1, 2, 3]

letters_and_numbers = letters.union(numbers)

print(letters_and_numbers)  # {'a', 'c', 1, 2, 3, 'b'}

# Combining a set with a tuple:
letters = {"a", "b", "c"}
numbers = (1, 2, 3)

letters_and_numbers = letters.union(numbers)

print(letters_and_numbers)  # {'a', 'c', 1, 2, 3, 'b'}


# * ------------------- Checking if items are in Collections ------------------- #

# NOTE: To check if a value is in a collection, we can use the "in" keyword which returns True if the value specified is found:

numbers = {1, 2, 3, 4, 5}

print(3 in numbers)  # True
print(7 in numbers)  # False

# We can do this for any collection, such as a string:
print("j" in "Python")  # False
print("n" in "Python")  # True


# We can use "in" to check if a key is in a dictionary!:
student = {
    "name": "Eric Cartman",
    "age": 10,
    "school": "South Park Elementary"
}

print("grades" in student)  # False
print("school" in student)  # True

# or among its values:

print(10 in student.values())  # True


print("\n\n")


# ---------------------------------------------------------------------------- #
# *                                   Exercises                                  #
# ---------------------------------------------------------------------------- #

# 1) Create an empty set and assign it to a variable.
new_set = set()


# 2) Add three items to your empty set using either several add calls, or a single call to update.
new_set.update({1, 2, 3})


# 3) Create a second set which includes at least one common element with the first set.
second_set = {1, 4, 5, 6}


# 4) Find the union, symmetric difference, and intersection of the two sets. Print the results of each operation.

print(new_set.union(second_set))  # Prints

print(new_set.symmetric_difference(second_set))

print(new_set.intersection(second_set))

# 5) Create a sequence of numbers using range, then ask the user to enter a number. Inform the user whether or not their number was within the range you specified.

numbers = range(2, 36)

user_input = int(input("Enter an integer: "))

if user_input in numbers:
    print("Your number was in the list!")
else:
    if user_input < numbers[0]:
        print("Your number is too low.")
    else:
        print("Your number is too high.")

# NOTE: for the above --> If the user's number isn't within the specified series of numbers, we can check the user's number against the first value in the range. If it's lower than this number, the user's value was too low. Otherwise it must have exceeded the highest value in the range.
