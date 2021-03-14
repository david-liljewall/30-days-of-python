
#* --------------- Game environment and global variables initialization -------------- #
import sys
import pygame
from random import randint
from collections import namedtuple
from typing import List


## Define relevant game object colors:
Color = namedtuple("color", ["red", "green", "blue"])

BACKGROUND_COLOR = Color( red=0, green=0, blue=0 ) # black
TEXT_COLOR = Color( red=255, green=255, blue=255 ) # white
SNAKE_COLOR = Color( red=0, green=180, blue=0 ) # green
FOOD_COLOR = Color( red=255, green=255, blue=0 ) # yellow


## Define which keys correspond to the 4 directions the snake can move 
KEY_MAP = {
    273: "Up",
    274: "Down",
    275: "Right",
    276: "Left"
}


## Define snake size, food size, and snake velocity (based on user input)
SEGMENT_SIZE = 20

difficulty = input("\n"
    '''On what Difficulty would you like to play Snake?:
        '1' --> Easy
        '2' --> Medium
        '3' --> Hard
        '4' --> Go Home, You're Drunk
        '5' --> I'm Scared
    '''
).strip()

if difficulty == "1":
    SNAKE_VELOCITY = 10
elif difficulty == "2":
    SNAKE_VELOCITY = 20
elif difficulty == "3":
    SNAKE_VELOCITY = 30
elif difficulty == "4":
    SNAKE_VELOCITY = 40
elif difficulty == "5":
    print( "You're too scared? Your mother would be ashamed..." )
    sys.exit()



## Initialize pygame environment: caption, screen size, clock
pygame.init()

pygame.display.set_caption( "SNAKE GAME" )

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode( [ 1200, 1000 ] )
clock = pygame.time.Clock()


## Initialize font object to be used throughout
font = pygame.font.Font( None, 25 )


#* ------------------------------- My Functions ------------------------------- #
def render_score( player_score: int, string: str, color: Color ):
    pygame.draw.rect( screen, BACKGROUND_COLOR, [ 0, 0, 200, 50 ] )
    current_score = font.render( string + str(player_score), True, color )
    screen.blit( current_score, ( 5, 0 ) )
    
    
def render_objects( snake_positions: List[ tuple ], food_position: tuple ):
    pygame.draw.rect( screen, FOOD_COLOR, [ food_position, ( SEGMENT_SIZE, SEGMENT_SIZE ) ] )
    
    for x, y in snake_positions:
        pygame.draw.rect( screen, SNAKE_COLOR, [ x, y, SEGMENT_SIZE, SEGMENT_SIZE ] )
    
    
def set_new_food_position( snake_positions: List[ tuple ] ):
    while True:
        x_position = randint( 0, 39 ) * SEGMENT_SIZE
        y_position = randint( 2, 41 ) * SEGMENT_SIZE
        food_position = ( x_position, y_position )
        
        if food_position not in snake_positions:
            return food_position


def check_boundary_collision( snake_positions: List[ tuple ] ):
    head_x_position, head_y_position = snake_positions[ 0 ]
    
    # return True if any of the following collision conditions met
    return (
        head_x_position in ( -20, SCREEN_WIDTH )
        or head_y_position in ( 20, SCREEN_HEIGHT )
        or ( head_x_position, head_y_position ) in snake_positions[ 1: ]
    )


def check_food_collision( snake_positions: List[ tuple ], food_position: tuple ):
    if snake_positions[ 0 ] == food_position:
        snake_positions.append( snake_positions[ -1 ] )
        
        return True
    
    
def move_snake( snake_positions: List[ tuple ], direction:str ):
    head_x_position, head_y_position = snake_positions[ 0 ]
    
        
    if direction == "Left":
        new_head_position = ( head_x_position - SEGMENT_SIZE, head_y_position )
    elif direction == "Right":
        new_head_position = ( head_x_position + SEGMENT_SIZE, head_y_position )
    elif direction == "Up":
        new_head_position = ( head_x_position, head_y_position - SEGMENT_SIZE )
    elif direction == "Down":
        new_head_position = ( head_x_position, head_y_position + SEGMENT_SIZE )
        
        
    # Add new head position to front of snake_positions list, then delete the tail since that will now occupy the old 2nd to last position
    snake_positions.insert( 0, new_head_position )
    del snake_positions[ -1 ]


def snake_direction( event:pygame.event, current_direction: str ):
    key = event.__dict__[ "key" ]
    new_direction = KEY_MAP.get( key )
    
    all_directions = ( "Up", "Down", "Left", "Right" )
    opposites = ( { "Up", "Down" }, {"Left", "Right"} )

    # If new_direction is valid and is NOT opposite of current_direction , return new_direction
    if ( new_direction in all_directions 
    and { new_direction, current_direction} not in opposites ):
        return new_direction
    else:
        return current_direction
        

def endScreen( player_score: int ):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                return False
            elif event.type == pygame.KEYDOWN:
                play()
            

        
        screen.fill( BACKGROUND_COLOR )
        
        render_score( player_score, "Final Score: ", SNAKE_COLOR )
        
        play_again = font.render( "Play again? (keypress=y, double-click=n)", True, TEXT_COLOR )
        screen.blit( play_again, ( 5, 200 ) )
        
        pygame.display.update()
                


#* ------------------------------ Main Game Loop ------------------------------ #
def play():
    # Initialize snake game variables
    score = 0

    current_direction = "Right"
    snake_positions = [ ( 100, 100 ) ] # start with 1 piece
    food_position = set_new_food_position( snake_positions )
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                current_direction = snake_direction( event, current_direction )
                
        
        # Render background, snake, food, and score before updating display
        screen.fill( BACKGROUND_COLOR )
        render_objects( snake_positions, food_position )
        render_score( score, "Current Score: ", TEXT_COLOR )
        
        # Update display
        pygame.display.update()
        
        
        # Move snake based on current_direction
        move_snake( snake_positions, current_direction )
                     
                            
        # Check for game boundary collisions, break to endScreen()
        if check_boundary_collision( snake_positions ):
            break
        
        
        # If food acquired, change food_position and add to score
        if check_food_collision( snake_positions, food_position ):
            food_position = set_new_food_position( snake_positions )
            score += 1
            
        
        # Progress game time forward at fps = SNAKE_VELOCITY
        clock.tick( SNAKE_VELOCITY )


    endScreen( score )


#* ---------------------------------------------------------------------------- #
#*                                   RUN GAME                                   #
#* ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    play()