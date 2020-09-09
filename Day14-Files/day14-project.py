# ---------------------------------------------------------------------------- #
#*                          Reading List (Easy Version)                         #
# ---------------------------------------------------------------------------- #

## NOTE: Majority of code taken from day12-project - added file functionality to this one


#* --------------------------- Function Definitions --------------------------- #

## Adapted from day12-project --> inefficient because it creates a dictionary and then reads data from that to write to the file, instead of just writing to it directly:
# def add_book_to_csv(  ):
    
#     # Initialize local variables:
#     book = {}
#     title = ""
#     author = ""
#     publication_year = 0
    
#     # Terminal prompts
#     print( "Please enter the following information for the book you'd like to add to your list:") 
    
#     title = input( "    Book Title: " )
#     author = input( "   Author's Name: " )
#     publication_year = int( input( "    Year of Publication: " ) )


#     # Add book information to book{}
#     book.update( {"Title": title, "Author": author, "Publication Year": publication_year} )
    
    
#     # Parse book{} information and put into .csv file
#     with open( "./reading_list.csv", mode="a" ) as output_csv:
#         # Add a new line before writing to file to separate book information
#         output_csv.write( "\n" )
        
#         # Write book information to file
#         for value in book.values():
#             output_csv.write( value )
#             output_csv.write( "," )
    
            
def add_book_to_csv():
    # Terminal prompts
    print( "Please enter the following information for the book you'd like to add to your list:") 
    
    title = input( "Book Title: " ).strip()
    author = input( "Author's Name: " ).strip()
    publication_year = int( input( "Year of Publication: " ).strip() )
    read_status = input( "" )
    
    with open( "./reading_list.csv", mode="a" ) as output_csv:
        # Add a new line before writing to file to separate book information        
        output_csv.write( f"{title},{author},{publication_year}\n" )
    
    
def get_book_list():
    # Convert read data into a dictionary to be read from
    with open( "./reading_list.csv", mode="r" ) as f:
        reading_list_data = f.readlines()
        
        reading_list = []
        
        for row in reading_list_data:
            title, author, publication_year = row.strip().split( "," )
            
            reading_list.append( {
                "Title": title,
                "Author": author,
                "Publication Year": publication_year
            } )
            
    return reading_list
    
    
def display_book_list( reading_list=list ):
    
    # Parse reading_list book dictionaries and print to terminal
    print( "\n<< Reading List >>" )
    for count, book in enumerate( reading_list, start=1 ):
        print( f"   {count}: {book['Title']} by {book['Author']} ({book['Publication Year']})" )
            

        
def search_book_list( reading_list=list ):
    
    target = input( "Please enter the name of the book you are looking for: " ).strip()
    
    # Search reading_list for book title match
    for book in reading_list:

        if target == book[ 'Title' ]:
            print( "<< The book you searched for is:" )
            print( f"{book['Title']} by {book['Author']} ({book['Publication Year']})" ) 
            
        



#* ------------------------------- Main Program ------------------------------- #

# Initialize empty book list
book_list = []

menu_option = ""
# Menu Loop:
while True:
    print( "\n\n" ) # extra whitespace

    print( "Please select from the options below:" )
    
    menu_option = input (
        "\n     1) Add a book to your reading list"
        "\n     2) Display your reading list"
        "\n     3) Search for a book in your reading list"
        "\n     4) Quit program"
        "\n"
    )
    
    
    # conditionals for menu option selection:
    if menu_option == "1":
        add_book_to_csv()
        
    elif menu_option == "2":
        book_list = get_book_list()
        
        if book_list:
            display_book_list( book_list )
        else: 
            print( "Your eading list is empty." )
            
    elif menu_option == "3":
        search_book_list( book_list )
    
    elif menu_option == "4":
        print( "You have successfully exited the program!" )
        break
    
    else:
        print( "Error -- your entry is invalid. Please try again." )