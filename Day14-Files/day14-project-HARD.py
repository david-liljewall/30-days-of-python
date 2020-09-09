# ---------------------------------------------------------------------------- #
#                        Day 14 Project -- HARD VERSION                        #
# ---------------------------------------------------------------------------- #


## Goal: 
    # Users should be able to add a book to their reading list by providing a book title, an author's name, a year of publication, and whether or not the book has been read.
    # Users should be able to mark a book as read by entering a book title. If there are multiple books with the same title, you can just mark the first matching book as read.
    # Users should be able to delete books from their reading list by providing the book title for the book they want to delete. Once again, you can just delete the first matching book.



# --------------------------- FUNCTION DEFINITIONS --------------------------- #

def add_book():
    ## Function adds a book to reading_list.csv via user input to the terminal. The user enters the title, author, publication year, and read status - the function takes that information, turns into a string (where each piece of info is separated by a comma) and and appends that to the .csv file

    # User input for book information
    title = input( "Please enter the book title: " ).strip()
    author = input( "Please enter the author: " ).strip()
    publication_year = input( "Please enter the publication year: " ).strip()

    read = input( "Have you read this book already? (y/n) " ).strip().lower()
    if read == "y":
        read = "Read"
    elif read == "n":
        read = "Not Read"


    # Append book to .csv file
    with open( "./reading_list.csv", mode="a" ) as file:
        file.write( f"{title},{author},{publication_year},{read}\n" )


def get_book_list():
    ## Reads lines from .csv file, appends that to a list of dictionaries where each dictionary is a book, and returns the list. 

    # read lines from .csv file
    with open( "./reading_list.csv", mode="r" ) as file:
        book_data = file.readlines()


    # Create a list of dictionaries whereby each dictionary is a book
    reading_list = []

    for row in book_data:
        title, author, publication_year, read = row.split( "," )
        
        reading_list.append( {
            "title": title,
            "author": author,
            "publication_year": publication_year,
            "read": read
        } )         

    return reading_list


def display_book_list():
    ## Prints data from the list returned from the get_book_list() function

    # Retrieve book list from .csv file 
    reading_list = get_book_list( )

    print( "\n<< Reading List >>\n" )

    # Print enumerated reading list
    for count, book in enumerate( reading_list, start=1 ):
        print( f"Book {count}: {book['title']} by {book['author']} ({book['publication_year']}) -- {book['read']}" )
    


def search_book():
    ## Finds relevant book information based on a book title provided via user input

    # Retrieve book list from .csv file 
    reading_list = get_book_list( )
    
    # Display book list
    display_book_list()

    target = input( "Please enter book title: " ).strip()

    print( "\n<< Searched Book >>\n" )

    # Loop through book dictionaries in reading_list till a string match is found
    for book in reading_list:
        
        if target == book[ 'title' ]:
            print( f"{book['title']} by {book['author']} ({book['publication_year']}) -- {book['read']}" )
        
       
            
def mark_read():
    ## User enters a book title and the function takes the first matching title and marks that it has been read (sets 'read' status to "Read")
    
    # Retrieve book list from .csv file 
    reading_list = get_book_list( )
    
    # Retrieve/display book list
    display_book_list( )

    # User input for target book
    target = input( "Please enter book title: " ).strip()

    # Loop through book dictionaries in reading_list till a string match is found
    for book in reading_list:
        
        if target == book[ 'title' ]:
            book[ 'read' ] = "Read\n" # new line needed to separate books into rows
                        
            break
        
    # Write newly edited book list to .csv file
    with open( "./reading_list.csv", mode="w" ) as file:
        
        # write all books in reading_list to file:
        for book in reading_list:
            
            ## NOTE: do not add \n after 'read' because the newly marked read books already have the "\n", and the books in reading_list also have it at the end already
            file.write( f"{book['title']},{book['author']},{book['publication_year']},{book['read']}" )
            
        
   


def delete_book():
    ## User enters a book title and the function removes this book from the .csv file

    # Retrieve book list from .csv file 
    reading_list = get_book_list( )

    # Display book list
    display_book_list(  )

    # User input for target book
    target = input( "Please enter book title: " ).strip()

    # Verify user wants to delete book from list
    option = input( "Are you sure you want to delete this book from your list? (y/n) " ).strip().lower()

    if option == "y":
        # Loop through book dictionaries in reading_list till a string match is found
        for index in range( len( reading_list ) ):
            
            if target == reading_list[index][ 'title' ]:
                del reading_list[ index ]
                
        # Write newly edited book list to .csv file
        with open( "./reading_list.csv", mode="w" ) as file:
            
            # write all books in reading_list to file:
            for book in reading_list:
                file.write( f"{book['title']},{book['author']},{book['publication_year']},{book['read']}" )



# ------------------------------- MAIN PROGRAM ------------------------------- #

if __name__ == "__main__":
    
    # Menu Loop:
    while True:
        print( "\n\n" ) # extra whitespace

        print( "Please select from the options below:" )
        
        menu_option = input (
            "\n     1) Add a book to your reading list"
            "\n     2) Display your reading list"
            "\n     3) Mark book as read"
            "\n     4) Search for a book in your reading list"
            "\n     5) Delete book from reading list"
            "\n     6) Quit program"
            "\n"
        )
        
        
        # conditionals for menu option selection:
        if menu_option == "1":
            add_book()
        
        elif menu_option == "2":
            display_book_list()
        
        elif menu_option == "3":
            mark_read()
        
        elif menu_option == "4":
            search_book()
        
        elif menu_option == "5":
            delete_book()
        
        elif menu_option == "6":
            print( "You have successfully exited the program\n" )
            break
        
        else:
            print( "Error -- your entry is invalid. Please try again." )