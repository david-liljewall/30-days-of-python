from bs4 import BeautifulSoup


## Here is some sample HTML code from the BeautifulSoup documentation:
html_doc = """
<html>

<head>
	<title>The Dormouse's story</title>
</head>

<body>
	<p class="title"><b>The Dormouse's story</b></p>

	<p class="story">
		Once upon a time there were three little sisters; and their names were
		<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
		<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
		<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
		and they lived at the bottom of a well.
	</p>

</body>

</html>
"""

soup = BeautifulSoup( html_doc, "html.parser" )


# ----------------------- Getting data out of the soup ----------------------- #

## The items inside soup are "Tag" objects, which is a construct of BeautifulSoup.
	# When we search throup the soup object, we'll get back a Tag or list of Tag objects
	# 
 
sisters = soup.select( ".sister" )
	# Gives back a list of <a> elements as Tag objects, using .sister as the CSS selector for class="sister"
## NOTE: to search by id, we would use "#" followed by the name of the id.
	# I.e., to search for the link1 id, we'd use "#link1", which is the id for Elsie above

# Loop through list of Tags, where each "sister" is a Tag in the list
print( "Search by class='sister'" )

for sister in sisters:
    print( sister.string )
    
print(  )
sisters_id = soup.select( "#link1" )

print( "\nSearch by id='link1'" )

for sis_id in sisters_id:
    print( sis_id.string )

print() 

## Creating a tag object from looking at the first <p> element
tag = soup.p
print( tag.name )
print( tag[ 'class' ] )
print( tag.attrs )