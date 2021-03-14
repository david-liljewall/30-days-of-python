# ---------------------------------------------------------------------------- #
#*                             WEB SCRAPING PROJECT                             #
# ---------------------------------------------------------------------------- #

## DATA WANTED:
    # Title
    # Star rating
    # Price
    #* write all this information to a new file in CSV format (headers = title, star, price)

## Book title:
    # <a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">, where href and title behave as keys. So to find the title, we would do tag[ 'title ]
    # Note -> each book is within a "product_pod" class: <article class="product_pod">
    # NOTE: the CSS selector for the title is: ".product_pod h3 a" --> looks for <a> elements that live inside of <h3> elements, that are within an element with the class "product_pod"



# ------ First we need the HTML document of the web page we are scraping ----- #
import requests

data = requests.get( "http://books.toscrape.com/" ).content



# ----------------------- Convert HTML to BeautifulSoup ---------------------- #
from bs4 import BeautifulSoup


soup = BeautifulSoup( data, "html.parser" )

# Create .html file for reference
with open( "./books_to_scrape.html", mode="w" ) as file:
    file.write( soup.prettify() )


# Retrieve relevant information about each book
titles = soup.select( ".product_pod h3 a" )
prices = soup.select( ".price_color" )    
ratings = soup.select( ".star-rating" )


# Print information to terminal
for title, price, rating in zip( titles, prices, ratings ):
    print( f"{title[ 'title' ]} has a rating of {rating[ 'class' ][ 1 ]} stars and costs {price.string}" )


# Write information to file
with open( "./scraped_books.csv", mode="w" ) as output_file:
    # Write headers
    output_file.write( "title,price,star_rating\n" )
    
    for title, price, rating in zip( titles, prices, ratings ):
        output_file.write( f"{title[ 'title' ]},{price.string},{rating[ 'class' ][ 1 ]}\n" )