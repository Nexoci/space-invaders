#Name:
#Date:
#Basic PyGame Setup Code
import pygame,sys,time
from player import Player
from player import Health
from projectile import Projectile
from projectile import EProjectile
from backround import backround
from buttons import imagebutton
from static import stillimage
from Enemy import Evil
from blockers import Blockers

import pygame,random
import sys

    

pygame.init()
def exit():
    pygame.quit()
    sys.exit()
def next():
    global done
    done=True

    
    
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
cooldown=fps/30
Icon = pygame.image.load("images/spacers.jpg")
#Creating Groups
player_group = pygame.sprite.Group()
space_group = pygame.sprite.Group()
collision_group = pygame.sprite.Group()
start_group = pygame.sprite.Group()
starttext_group = pygame.sprite.Group()
start_btn= pygame.sprite.Group()
projectile_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()
blocker_group = pygame.sprite.Group()
Health_group =pygame.sprite.Group()
#creates window and custom objects
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
font = pygame.font.SysFont('Consolas', 30)
billy=Player(350,600,125,75,"images/billy.png",10)
alien2=Evil(85,200,125,100,"images/enemy.png",10)
alien3=Evil(150,200,125,100,"images/enemy.png",10)
alien4=Evil(215,200,125,100,"images/enemy.png",10)
alien5=Evil(280,200,125,100,"images/enemy.png",10)
alien6=Evil(345,200,125,100,"images/enemy.png",10)
alien7=Evil(410,200,125,100,"images/enemy.png",10)
alien8=Evil(475,200,125,100,"images/enemy.png",10)
alien9=Evil(540,200,125,100,"images/enemy.png",10)
blocker1= Blockers(300,475,125,125,"blockers/good.png","blockers/hit.png","blockers/broken.png","blockers/damaged.png","blockers/destroyed.png",4)
blocker2= Blockers(560,475,125,125,"blockers/good.png","blockers/hit.png","blockers/broken.png","blockers/damaged.png","blockers/destroyed.png",4)
blocker3= Blockers(10,475,125,125,"blockers/good.png","blockers/hit.png","blockers/broken.png","blockers/damaged.png","blockers/destroyed.png",4)
Healthbars= Health(50,740,600,50,"images/healthbar.png","images/healthbar2.png","images/healthbar3.png","images/healthbarD.png")
spaceback=backround(WINDOW_WIDTH,WINDOW_HEIGHT,"images/spacers.jpg")
help= stillimage(105,390,500,400,"images/help.png")
author= stillimage(275,75,150,100,"images/author.png")
btn_ply= imagebutton(225,100,250,250,"images/play.png","images/playclicked.png",next)
btn_ext= imagebutton(225,200,250,250,"images/exits.png","images/exitclicked.png",exit)
startback=backround(WINDOW_WIDTH,WINDOW_HEIGHT,"images/startback.jpg")
collidewalls=backround(WINDOW_WIDTH,WINDOW_HEIGHT,"images/collide.png")
title= stillimage(125,0,500,250,"images/title.png")
blocker_group.add(blocker1,blocker2,blocker3)
player_group.add(billy)
alien_group.add(alien2,alien3,alien4,alien5,alien6,alien7,alien8,alien9)
space_group.add(spaceback)
Health_group.add(Healthbars)
start_btn.add(btn_ply,btn_ext)
start_group.add(startback,title,help,author)
collision_group.add(collidewalls)
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(Icon)

def display():
    window.fill((255,255,255))
    collision_group.draw(window)
    space_group.draw(window)
    projectile_group.draw(window)
    player_group.draw(window)
    alien_group.draw(window)
    Health_group.draw(window)
    blocker_group.draw(window)
    #gridHelp(window,WINDOW_WIDTH,WINDOW_HEIGHT)

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
    shoot_cooldown = 0
    cooldown=cooldown-1
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for alien in alien_group:
        alien.move()
        if alien.check_hit(collision_group):
            alien.move()
        # Randomly decide whether to shoot
            if random.randint(1, 10) <= 5 and cooldown<0:
                E_bullet = EProjectile((alien2.rect.x + 33), (alien2.rect.centery - 40), 60, 32, "images/bullet.png")
                alien_group.add(E_bullet)
                #cooldown=0
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_SPACE] and cooldown<0:
        bullet = Projectile((billy.rect.x+33), (billy.rect.centery-40),60,32,"images/bullet.png")
        projectile_group.add(bullet) 
        cooldown=10
        if bullet.check_hit(alien_group):
            bullet.kill()
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
    pygame.sprite.groupcollide(projectile_group,alien_group,True,True, collided=pygame.sprite.collide_mask)
    if billy.check_hit(collision_group):
        billy.back()
    if billy.check_hit(alien_group):
        Healthbars.healthhit()
    if blocker1.check_hit(projectile_group):
        blocker1.damage()
        bullet.kill()
    if blocker2.check_hit(projectile_group):
        blocker2.damage()
        bullet.kill()
    if blocker3.check_hit(projectile_group):
        blocker3.damage()
        bullet.kill()
        
    

            
        
    billy.move()
    
    projectile_group.update()  # Update the projectiles
    alien_group.update()
    blocker_group.update()
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw
