# ---------------------------------------------------------------------------- #
#                                    PROJECT                                   #
# ---------------------------------------------------------------------------- #


# *Goal:
# 1) Calculate the average budget of all movies in the data set.
# 2) Print out every movie that has a budget higher than the average you calculated. You should also print out how much higher than the average the movie's budget was.
# 3) Print out how many movies spent more than the average you calculated.



movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]


# 1)

tot_budget = 0

# iterate through each movie (tuple)
for movie in movies:
    tot_budget += movie[1] 

avg_budget = int( tot_budget / len( movies ) )


# 2) & 3)
count = 0

for movie in movies:
    if movie[1] > avg_budget:
        count += 1
        print( f"{movie[0]} was ${movie[1] - avg_budget} higher than average" )    
print( f"There were {count} movies more than the average budget" )