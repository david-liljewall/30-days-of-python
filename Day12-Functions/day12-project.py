# ---------------------------------------------------------------------------- #
#                                   PROJECT!                                   #
# ---------------------------------------------------------------------------- #

##* For this project the application needs to have the following functionality:

# 1) Users should be able to add a book to their reading list by providing a book title, an author's name, and a year of publication.
# 2) The program should store information about all of these books in a Python list.
# 3) Users should be able to display all the books in their reading list, and these books should be printed out in a user-friendly format.
# 4) Users should be able to select these options from a text menu, and they should be able to perform multiple operations without restarting the program. You can see an example of a working menu in the post on while loops (day 8).





#* --------------------------- Function Definitions --------------------------- #

def add_book( reading_list=list ):
    print( "\n\n" ) # extra whitespace
    
    # initialize local variables:
    book = {}
    title = ""
    author = ""
    publication_year = 0
    
       
    print( "Please enter the following information for the book you'd like to add to your list:") 
    
    title = input( "    Book Title: " )
    author = input( "   Author's Name: " )
    publication_year = int( input( "    Year of Publication: " ) )

    # Add book information to book{}
    book.update( {"Title": title, "Author": author, "Publication Year": publication_year} )
    
    # Add book to reading_list[]
    reading_list.append( book )


def display_book_list( reading_list=list ):
    print( "\n\n" ) # extra whitespace
    
    # Iterate through reading_list, print in a readable format
    for book in reading_list:
        for key, value in book.items():
            print( f"   {key} --> {value}" )



#* ------------------------------- Main Program ------------------------------- #

# Initialize empty book list
book_list = []

menu_option = ""
# Menu Loop:
while True:

    print( "\n\n" ) # extra whitespace

    print( "Please select from the options below:" )
    print(
        "\n     1) Add a book to your reading list"
        "\n     2) Display your reading list"
        "\n     3) Quit program"
    )

    menu_option = input()
    # conditionals for menu option selection:
    if menu_option == "1":
        add_book( book_list )
    elif menu_option == "2":
        display_book_list( book_list )
    elif menu_option == "3":
        print( "You have successfully exited the program!" )
        break
    else:
        print( "Error -- your entry is invalid. Please try again." )
        
