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
light_red = (255, 127, 127)
blue = (0,0,255)
green = (0,255,0)
brown = (100,40,0)
light_brown = (196, 164, 132)
light_blue = (173,216,230)
grey = (50,50,50)
light_purple = (137,93,172)
purple = (128,0,128)
med_purple = (177,119,222)
light_grey = (128,128,128)
dark_red = (139, 0, 0)

WIDTH = 900
HEIGHT = 600

GRASSY_FIELD = pygame.image.load("/Users/jonathan/Documents/git/HackRice11/GrassyField.png")
PLANET_EARTH = pygame.image.load("/Users/jonathan/Documents/git/HackRice11/PlanetEarth.png")
EARTH_MOON = pygame.image.load("/Users/jonathan/Documents/git/HackRice11/EarthMoon.png")
SOLAR_SYSTEM = pygame.image.load("/Users/jonathan/Documents/git/HackRice11/SolarSystem.png")
GALAXY_VIEW = pygame.image.load("/Users/jonathan/Documents/git/HackRice11/GalaxyView.png")
VICTORY_SCREEN = pygame.image.load("/Users/jonathan/Documents/git/HackRice11/GalaxyView.png")
BEAKER = pygame.image.load("/Users/jonathan/Documents/git/HackRice11/beaker.png")

GRASSY_FIELD = pygame.transform.smoothscale(GRASSY_FIELD, (WIDTH, HEIGHT))
PLANET_EARTH = pygame.transform.smoothscale(PLANET_EARTH, (WIDTH, HEIGHT))
EARTH_MOON = pygame.transform.smoothscale(EARTH_MOON, (WIDTH, HEIGHT))
SOLAR_SYSTEM = pygame.transform.smoothscale(SOLAR_SYSTEM, (WIDTH, HEIGHT))
GALAXY_VIEW = pygame.transform.smoothscale(GALAXY_VIEW, (WIDTH, HEIGHT))
VICTORY_SCREEN = pygame.transform.smoothscale(VICTORY_SCREEN, (WIDTH, HEIGHT))
BEAKER = pygame.transform.scale(BEAKER, (40, 56))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
# CHANGE THE GAME NAME DO NOT FORGET
# DO NOT FORGET TO DO THIS
# DO NOT FORGET TO DO THIS
# DO NOT FORGET TO DO THIS
pygame.display.set_caption('GAME NAME')

font = pygame.font.SysFont('Arial', 30)

SCENES = [GRASSY_FIELD, PLANET_EARTH, EARTH_MOON, SOLAR_SYSTEM, GALAXY_VIEW, VICTORY_SCREEN, BEAKER]
# Once you have accrued 100,000 you achieve victory and can choose to play again.
CUTOFF_VALUES = [0, 100, 500, 2500, 15000, 50000,1000000000]
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


