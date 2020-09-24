
##* Project outline:
    # 1.) I want to know which region had the lowest average price for conventionally grown avocados each year, and I want to know the same information for organic avocados.
    # 2.) I want to know which region had the highest average price for both types of avocado for each given year.
    # 3.) I want to know the lowest all time price for both conventionally grown and organic avocados, and I want to know the highest price as well.
    
    
import pandas as pd


def filter_by_year( df, year ):
    return df.query( "year == @year" ).drop( columns="year" )
        # NOTE: use an "@" symbol if you want to query using a variable. In this case, the function parameter 

def get_average_by_year( df ):
    averages = {}
    
    # List of unique years in original DataFrame
    years = df.year.unique()

    for year in years:
        averages_for_year = filter_by_year( df, year ).groupby( "region" ).mean()
        averages.update( { year: averages_for_year } )
        
    return averages

def lowest_ave_price( dic ):
    for year, data in dic.items():
        lowest_value = data.price.min()
        location = data.query( "price == @lowest_value" ).index[ 0 ]
        print( f"Lowest price for conventional avocados in {year} was ${lowest_value:.2f} in {location}" )

def highest_ave_price( dic ):
    for year, data in dic.items():
        highest_value = data.price.max()
        location = data.query( "price == @highest_value" ).index[ 0 ]
        print( f"Highest price for conventional avocados in {year} was ${highest_value:.2f} in {location}" )


# Use pd.read_csv to create a DataFrame
with open( "./avocado.csv", mode="r" ) as file:
    df = pd.read_csv( file ).rename( columns={ "AveragePrice": "price" } )
    
# Create subset of original DataFrame of essential data (Average price, type, year, region)
df = df[ [ "year", "region", "price", "type" ] ]


# Filter by conventional, organic avocados. Drop the "type" column since they're already sorted that way
conventional = df.query( "type == 'conventional'" ).copy()
conventional.drop( columns="type", inplace=True )

organic = df.query( "type == 'organic'" ).copy()
organic.drop( columns="type", inplace=True )


# Compute average prices for each year
conventional_average = get_average_by_year( conventional )
organic_average = get_average_by_year( organic )


# Print lowest/highest prices for conventional and organic avocados
lowest_ave_price( conventional_average )
print()
highest_ave_price( conventional_average )

print()

lowest_ave_price( organic_average )
print()
highest_ave_price( organic_average )

print()


# Calculate the overall lowest and highest values for both types of avocados:
max_conventional = conventional.price.max()
min_conventional = conventional.price.min()

max_organic = organic.price.max()
min_organic = organic.price.min()

print(f"The highest price for conventional avocados was ${max_conventional:.2f}")
print(f"The lowest price for conventional avocados was ${min_conventional:.2f}")

print(f"The highest price for organic avocados was ${max_organic:.2f}")
print(f"The lowest price for organic avocados was ${min_organic:.2f}")