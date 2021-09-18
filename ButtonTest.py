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

    def __init__(self, x, y, width, height, text, button_col, clicked_col, hover_col):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.button_col = button_col
        self.clicked_col = clicked_col
        self.hover_col = hover_col
        self.button_rect = Rect(self.x, self.y, self.width, self.height)

	
    def isClicked(self):
        global clicked
        action = False
        
        pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(pos):
            self.drawButton(hover_col)
            # pygame.draw.rect(screen, self.hover_col, button_rect)
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                self.drawButton(clicked_col)
                pygame.draw.rect(screen, self.clicked_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
        else:
            pygame.draw.rect(screen, self.button_col, self.button_rect)

        text_img = font.render(self.text, True, (100,50,100))
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action

    def drawButton(self, color):
        global clicked
        pygame.draw.rect(screen, color, self.button_rect)

button_col = (255, 0, 0)
clicked_col = (50, 50, 255)
hover_col = (100, 100, 250)
getPoints = Button(250, 350, 350, 100, 'Click Me!', button_col, clicked_col, hover_col)

telescopeLevel = 1
upgradeTelescope = Button(250, 550, 250, 100, 'Upgrade Telescope', button_col, clicked_col, hover_col)

run = True
while run:

    screen.fill((255, 255, 255))

    if getPoints.isClicked():
        print('Got a point!')
        counter += telescopeLevel
    counter_img = font.render(str(counter), True, (100,50,100))

    screen.blit(counter_img, (280, 450))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False	


    pygame.display.update()

