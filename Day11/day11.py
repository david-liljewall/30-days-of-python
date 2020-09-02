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

