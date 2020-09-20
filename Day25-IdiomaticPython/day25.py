# ---------------------------------------------------------------------------- #
#                               IDIOMATIC PYTHON                               #
# ---------------------------------------------------------------------------- #



#* ------------------------ Truth values as conditions ------------------------ #

## Instead of doing this:
my_list = []

if len(my_list) == 0:
	print("The list is empty")
else:
	values = ', '.join(str(value) for value in my_list)
	print("The list contains: {values}")
 
## "pythonic" code looks like this:
my_list = []

if my_list:
	values = ', '.join(str(value) for value in my_list)
	print("The list contains: {values}")
else:
	print("The list is empty")


## NOTE: This approach is especially useful for checking whether or not a function or method returned None:
from operator import add, mul, sub, truediv

operations = {
	"add": add,
	"divide": truediv,
	"multiply": mul,
	"subtract": sub
}

selected_option = input("Select the operation to perform: ").strip().lower()

operation = operations.get(selected_option)  # returns None if the key is invalid

if operation:
	a = input("Please enter a value for the first operand: ")
	b = input("Please enter a value for the second operand: ")

	print(operation(a, b))
else:
	print("Invalid operation")
