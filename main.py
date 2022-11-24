import pygame

from pygame import Color, Rect
from pygame import draw
from pygame import display

SCREEN_SIZE = (500, 500)

# initialize pygame modules
pygame.init()

# get a surface for graphics display
gameDisplay = display.set_mode(SCREEN_SIZE)

# background
gameDisplay.fill(Color('blue'))

# Fish
draw.polygon(gameDisplay, Color('silver'), ((250,199),(250,300),(325,275),(375,300),(375,199),(325,225)))
draw.circle(gameDisplay, Color('silver'), (250, 250), 50)
draw.line(gameDisplay, Color('black'), (230,250),(230,225),3)

# Bubbles
draw.circle(gameDisplay, Color('darkblue'), (75,450), 40)
draw.circle(gameDisplay, Color('blue'), (75,450), 37)
draw.circle(gameDisplay, Color('darkblue'), (130,400), 30)
draw.circle(gameDisplay, Color('blue'), (130,400), 27)
draw.circle(gameDisplay, Color('darkblue'), (93,362), 20)
draw.circle(gameDisplay, Color('blue'), (93,362), 17)

# show the graphics on the screen
display.flip()

# Wait for user input before closing the window
input("Press enter to exit")