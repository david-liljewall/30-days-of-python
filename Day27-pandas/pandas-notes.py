# ---------------------------------------------------------------------------- #
#                          Notes on Pandas module use                          #
# ---------------------------------------------------------------------------- #



#* ---------------------- The Series and DataFrame types ---------------------- #
import pandas as pd

## NOTE: The "DataFrame" type is used to store tabular data, consisting of rows and columns which can be populated with data. Each column in the data fram is called a "Series"
# To create, we can use:
# 1.) Dictionary
movies = {
	"title": ("Inception", "Pirates of the Caribbean: The Curse of the Black Pearl"),
	"director": ("Christopher Nolan", "Gore Verbinski"),
	"year": (2010, 2003)
}

df = pd.DataFrame( movies )
print( df ) 

# To see a specific subset of the DataFrame, use df.head():
print( df.head( 1 ) ) # prints info about Inception



#* --------------------------- Modifying a DataFrame -------------------------- #

## Renaming Headers
new_df = df.rename( columns={ "year": "release_year" } )
    # We have renamed the "year" column into "release_year" by making a copy of df and then modifying it
print( new_df )

# NOTE: To modify inplace, i.e. change the original DataFrame instead of creating a copy and then modifying it:
df = pd.DataFrame(movies)
df.rename(columns={"year": "release_year"}, inplace=True)
print( df )


## Throwing away columns
df_without_director = df.drop( columns="director" )
print( df )
print( df_without_director )

# If instead we want to specify which columns to KEEP:
df = df[ [ "title", "release_year" ] ] 
print( df )



#* ---------------------------- Filtering by values --------------------------- #

## Query Method: To search for specific data in a DataFrame, we can use the query method:
    # specify a string which gives a condition to filter the DataFrame with.
    # query method returns a DataFrame that satisfies the condition we posed it
print( "\n\n" )


movies = {
	"title": ("Inception", "Pirates of the Caribbean: The Curse of the Black Pearl"),
	"director": ("Christopher Nolan", "Gore Verbinski"),
	"year": (2010, 2003)
}

df = pd.DataFrame( movies )


nolan_movies = df.query( "director == 'Christopher Nolan'" )
print( nolan_movies )

# NOTE: to modify to the DataFrame object created above, we have to use .copy(). We cannot modify a copy of a slice from a DataFrame inplace, we must create a copy:
nolan_movies.copy().rename( columns={"title": "movie_title"}, inplace=True )
#or:
nolan_movies = nolan_movies.rename( columns={"title": "movie_title"} )
