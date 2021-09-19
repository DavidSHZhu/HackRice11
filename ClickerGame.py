"""
TODO:
add logic to when victory screen appears (aka when progression_index == len(CUTOFF_VALUES) - 1)
    -delete buttons
    -add a quit button

fix button positioning / colors, etc.
add informative popups.
add comments to code
THINK OF NAME FOR GAME.
"""

import pygame
from pygame.locals import *
import sys
pygame.init()

#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

WIDTH = 900
HEIGHT = 600

GRASSY_FIELD = pygame.image.load("/Users/davidzhu/Documents/Rice University/HackRice11/GrassyField.png")
PLANET_EARTH = pygame.image.load("/Users/davidzhu/Documents/Rice University/HackRice11/PlanetEarth.png")
EARTH_MOON = pygame.image.load("/Users/davidzhu/Documents/Rice University/HackRice11/EarthMoon.png")
SOLAR_SYSTEM = pygame.image.load("/Users/davidzhu/Documents/Rice University/HackRice11/SolarSystem.png")
GALAXY_VIEW = pygame.image.load("/Users/davidzhu/Documents/Rice University/HackRice11/GalaxyView.png")
VICTORY_SCREEN = pygame.image.load("/Users/davidzhu/Documents/Rice University/HackRice11/GalaxyView.png")

GRASSY_FIELD = pygame.transform.smoothscale(GRASSY_FIELD, (WIDTH, HEIGHT))
PLANET_EARTH = pygame.transform.smoothscale(PLANET_EARTH, (WIDTH, HEIGHT))
EARTH_MOON = pygame.transform.smoothscale(EARTH_MOON, (WIDTH, HEIGHT))
SOLAR_SYSTEM = pygame.transform.smoothscale(SOLAR_SYSTEM, (WIDTH, HEIGHT))
GALAXY_VIEW = pygame.transform.smoothscale(GALAXY_VIEW, (WIDTH, HEIGHT))
VICTORY_SCREEN = pygame.transform.smoothscale(VICTORY_SCREEN, (WIDTH, HEIGHT))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
# CHANGE THE GAME NAME DO NOT FORGET
# DO NOT FORGET TO DO THIS
# DO NOT FORGET TO DO THIS
# DO NOT FORGET TO DO THIS
pygame.display.set_caption('GAME NAME')

font = pygame.font.SysFont('Arial', 30)

SCENES = [GRASSY_FIELD, PLANET_EARTH, EARTH_MOON, SOLAR_SYSTEM, GALAXY_VIEW]
# Once you have accrued 100,000 you achieve victory and can choose to play again.
CUTOFF_VALUES = [0, 100, 500, 2500, 15000, 50000]
progression_index = 0

clicked = False
counter = 0
count_up_by = 1

class Button():

    def __init__(self, x, y, text, button_col, height, width, clicked_col, hover_col, font):
        self.text = text
        self.x = x
        self.y = y
        self.button_col = button_col
        self.height = height
        self.width = width
        self.clicked_col = clicked_col
        self.hover_col = hover_col
        self.button_rect = Rect(self.x, self.y, self.width, self.height)
        self.font = font = pygame.font.SysFont('Arial', font)

    #finds out if button is clicked
    def isClicked(self):
        global clicked
        action = False

        pos = pygame.mouse.get_pos()

        if self.button_rect.collidepoint(pos):
            self.drawButton(self.hover_col)
            # pygame.draw.rect(screen, self.hover_col, button_rect)
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                self.drawButton(self.clicked_col)
                pygame.draw.rect(screen, self.clicked_col, self.button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
        else:
            pygame.draw.rect(screen, self.button_col, self.button_rect)

#centers text onto button
        text_img = self.font.render(self.text, True, (black))
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 15))
        return action
            
    def drawButton(self, color):
        global clicked
        pygame.draw.rect(screen, color, self.button_rect)

#Buttons
up = Button(275, 200, '', red, 70, 70, green, blue, 10)
activeUpgrade1 = Button(400, 300, "Upgrade Telescope (" + str(10) + " RP)", red, 70, 70, green, blue, 10)
passiveUpgrade1 = Button(200, 300, "Upgrade Lunar Rovers (" + str(100) + " RP)", red, 70, 70, green, blue, 10)
ActivePressed = [False, False]
PassivePressed = [False, False]


#main run function
passive_income = 0
run = True
FPS = 60
clock = pygame.time.Clock()
time_counter = 0
while run:
    clock.tick(FPS)
    time_counter += 1
    time_counter %= 60
    if time_counter == 0:
        counter += passive_income
    if counter > CUTOFF_VALUES[progression_index + 1]:
        progression_index += 1
    if progression_index == len(CUTOFF_VALUES) - 1:
        screen.blit(VICTORY_SCREEN, (0, 0)) # TODO
    #fill screen
    screen.blit(SCENES[progression_index], (0, 0))
    #adds title
    screen.blit(font.render(str("Rectangle Clicker"), True, (black)), (200, 50))
    
    #check if button is clicked and what it does
    #what happens when up is clicked
    if up.isClicked():
        counter += count_up_by

    if activeUpgrade1.isClicked() and counter >= 10 :
        count_up_by += 1
        counter -= 10
        ActivePressed[0] = True
        
    if ActivePressed[0] == True:
        activeUpgrade2 = Button(400, 400, "Upgrade Space Elevator (" + str(5000) + " RP)", red, 70, 70, green, blue, 10)
        if activeUpgrade2.isClicked() and counter >= 5000:
            count_up_by += 60
            counter -= 5000
            ActivePressed[1] = True
    
    if ActivePressed[1] == True:
        activeUpgrade3 = Button(400, 500, "Upgrade Deep Space Probes (" + str(20000) + " RP)", red, 70, 70, green, blue, 10)
        if activeUpgrade3.isClicked() and counter >= 20000:
            count_up_by += 250
            counter -= 20000
            activeUpgrade2Pressed = True
    
    if passiveUpgrade1.isClicked() and counter >= 100 :
        passive_income += 1
        counter -= 100
        PassivePressed[0] = True

    if PassivePressed[0] == True:
        passiveUpgrade2 = Button(200, 400, "Upgrade Satellites (" + str(2000) + " RP)", red, 70, 70, green, blue, 10)
        if passiveUpgrade2.isClicked() and counter >= 2000:
            passive_income += 25
            counter -= 2000
            PassivePressed[1] = True

    if PassivePressed[1] == True:
        passiveUpgrade3 = Button(200, 500, "Upgrade Lunar Base (" + str(30000) + " RP)", red, 70, 70, green, blue, 10)
        if passiveUpgrade3.isClicked() and counter >= 300000:
            passive_income += 400
            counter -= 30000

#counter number
    counter_img = font.render(str(counter), True, (100,50,100))
    screen.blit(counter_img, (280, 450))

#main loop DO NOT TOUCH
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False	
    pygame.display.update()

pygame.quit()
