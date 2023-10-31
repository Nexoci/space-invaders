import pygame
import sys

class Evil(pygame.sprite.Sprite):
    def __init__(self, startX,startY,width,height,image_to_use,speed):
        super().__init__() 
        self.image = pygame.image.load(image_to_use)
        self.image = pygame.transform.scale(self.image , (width, height)).convert_alpha() 
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
        self.speed = speed
        self.direction=True
    def move(self):
        if self.direction:
            self.rect.x += self.move
    def check_hit(self,group):
        if pygame.sprite.spritecollide(self,group, True, collided=pygame.sprite.collide_mask):
            pass