

def read_column( column ):
    ## Reads a specific column of data from iris.csv and returns it
        
    column_data = []
    
    # Read all columns from iris.csv (besides headers)
    with open( "./iris.csv", mode="r" ) as iris:
    
        for row in iris.readlines()[ 1: ]:
            
            data = row.strip().split( "," )
            column_data.append( data[ column ] ) # we only want the specified column
            
          
    # NOTE: column_data is contains a list of STRINGS
    return column_data
        


def read_headers():
    ## Reads the first row of iris.csv and returns it as "headers"
    
    with open( "./iris.csv", mode="r" ) as iris_file:
	    iris_data = iris_file.readlines()

    headers = iris_data[0].strip().split( "," )[ :-1 ] # capture every header except last  (species)
            
    return headers


def print_axis_options( headers ):
    ## Takes the headers list and prints them to the user to choose which to use as the y-axis
    
    print( "\nY-Axis options to plot against Iris Species:" )
    
    for count, header in enumerate( headers, start=1) :
        print( f"{count}.) {header}" )
        
    print() # extra whitespace