up = Button(50, 305, 'Click me!', red, 50, 100, dark_red, light_red, 20)
#Upgrade Telescope (10 RP)
activeUpgrade1 = Button(705, 120, "10 RP", light_purple, 70, 70, purple, med_purple, 15)
#Upgrade Lunar Rovers (100 RP)
passiveUpgrade1 = Button(791, 120, "100 RP", light_purple, 70, 70, purple, med_purple, 15)
close_journal =  Button(12, 452, "", grey, 20, 20, black, light_grey, 10)
ActivePressed = [False, False]
PassivePressed = [False, False]
journal_flag = 0

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
        screen.blit(VICTORY_SCREEN, (0, 0))
        break
    #fill screen
    screen.blit(SCENES[progression_index], (0, 0))
    #adds background
    #draws upgrade screen
    pygame.draw.rect(screen, (blue), pygame.Rect(685, 25, 200, 400))
    pygame.draw.rect(screen, (light_blue), pygame.Rect(690, 30, 190, 390))
    upgrade_text1 = font.render("Upgrade Tools", True, (black))
    screen.blit(upgrade_text1, (705, 35))
    pygame.draw.line(screen, black, (695, 75), (870, 75))
    pygame.draw.line(screen, black, (783, 75), (783, 400))
    upgrade_text2 = (pygame.font.SysFont('Arial', 15)).render("Observational", True, (black))
    screen.blit(upgrade_text2, (700, 80))
    upgrade_text3 = (pygame.font.SysFont('Arial', 15)).render("Explorational", True, (black))
    screen.blit(upgrade_text3, (790, 80))
    #draws research point screen
    pygame.draw.rect(screen, (black), pygame.Rect(5, 360, 200, 70))
    pygame.draw.rect(screen, (white), pygame.Rect(10, 365, 190, 60))
    screen.blit(BEAKER, (100, 367))


    #check if button is clicked and what it does
    #what happens when up is clicked
    
    if close_journal.isClicked():
        journal_flag += 1
    if journal_flag % 2 == 0:
        pygame.draw.rect(screen, (brown), pygame.Rect(5, 445, 885, 150))
        pygame.draw.rect(screen, (light_brown), pygame.Rect(10, 450, 875, 140))
        close_journal.isClicked()
                

    if up.isClicked():
        counter += count_up_by

    if activeUpgrade1.isClicked() and counter >= 10 :
        count_up_by += 1
        counter -= 10
        ActivePressed[0] = True
        
    if ActivePressed[0] == True:
        activeUpgrade2 = Button(705, 210, "5000 RP", light_purple, 70, 70, purple, med_purple, 15)
        if activeUpgrade2.isClicked() and counter >= 5000:
            count_up_by += 60
            counter -= 5000
            ActivePressed[1] = True
    
    if ActivePressed[1] == True:
        activeUpgrade3 = Button(705, 300, "20000 RP", light_purple, 70, 70, purple, med_purple, 15)
        if activeUpgrade3.isClicked() and counter >= 20000:
            count_up_by += 250
            counter -= 20000
            activeUpgrade2Pressed = True
    
    if passiveUpgrade1.isClicked() and counter >= 100 :
        passive_income += 1
        counter -= 100
        PassivePressed[0] = True

    if PassivePressed[0] == True:
        passiveUpgrade2 = Button(791, 210, "2000 RP)", light_purple, 70, 70, purple, med_purple, 15)
        if passiveUpgrade2.isClicked() and counter >= 2000:
            passive_income += 25
            counter -= 2000
            PassivePressed[1] = True

    if PassivePressed[1] == True:
        passiveUpgrade3 = Button(791, 300, "Upgrade Lunar Base (30000 RP)", light_purple, 70, 70, purple, med_purple, 15)
        if passiveUpgrade3.isClicked() and counter >= 300000:
            passive_income += 400
            counter -= 30000

