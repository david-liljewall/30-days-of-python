## 2) Create a function that accepts any number of positional and keyword arguments, and that prints them back to the user. Your output should indicate which values were provided as positional arguments, and which were provided as keyword arguments.

def arg_printer(*args, **kwargs):
	args = [repr(arg) for arg in args]
	print(f"Positional arguments are: {', '.join(args)}")

	kwargs = [f"{key}={repr(value)}" for key, value in kwargs.items()]
	print(f"Keyword arguments are: {', '.join(kwargs)}")

## 3) Print the following dictionary using the format method and ** unpacking.

country = {
	"name": "Germany",
	"population": "83 million",
	"capital": "Berlin",
	"currency": "Euro"
}

country_template = """Name: {name}
Population: {population}
Capital: {capital}
Currency: {currency}"""

print(country_template.format(**country))



## 4) Using * unpacking and range, print the numbers 1 to 20, separated by commas. You will have to provide an argument for print function's sep parameter for this exercise.

print( *range(1, 21 ), sep = ", " )


## 5) Modify your code from exercise 4 so that each number prints on a different line. You can only use a single print call.

print( *range(1, 21 ), sep = "\n" )