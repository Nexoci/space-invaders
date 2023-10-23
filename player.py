import pygame
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self, startX,startY,width,height,image_to_use,speed):
            super().__init__() 
            self.image = pygame.image.load(image_to_use)
            self.image = pygame.transform.scale(self.image , (width, height)).convert_alpha() 
            self.mask  = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect(topleft=(startX,startY))
            self.speed = speed
    def back(self):
        self.rect.x -= self.movex
    def move(self):
        key_input = pygame.key.get_pressed()
        self.movex = (key_input[pygame.K_LEFT] * -self.speed) + (key_input[pygame.K_RIGHT] * self.speed)
        self.rect.x += self.movex
    def check_hit(self,group):
        if pygame.sprite.spritecollide(self,group, False, collided=pygame.sprite.collide_mask):
            return True
        else:
            return False