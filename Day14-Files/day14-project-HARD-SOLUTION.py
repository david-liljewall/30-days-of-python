def add_book():
	title = input("Title: ").strip().title()
	author = input("Author: ").strip().title()
	year = input("Year of publication: ").strip()

	with open("./reading_list.csv", "a") as reading_list:
		reading_list.write(f"{title},{author},{year},Not Read\n")


def delete_book(books, book_to_delete):
	books.remove(book_to_delete)


def find_books():
	reading_list = get_all_books()
	matching_books = []

	search_term = input("Please enter a book title: ").strip().lower()

	for book in reading_list:
		if search_term in book["title"].lower():
			matching_books.append(book)

	return matching_books


# Helper function for retrieving data from the csv file
def get_all_books():
	books = []
	
	with open("./reading_list.csv", "r") as reading_list:
		for book in reading_list:
			# Extracts the values from the CSV data
			title, author, year, read_status = book.strip().split(",")

			# Creates a dictionary from the csv data and adds it to the books list
			books.append({
				"title": title,
				"author": author,
				"year": year,
				"read": read_status
			})

	return books


def mark_book_as_read(books, book_to_update):
	index = books.index(book_to_update)
	books[index]['read'] = "Read"


def update_reading_list(operation):
	books = get_all_books()
	matching_books = find_books()
	
	if matching_books:
		operation(books, matching_books[0])
        
		
		with open("./reading_list.csv", "w") as reading_list:
			for book in books:
				reading_list.write(f"{book['title']},{book['author']},{book['year']},{book['read']}\n")
	else:
		print("Sorry, we didn't find any books matching that title.")


def show_books(books):
	# Adds an empty line before the output
	print()
	
	for book in books:
		print(f"{book['title']}, by {book['author']} ({book['year']}) - {book['read']}")

	print()


menu_prompt = """Please enter one of the following options:

- 'a' to add a book
- 'd' to delete a book
- 'l' to list the books
- 'r' to mark a book as read
- 's' to search for a book
- 'q' to quit

What would you like to do? """

# Get a selection from the user
selected_option = input(menu_prompt).strip().lower()

# Run the loop until the user selected 'q'
while selected_option != "q":
	if selected_option == "a":
		add_book()
	elif selected_option == "d":
		update_reading_list(delete_book)
	elif selected_option == "l":
		# Retrieves the whole reading list for printing
		reading_list = get_all_books()

		# Check that reading_list contains at least one book
		if reading_list:
			show_books(reading_list)
		else:
			print("Your reading list is empty.")
	elif selected_option == "r":
		update_reading_list(mark_book_as_read)
	elif selected_option == "s":
		matching_books = find_books()
		
		# Checks that the seach returned at least one book
		if matching_books:
			show_books(matching_books)
		else:
			print("Sorry, we didn't find any books for that search term")
	else:
		print(f"Sorry, '{selected_option}' isn't a valid option.")

	# Allow the user to change their selection at the end of each iteration
	selected_option = input(menu_prompt).strip().lower()
