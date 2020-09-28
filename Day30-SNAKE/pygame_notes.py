
#* --------------- Creating a pygame window (application window) -------------- #

import pygame

pygame.init()

pygame.display.set_caption( "My game!" )

screen = pygame.display.set_mode( [ 640, 480 ] ) # defines the size of our application window


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            
# main() # Call to start the game screen (Surface object)


#* ------------------------------ Drawing Basics ------------------------------ #

# set_mode() returns a "Surface" object which are used by pygame to represent an image. They're also surfaces we can draw onto, and we have several methods at our disposal for handling this kind of operation

## Fill method:
    # Allows us to fill an area of a surface with some color 
from collections import namedtuple

Color = namedtuple( "Color", [ "red", "green", "blue" ] )

BACKGROUND_COLOR = Color( red=36, green=188, blue=168 )

screen.fill( BACKGROUND_COLOR )

pygame.display.update()


## Draw module:
    # Can draw simple shapes onto a surface
    
RECTANGLE_COLOR = Color( red=255, green=255, blue=255 )
CIRCLE_COLOR = Color( red=255, green=253, blue=65 )

pygame.draw.rect( screen, RECTANGLE_COLOR, [ 0, 0, 100, 50 ] )
pygame.draw.circle( screen, CIRCLE_COLOR, [ int( screen.get_width() / 2 ), int( screen.get_height() / 2 ) ], 40 ) # will always be in the middle of the screen independent of window size

pygame.display.update()


## Drawing text:

# 1.) Create a font object
font = pygame.font.Font( None, 28 )
text = font.render( "Woo! This is some text!", True, ( 0, 0, 0 ) )
screen.blit( text, ( 50, 50 ) )

pygame.display.update()


#* ------------------------------- Moving Items ------------------------------- #

## Moving items on the screen is a matter of repeatedly drawing items to the screen in different positions and covering up the old content.
    # In our case, that means filling the screen with the background color, drawing new shapes, and using the update() function for the screen
    
from collections import namedtuple

Colour = namedtuple("Colour", ["red", "green", "blue"])

BACKGROUND_COLOUR = Colour(red=36, green=188, blue=168)
CIRCLE_COLOUR = Colour(red=255, green=253, blue=65)

pygame.init()

pygame.display.set_caption("My game!")

clock = pygame.time.Clock()
screen = pygame.display.set_mode([640, 480])


def main():
    circle_position = [320, 240]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(BACKGROUND_COLOUR)
        pygame.draw.circle(screen, CIRCLE_COLOUR, circle_position, 40)
        pygame.display.update()

        circle_position[0] += 5

        clock.tick(60)



#* ---------------------------------- Events ---------------------------------- #

## Events are how pygame communicates that something has happened in the application. This might be something like the user moving their mouse, pressing a key, or clicking to close the application

    # Let's create a new application where we just print out the position of the mouse to the console. We can find the position of the mouse from a pygame.MOUSEMOTION event by accessing an attribute on the event called __dict__.

    # This gives us a dictionary with a key called "pos" which contains coordinates for the mouse position when that event was triggered.


pygame.init()

pygame.display.set_caption("Mousetracker")
screen = pygame.display.set_mode([640, 480])


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEMOTION:
	            position = event.__dict__["pos"]
	            print(position)





Colour = namedtuple("Colour", ["red", "green", "blue"])

BACKGROUND_COLOUR = Colour(red=36, green=188, blue=168)
CIRCLE_COLOUR = Colour(red=255, green=253, blue=65)

pygame.init()

pygame.display.set_caption("Mousetracker")

clock = pygame.time.Clock()
screen = pygame.display.set_mode([640, 480])


def main():
    circle_position = (screen.get_width() // 2), (screen.get_height() // 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return # NOTE: None, meaning while True fails, main ends
            elif event.type == pygame.MOUSEMOTION:
                circle_position = event.__dict__["pos"] # follows the mouse motion


        screen.fill(BACKGROUND_COLOUR)
        pygame.draw.circle(screen, CIRCLE_COLOUR, circle_position, 20)
        pygame.display.update()

        clock.tick(60)



#* ------------------------------ A bouncing ball ----------------------------- #

## We need to keep track of the ball's velocity, describing how far the ball will move in a given direction for each tick of our clock. We will start by randomizing the starting values for the velocity

from pygame import *
from random import randint

Colour = namedtuple("Colour", ["red", "green", "blue"])

BACKGROUND_COLOUR = Colour(red=36, green=188, blue=168)
BALL_COLOUR = Colour(red=255, green=253, blue=65)

BALL_RADIUS = 20

pygame.init()

pygame.display.set_caption("Bouncing Ball")

clock = pygame.time.Clock()
screen = pygame.display.set_mode([640, 480])


def main():
    ball_position = [(screen.get_width() // 2), (screen.get_height() // 2)]
    ball_velocity = [randint(-5, 5), randint(-5, 5)]
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(BACKGROUND_COLOUR)
        pygame.draw.circle(screen, BALL_COLOUR, ball_position, BALL_RADIUS)
        pygame.display.update()
        
        # Check for left and right collisions
        if ball_position[ 0 ] - BALL_RADIUS < 0:
            ball_velocity[ 0 ] = -ball_velocity[ 0 ]
        elif ball_position[ 0 ] + BALL_RADIUS > screen.get_width():
            ball_velocity = - ball_velocity[ 0 ]

        # Check for top and bottom collisions
        if ball_position[ 1 ] - BALL_RADIUS < 0:
            ball_velocity[ 1 ] = -ball_velocity[ 1 ]
        elif ball_position[ 1 ] + BALL_RADIUS > screen.get_height():
            ball_velocity[ 1 ] = -ball_velocity[ 1 ]
            
        
        ball_position[ 0 ] += ball_velocity[ 0 ]
        ball_position[ 1 ] += ball_velocity[ 1 ]
        
        clock.tick(60)

pygame.display.update()

main()