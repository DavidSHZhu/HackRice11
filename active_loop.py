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

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Clicker Prototype')

font = pygame.font.SysFont('Arial', 30)

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

    def draw_button(self):
        pass

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
passiveUpgrade1 = Button(200, 300, "Upgrade exploration (" + str(10) + " RP)", red, 70, 70, green, blue, 10)
passiveupgrade1Pressed = False
activeUpgrade1Pressed = False
activeUpgrade2Pressed = False
passiveupgrade2Pressed = False
passiveUpgrade2Pressed = False


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
    #fill screen
    screen.fill(white)
    #adds title
    screen.blit(font.render(str("Rectangle Clicker"), True, (black)), (200, 50))
    
    #check if button is clicked and what it does
    #what happens when up is clicked
    if up.isClicked():
        counter += count_up_by

    if activeUpgrade1.isClicked() and counter >= 10 :
        count_up_by += 1
        counter -= 10
        activeUpgrade1Pressed = True
        
    if activeUpgrade1Pressed == True:
        activeUpgrade2 = Button(400, 400, "Upgrade Telescope (" + str(20) + " RP)", red, 70, 70, green, blue, 10)
        if activeUpgrade2.isClicked() and counter >= 20:
            count_up_by += 5
            counter -= 20
            activeUpgrade2Pressed = True
    
    if activeUpgrade2Pressed == True:
        activeUpgrade3 = Button(400, 500, "Upgrade Telescope (" + str(50) + " RP)", red, 70, 70, green, blue, 10)
        if activeUpgrade3.isClicked() and counter >= 50:
            count_up_by += 10
            counter -= 50
            activeUpgrade2Pressed = True
    
    if passiveUpgrade1.isClicked() and counter >= 10 :
        passive_income += 1
        counter -= 10
        passiveupgrade1Pressed = True

    if passiveupgrade1Pressed == True:
        passiveUpgrade2 = Button(200, 400, "Upgrade Exploration (" + str(20) + " RP)", red, 70, 70, green, blue, 10)
        if passiveUpgrade2.isClicked() and counter >= 20:
            passive_income += 5
            counter -= 20
            passiveUpgrade2Pressed = True

    if passiveUpgrade2Pressed == True:
        passiveUpgrade3 = Button(200, 500, "Upgrade Exploration (" + str(50) + " RP)", red, 70, 70, green, blue, 10)
        if passiveUpgrade3.isClicked() and counter >= 50:
            passive_income += 10
            counter -= 50

#counter number
    counter_img = font.render(str(counter), True, (100,50,100))
    screen.blit(counter_img, (280, 450))

#main loop DO NOT TOUCH
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False	
    pygame.display.update()

pygame.quit()
