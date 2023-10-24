#Name:
#Date:
#Basic PyGame Setup Code
import pygame,sys,time
from player import Player
from backround import backround
from buttons import imagebutton
from static import stillimage
from text import customtext


pygame.init()
def exit():
    pygame.quit()
    sys.exit()
def next():
    global done
    done=True
def health():
    global healthbar
    healthbar="images/healthbar.png"
    
def gridHelp(window,WINDOW_WIDTH,WINDOW_HEIGHT):
        spacer = 10
        font = pygame.font.SysFont('Consolas', 10)
        for gridX in range(0, WINDOW_WIDTH, spacer):        
            window.blit(pygame.transform.rotate(font.render(str(gridX), True, (255, 255, 255)),90),(gridX,0))
        for gridY in range(0, WINDOW_HEIGHT, spacer):
            window.blit(font.render(str(gridY), True, (255, 255, 255)), (0, gridY))
        for gridX in range(0, WINDOW_WIDTH, spacer):
            pygame.draw.line(window,(255,0,0),(gridX,0),(gridX,WINDOW_HEIGHT))
        for gridY in range(0, WINDOW_HEIGHT, spacer):
            pygame.draw.line(window,(255,0,0),(0,gridY),(WINDOW_WIDTH,gridY)) 
fps = 30
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 800
player_group = pygame.sprite.Group()
space_group = pygame.sprite.Group()
collision_group = pygame.sprite.Group()
start_group = pygame.sprite.Group()
starttext_group = pygame.sprite.Group()
start_btn= pygame.sprite.Group()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
billy=Player(350,600,125,75,"images/billy.png",10)
player_group.add(billy)
spaceback=backround(WINDOW_WIDTH,WINDOW_HEIGHT,"images/spacers.jpg")
space_group.add(spaceback)
btn_ext= imagebutton(225,200,250,250,"images/play.png","images/playclicked.png",next)
start_btn.add(btn_ext)
startback=backround(WINDOW_WIDTH,WINDOW_HEIGHT,"images/startback.jpg")
start_group.add(startback)
title= stillimage(125,0,500,250,"images/title.png")
start_group.add(title)
collidewalls=backround(WINDOW_WIDTH,WINDOW_HEIGHT,"images/collide.png")
collision_group.add(collidewalls)
pygame.display.set_caption("Space Invaders")
def display():
    window.fill((255,255,255))
    collision_group.draw(window)
    space_group.draw(window)
    player_group.draw(window)
    

done=False
while not done:
    window.fill((255,255,255))
    start_group.draw(window)
    start_btn.draw(window)
    #gridHelp(window,WINDOW_WIDTH,WINDOW_HEIGHT)
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        start_btn.update(pos,event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(fps)

while True:
    display()
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        
      # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    
        key_input = pygame.key.get_pressed()
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            #If they click the reset button the game will reset
    billy.move()
    if billy.check_hit(collision_group):
        billy.back()

    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw