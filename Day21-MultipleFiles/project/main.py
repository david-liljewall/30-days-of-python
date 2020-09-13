# ---------------------------------------------------------------------------- #
#*                                Day 21 Project                                #
# ---------------------------------------------------------------------------- #

## Goal:
    # Create a scatter plot where the x axis is the species and the y axis is one of the other columns.
    # Via a user menu, tell us the column they would like to plot in the y axis.
    # Also via the menu, tell us the name of the file they would like to create to contain the final plot image.
    




# Import relevant files for data storage and graphing:
import data_storage, graphing


# ------------------------------------ -- ------------------------------------ #
# ------------------------------- Program Start ------------------------------ #

user_menu = """Please choose from the following options:

- Enter 'c' to chart a new graph.
- Enter 'q' to quit.

Your selection: """

charting_menu = "Enter the number of the column you'd like to chart: "

filename_prompt = "Enter your desired file name: "



def handle_chart():

    column = int( input( charting_menu ) ) - 1 # if they enter 1 for sepal_length, need to choose 0th column
    
    # create scatter plot from x-axis (species = last column) and y-axis (column)
    x = data_storage.read_column( -1 )
    y = [ float( n ) for n in data_storage.read_column( column ) ]
    filename = input( filename_prompt ).strip().lower()
    
    graphing.create_chart( x, y, filename )
    

# ----------------------------------- Main ----------------------------------- #
if __name__ == "__main__":
    
    while True:
        # Initiate menu prompt for user
        user_selection = input( user_menu )
        
        if user_selection == "c":
            data_storage.print_axis_options( data_storage.read_headers() )
            handle_chart()
            
        elif user_selection == "q":
            break
        
        else:
            print( f"Sorry, '{user_selection}' is not a valid option." )