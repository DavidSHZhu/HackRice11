import pygame
from pygame.locals import *
import sys
pygame.init()

#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Clicker Prototype')

font = pygame.font.SysFont('Arial', 30)

clicked = False
counter = 0
count_up_by = 1

class Button():

	def __init__(self, x, y, text, button_col, height, width):
		self.x = x
		self.y = y
		self.button_col = button_col
		self.text = text
		self.height = height
		self.width = width
	
    #finds out if button is clicked
	def isClicked(self):
		global clicked
		action = False
		button_rect = Rect(self.x, self.y, self.width, self.height)

		pos = pygame.mouse.get_pos()
        
        #draws button
		pygame.draw.rect(screen, self.button_col, button_rect)

        #checks if button is clciked
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True

        #centers text onto button
		text_img = font.render(self.text, True, (black))
		text_len = text_img.get_width()
		screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 15))
		return action

#Buttons
up = Button(275, 200, '', red, 70, 70)

#main run function
run = True
while run:
    #fill screen
    screen.fill(white)
    #adds title
    screen.blit(font.render(str("Rectangle Clicker"), True, (black)), (200, 50))
    
    #check if button is clicked and what it does
    #what happens when up is clicked
    if up.isClicked():
    	counter += count_up_by
    counter_img = font.render(str(counter), True, (100,50,100))
    screen.blit(counter_img, (280, 450))



    #main loop DO NOT TOUCH
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False	
    pygame.display.update()

pygame.quit()