#text
    #research lab
    if journal_flag % 2 == 0 and 50 <= counter < 100:
        line1 = (pygame.font.SysFont('Arial', 25)).render("research lab - You’ve discovered the research lab! This is where cool scientists like you do ", True, (black))
        screen.blit(line1, (15, 465))
        line2 = (pygame.font.SysFont('Arial', 25)).render("experiments to learn more about the earth and the universe. You have a selection of tools that", True, (black))
        screen.blit(line2, (15, 490))
        line3 = (pygame.font.SysFont('Arial', 25)).render("help you see and understand the bodies of the universe, discover new stars, and work with ", True, (black))
        screen.blit(line3, (15, 520))
        line4 = (pygame.font.SysFont('Arial', 25)).render("Professor JMak", True, (black))
        screen.blit(line4, (15, 550))
    #earth
    if journal_flag % 2 == 0 and 100 <= counter < 250:
        line1 = (pygame.font.SysFont('Arial', 25)).render("You’ve discovered that our home planet is called the Earth! Earth revolves around the Sun once", True, (black))
        screen.blit(line1, (15, 465))
        line2 = (pygame.font.SysFont('Arial', 25)).render("every 365.25 days – this is known as one Earth year. Earth is very special because it is the", True, (black))
        screen.blit(line2, (15, 490))
        line3 = (pygame.font.SysFont('Arial', 25)).render("only planet we know of right now that we can live on!", True, (black))
        screen.blit(line3, (15, 520))
    #asteriod
    if journal_flag % 2 == 0 and 250 <= counter < 500:
        line1 = (pygame.font.SysFont('Arial', 25)).render("You’ve discovered asteroids! Asteroids have valuable metals in them as well as water. There are", True, (black))
        screen.blit(line1, (15, 465))
        line2 = (pygame.font.SysFont('Arial', 25)).render("millions of asteroids. Sometimes asteroids hit Earth and other planets, one of which made the", True, (black))
        screen.blit(line2, (15, 490))
        line3 = (pygame.font.SysFont('Arial', 25)).render("dinosaurs go extinct! Most asteroids are in a “belt” between Earth and Mars.", True, (black))
        screen.blit(line3, (15, 520))
    #moon    
    if journal_flag % 2 == 0 and 500 <= counter < 2500:
        line1 = (pygame.font.SysFont('Arial', 25)).render("You’ve discovered the moon! The moon orbits around Earth. The moon has different “phases”. When", True, (black))
        screen.blit(line1, (15, 465))
        line2 = (pygame.font.SysFont('Arial', 25)).render("the Sun and Moon line up on the same side of the Earth, the Moon is “new” and looks like it", True, (black))
        screen.blit(line2, (15, 490))
        line3 = (pygame.font.SysFont('Arial', 25)).render("isn’t there. As the moon rotates, we can see more and more of the moon (waxing) until it reaches", True, (black))
        screen.blit(line3, (15, 520))
        line4 = (pygame.font.SysFont('Arial', 25)).render("the “full moon” phase and what we can see starts shrinking again (waning).", True, (black))
        screen.blit(line4, (15, 550))
    #mars    
    if journal_flag % 2 == 0 and 2500 <= counter < 4000:
        line1 = (pygame.font.SysFont('Arial', 25)).render("You’ve discovered Mars, the fourth planet from the Sun! The tallest volcano in the Solar System ", True, (black))
        screen.blit(line1, (15, 465))
        line2 = (pygame.font.SysFont('Arial', 25)).render("is located on Mars. It is 3 times taller than Mt. Everest!  Mars was named after the Roman god", True, (black))
        screen.blit(line2, (15, 490))
        line3 = (pygame.font.SysFont('Arial', 25)).render("of war because of its red color, but the planet is very cold. It has ice at its north pole.", True, (black))
        screen.blit(line3, (15, 520))
    #venus    
    if journal_flag % 2 == 0 and 4000 <= counter < 5000:
        line1 = (pygame.font.SysFont('Arial', 25)).render("You’ve discovered Venus, the second planet from the Sun! Venus is named after the ancient", True, (black))
        screen.blit(line1, (15, 465))
        line2 = (pygame.font.SysFont('Arial', 25)).render("Roman goddess of love and beauty because it is the second brightest object in the sky after the", True, (black))
        screen.blit(line2, (15, 490))
        line3 = (pygame.font.SysFont('Arial', 25)).render("Moon. Although Mercury is closer to the Sun, Venus is the hottest planet in the Solar System.", True, (black))
        screen.blit(line3, (15, 520))    
    #mercury
    if journal_flag % 2 == 0 and 5000 <= counter < 7500:
        line1 = (pygame.font.SysFont('Arial', 25)).render("You’ve discovered Mercury! Mercury is the closest planet to the Sun, but it’s also the smallest ", True, (black))
        screen.blit(line1, (15, 465))
        line2 = (pygame.font.SysFont('Arial', 25)).render("planet. During Mercury’s day time, it is very hot, but at night it gets extremely cold!", True, (black))
        screen.blit(line2, (15, 490))
    #jupiter 
    if journal_flag % 2 == 0 and 7500 <= counter < 10000:
        line1 = (pygame.font.SysFont('Arial', 25)).render("You’ve discovered Jupiter, the fifth planet from the Sun! It is the largest planet in our solar", True, (black))
        screen.blit(line1, (15, 465))
        line2 = (pygame.font.SysFont('Arial', 25)).render("system and is named after the king of the Roman gods. Jupiter is over twice the mass of every", True, (black))
        screen.blit(line2, (15, 490))
        line3 = (pygame.font.SysFont('Arial', 25)).render("other planet added together. It has a storm larger than Earth called the Great Red Spot.", True, (black))
        screen.blit(line3, (15, 520)) 
    #saturn     
    if journal_flag % 2 == 0 and 10000 <= counter < 12500:
        line1 = (pygame.font.SysFont('Arial', 25)).render("You’ve discovered Saturn, the sixth planet from the Sun! It has beautiful rings made of ice and ", True, (black))
        screen.blit(line1, (15, 465))
        line2 = (pygame.font.SysFont('Arial', 25)).render("dust. Saturn doesn’t have a solid surface -- it is made of swirling gases and liquids, so it", True, (black))
        screen.blit(line2, (15, 490))
        line3 = (pygame.font.SysFont('Arial', 25)).render("would float in water. It is suspected to have helped fling Uranus and Neptune into their extremely", True, (black))
        screen.blit(line3, (15, 520))
        line4 = (pygame.font.SysFont('Arial', 25)).render("far orbits.", True, (black))
        screen.blit(line4, (15, 550))  
    #uranaus     
    if journal_flag % 2 == 0 and 12500 <= counter < 14000:
        line1 = (pygame.font.SysFont('Arial', 25)).render("You’ve discovered Uranus, the seventh planet from the Sun! It is the coldest planet in our solar", True, (black))
        screen.blit(line1, (15, 465))
        line2 = (pygame.font.SysFont('Arial', 25)).render("system. It also orbits the Sun on its side so that one side is in constant light and the other", True, (black))
        screen.blit(line2, (15, 490))
        line3 = (pygame.font.SysFont('Arial', 25)).render("side is in constant darkness. It also has a storm called the Great Dark Spot, which is so large", True, (black))
        screen.blit(line3, (15, 520))
        line4 = (pygame.font.SysFont('Arial', 25)).render("that it would cover ⅔ of the United States!.", True, (black))
        screen.blit(line4, (15, 550))
        #neptune
    if journal_flag % 2 == 0 and 14000 <= counter < 15000:
        line1 = (pygame.font.SysFont('Arial', 25)).render("You’ve discovered Neptune, the farthest planet from the Sun! It is named after the Roman god of", True, (black))
        screen.blit(line1, (15, 465))
        line2 = (pygame.font.SysFont('Arial', 25)).render("the seas because of this planet’s beautiful, blue color. It has the strongest winds in the Solar ", True, (black))
        screen.blit(line2, (15, 490))
        line3 = (pygame.font.SysFont('Arial', 25)).render("System, reaching up to 2100 km / hr. It takes 169 Earth years for Neptune to orbit the Sun.", True, (black))
        screen.blit(line3, (15, 520))
    #constellations     
    if journal_flag % 2 == 0 and 15000 <= counter < 25000:
        line1 = (pygame.font.SysFont('Arial', 25)).render("You’ve discovered constellations! A constellation is a group of stars that form a perceived outline", True, (black))
        screen.blit(line1, (15, 465))
        line2 = (pygame.font.SysFont('Arial', 25)).render("or pattern. Since each star does not stay still in the sky, all constellations will change slowly", True, (black))
        screen.blit(line2, (15, 490))
        line3 = (pygame.font.SysFont('Arial', 25)).render("over time. After tens to hundreds of thousands of years, the constellations we see today will ", True, (black))
        screen.blit(line3, (15, 520))
        line4 = (pygame.font.SysFont('Arial', 25)).render("become unrecognizable.", True, (black))
        screen.blit(line4, (15, 550))    
    #big dipper     
    if journal_flag % 2 == 0 and 25000 <= counter < 35000:
        line1 = (pygame.font.SysFont('Arial', 25)).render("You’ve discovered The Big Dipper! The Big Dipper got its name because its seven brightest stars", True, (black))
        screen.blit(line1, (15, 465))
        line2 = (pygame.font.SysFont('Arial', 25)).render("seem to form the shape of something travelers would “dip” in the river to get water. It is part", True, (black))
        screen.blit(line2, (15, 490))
        line3 = (pygame.font.SysFont('Arial', 25)).render(" of the constellation Ursa Major, which is Latin for “Great Bear.", True, (black))
        screen.blit(line3, (15, 520))
    #little dipper     
    if journal_flag % 2 == 0 and 35000 <= counter < 50000:
        line1 = (pygame.font.SysFont('Arial', 25)).render("You’ve discovered The Little Dipper! Like The Big Dipper, The Little Dipper also has seven stars,", True, (black))
        screen.blit(line1, (15, 465))
        line2 = (pygame.font.SysFont('Arial', 25)).render("with four in its bowl. The best time to see the Little Dipper is in June. The North Star is the", True, (black))
        screen.blit(line2, (15, 490))
        line3 = (pygame.font.SysFont('Arial', 25)).render("brightest star of the Little Dipper. The North Star always appears in the same place in the sky. It", True, (black))
        screen.blit(line3, (15, 520))
        line4 = (pygame.font.SysFont('Arial', 25)).render("always points North!", True, (black))
        screen.blit(line4, (15, 550))    
#counter number
    counter_img = font.render(str(counter), True, (black))
    screen.blit(counter_img, (15, 375))
    counter_img = font.render("RP", True, (black))
    screen.blit(counter_img, (140, 375))


#main loop DO NOT TOUCH
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False	
    pygame.display.update()


if run == False:
    pygame.quit()
