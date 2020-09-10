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