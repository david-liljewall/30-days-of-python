## 3) Texas Hold'em
from random import shuffle

ranks = [ "ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king" ]
suits = [ "clubs", "spades", "diamonds", "hearts" ]

def create_deck( suits=list, ranks=list ):
    deck = []
    # Map each card to the suit till each suit holds all 13 cards
    for suit in suits:
        for card in ranks:
            deck.append( ( card, suit ) )
            
    return deck


deck = create_deck( suits, ranks )
shuffle( deck )

# Create iterator from shuffled deck
shuffled_deck = iter( deck )

# Could also use a generator expression to create a similar iterable object:
shuffled_deck_gen = ( list( card ) for card in deck )

# User input for number of players
n_players = int( input( "How many players are there? " ).strip() )

# Tracks number of hands
hands_counter = 1

## GAME START:
    # Loop till the entire deck has been consumed!
while True:
    try:
        print(f"\n<< Hand # {hands_counter} >>\n" ) 
        
        for n in range(n_players):
            print( f"Player {n + 1} was dealt: {str(next(shuffled_deck))}, {str(next(shuffled_deck))}" )

        print() # extra whitespace

        # Flop:
        print( f"The flop: {next(shuffled_deck)}, {next(shuffled_deck)}, {next(shuffled_deck)}" )
        # Turn:
        print( f"The turn: {next(shuffled_deck)}" )
        # River:
        print( f"The river: {next(shuffled_deck)}" )
        
        hands_counter += 1 # incremement number of hands dealt
        
    except StopIteration:
        print( "GAME OVER!" )
        break