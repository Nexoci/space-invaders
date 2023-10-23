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
fps = 30
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 800
player_group = pygame.sprite.Group()
space_group = pygame.sprite.Group()
collision_group = pygame.sprite.Group()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
billy=Player(350,600,125,75,"images/billy.png",10)
player_group.add(billy)
spaceback=backround(WINDOW_WIDTH,WINDOW_HEIGHT,"images/spacers.jpg")
space_group.add(spaceback)
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
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
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