# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:53:32 2020

@author: sushmita singh

"""
import pygame

# initializing all pygame modules
pygame.init()

# creating window
screen = pygame.display.set_mode((800, 700))

# inserting logo image
logo = pygame.image.load("image\logo.png")
pygame.display.set_icon(logo)

# Changing the tittle of the window
pygame.display.set_caption("SPACE INVADER @BY SUSHMITA SINGH")

# SPACESHIP for player
player = pygame.image.load("image/spaceship.png")
playerx = 360
playery = 600
playerx_change = 0
playery_change = 0


# function for player image
def playerImg(x, y):
    screen.blit(player, (x, y))


run = True
# game loop
while run:
    for event in pygame.event.get():  # it will call all events of pyagme
        # quit the program.
        if event.type == pygame.QUIT:  # IT WIL ENABLLE CLOSE BUTTON TO CLOSE THE WINDOW
            run = False

        # checking wheather the key is pressed
        if event.type == pygame.KEYDOWN:

            # movement of player  on pressing left arrow key
            if event.key == pygame.K_LEFT:
                playerx_change = -0.3

            # movement of player  on pressing right arrow key
            if event.key == pygame.K_RIGHT:
                playerx_change = 0.3

        # checking wheather the key is RELEASED
        if event.type == pygame.KEYUP:
            # stop the player if key is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

    # fill color to the surface of window
    screen.fill((60, 60, 110))  # CHANGING THE COLOR OF WINDOW

    # for the movement of player space ship ; changing the x co-ordinates
    playerx += playerx_change

    # setting boundaries:
    # when spaceship will touch the left boundary is will stop
    if playerx <= 0:
        playerx = 0

    # when spaceship will touch the right boundary is will stop
    if playerx >= 740:
        playerx = 740

    playerImg(playerx, playery)  # calling playerimage function

    # updating the changes in the window
    # Draws the surface object to the screen.
    pygame.display.update()
