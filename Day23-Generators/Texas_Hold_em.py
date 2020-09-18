## 3) Texas Hold'em
from random import shuffle

def shuffle_deck( suits=list, ranks=list ):
    # Map each card to the suit till each suit holds all 13 cards
    deck = [ ( rank, suit ) for rank in ranks for suit in suits ]
    
    shuffle( deck )
    
    return iter( deck )


def deal_hand( n_players, hands_counter ):
    print(f"\n<< Hand # {hands_counter} >>\n" ) 
        
    for n in range(n_players):
        print( f"Player {n + 1} was dealt: {str(next(shuffled_deck))}, {str(next(shuffled_deck))}" )

    print() # extra whitespace

    # Flop:
    print( f"The flop: {str(next(shuffled_deck))}, {str(next(shuffled_deck))}, {str(next(shuffled_deck))}" )
    # Turn:
    print( f"The turn: {str(next(shuffled_deck))}" )
    # River:
    print( f"The river: {str(next(shuffled_deck))}" )
    
    
    
## Data for game:
ranks = [ 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace" ]
suits = [ "clubs", "spades", "diamonds", "hearts" ]
shuffled_deck = shuffle_deck( ranks, suits )

# User input for number of players
n_players = int( input( "How many players are there? " ).strip() )



## GAME START:
# Loop till the entire deck has been consumed!
hands_counter = 1

while True:
    try:
        deal_hand( n_players, hands_counter )
        hands_counter += 1 # incremement number of hands dealt
    
    except StopIteration:
        print( "GAME OVER!" )
        break
    