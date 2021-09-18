import pygame
from pygame.locals import *
pygame.init()

screen_width = 1500
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Button Demo')

clicked = False
counter = 0

font = pygame.font.SysFont('Arial', 50)
screen.blit(font.render('Rectangle Clicker!', True, (0,0,0)), (50, 20))

class Button():

	button_col = (255, 0, 0)
	height = (70)
	width = (50)

	def __init__(self, x, y, text):
		self.x = x
		self.y = y
		self.text = text
	
	def isClicked(self):
		global clicked
		action = False
		button_rect = Rect(self.x, self.y, self.width, self.height)

		pos = pygame.mouse.get_pos()
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
				pygame.draw.rect(screen, (255,0,0), button_rect)
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True
		else:
			pygame.draw.rect(screen, self.button_col, button_rect)

		text_img = font.render(self.text, True, (100,50,100))
		text_len = text_img.get_width()
		screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
		return action

up = Button(325, 350, 'Up')

run = True
while run:

	screen.fill((0,0,0))

	if up.isClicked():
		print('Up')
		counter += 1
	counter_img = font.render(str(counter), True, (100,50,100))

	screen.blit(counter_img, (280, 450))


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False	


	pygame.display.update()

