# ------------------------------------ -- ------------------------------------ #
# ----------------- This file will scrape the entire 50 page ----------------- #
# ------------ catalogue of books from http://books.toscrape.com/ ------------ #
# ------------------------------------ -- ------------------------------------ #

from typing import List

## Requests Functions
import requests

def create_url_list( url: str, n_pages: int ) -> List[ str ]:
    url_list = [ url ]
    
    for n in range( 2, n_pages + 1 ):
        url_list.append( url + "catalogue/page-" + str( n ) + ".html" )
            
    return url_list


def get_html_data( url: str ) -> bytes :
    return requests.get( url ).content



## BeautifulSoup Functions    
from bs4 import BeautifulSoup

def get_soup( data: bytes ) -> BeautifulSoup:
    return  BeautifulSoup( data, "html.parser" )


def retrieve_soup_data( soup: BeautifulSoup, css_selector: str ):
    return soup.select( css_selector )


def write_to_file( titles, prices, ratings ):
    with open( "./scraped_books_entire_site.csv", mode="a" ) as output_file:        
        for title, price, rating in zip( titles, prices, ratings ):
            output_file.write( f"{title[ 'title' ]},{price.string},{rating[ 'class' ][ 1 ]}\n" )
    


# Intial url to scrape
html_to_scrape: str = "http://books.toscrape.com/"

# From above url, create list of all urls on site to scrape
scrape_list: List[ str ] = create_url_list( html_to_scrape, 50 )

# For each url in list, get html data
data_list: List[ bytes ] = []
for url in scrape_list:
    data_list.append( get_html_data( url ) )


# Get soup for each url
soup_list: List[ BeautifulSoup ] = []
for data in data_list:
    soup_list.append( get_soup( data ) )


# Write all soup data to file
for soup in soup_list:
    titles = retrieve_soup_data( soup, ".product_pod h3 a" )
    prices = retrieve_soup_data( soup, ".price_color" )
    ratings = retrieve_soup_data( soup, ".star-rating" )
    
    for title, price, rating in zip( titles, prices, ratings ):
        print( f"{title[ 'title' ]} has a rating of {rating[ 'class' ][ 1 ]} stars and costs {price.string}" )
    
    # Write all information from each soup (each webpage) to file
    write_to_file( titles, prices, ratings ) 
        
    
