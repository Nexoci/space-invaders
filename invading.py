#Name:
#Date:
#Basic PyGame Setup Code
import pygame,sys,time
from player import Player
from projectile import Projectile
from backround import backround
from buttons import imagebutton
from static import stillimage
from Enemy import Evil
from blockers import Blockers



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
#creates window and custom objects
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
font = pygame.font.SysFont('Consolas', 30)
billy=Player(350,600,125,75,"images/billy.png",10)
alien1=Evil(350,200,125,100,"images/enemy.png",10)
alien2=Evil(350,200,125,100,"images/enemy.png",10)
alien3=Evil(350,200,125,100,"images/enemy.png",10)
alien4=Evil(350,200,125,100,"images/enemy.png",10)
alien5=Evil(350,200,125,100,"images/enemy.png",10)
alien6=Evil(350,200,125,100,"images/enemy.png",10)
alien7=Evil(350,200,125,100,"images/enemy.png",10)
alien8=Evil(350,200,125,100,"images/enemy.png",10)
alien9=Evil(350,200,125,100,"images/enemy.png",10)
alien10=Evil(350,200,125,100,"images/enemy.png",10)
alien11=Evil(350,200,125,100,"images/enemy.png",10)
alien12=Evil(350,200,125,100,"images/enemy.png",10)
alien13=Evil(350,200,125,100,"images/enemy.png",10)
blocker1= Blockers(310,500,100,100,"blockers/good.png",1)
spaceback=backround(WINDOW_WIDTH,WINDOW_HEIGHT,"images/spacers.jpg")
lifeleft= stillimage(50,740,600,50,"images/healthbar.png")
help= stillimage(105,390,500,400,"images/help.png")
author= stillimage(275,75,150,100,"images/author.png")
btn_ply= imagebutton(225,100,250,250,"images/play.png","images/playclicked.png",next)
btn_ext= imagebutton(225,200,250,250,"images/exits.png","images/exitclicked.png",exit)
startback=backround(WINDOW_WIDTH,WINDOW_HEIGHT,"images/startback.jpg")
collidewalls=backround(WINDOW_WIDTH,WINDOW_HEIGHT,"images/collide.png")
title= stillimage(125,0,500,250,"images/title.png")
blocker_group.add(blocker1)
player_group.add(billy)
alien_group.add(alien1,alien2,alien3,alien4,alien5,alien6,alien7,alien8,alien9,alien10,alien11,alien12,alien13)
space_group.add(spaceback,lifeleft)
start_btn.add(btn_ply,btn_ext)
start_group.add(startback,title,help,author)
collision_group.add(collidewalls)
pygame.display.set_caption("Space Invaders")

def display():
    window.fill((255,255,255))
    collision_group.draw(window)
    space_group.draw(window)
    projectile_group.draw(window)
    player_group.draw(window)
    alien_group.draw(window)
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
    cooldown=cooldown-1
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_SPACE] and cooldown<0:
        bullet = Projectile((billy.rect.x+33), (billy.rect.centery-40),60,32,"images/bullet.png")
        projectile_group.add(bullet) 
        cooldown=20
        if bullet.check_hit(alien_group):
            bullet.kill()
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
    if alien1.check_hit(projectile_group):
        alien1.kill()
        bullet.kill()
    if billy.check_hit(collision_group):
        billy.back()
    if alien1.check_hit(collision_group):
        alien1.move()
    
    pygame.sprite.groupcollide(projectile_group,blocker_group,True,True)
    #if blocker1.check_hit(projectile_group):
     #   for entity in blocker_group:
      #      print(entity)
        #blocker1.kill()
       
     #   %blocker1.damage()
    #bullet.kill()
        
    billy.move()
    alien1.move()
    projectile_group.update()  # Update the projectiles
    alien_group.update()
    blocker_group.update()
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw