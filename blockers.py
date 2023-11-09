import pygame
import sys

class shield(pygame.sprite.Sprite):
    def __init__(self, startX,startY,width,height,image_shield,image_hit,image_damaged,image_broken,image_dstyd):
            super().__init__() 
            self.img_good = pygame.image.load(image_shield)
            self.img_hit = pygame.image.load(image_hit)
            self.img_dmg = pygame.image.load(image_damaged)
            self.img_brkn = pygame.image.load(image_broken)
            self.img_dstyd = pygame.image.load(image_dstyd)  
            self.img_good = pygame.transform.scale(self.img_good , (width, height)).convert_alpha()
            self.img_hit = pygame.transform.scale(self.img_hit , (width, height)).convert_alpha() 
            self.img_dmg = pygame.transform.scale(self.img_dmg , (width, height)).convert_alpha()
            self.img_brkn = pygame.transform.scale(self.img_brkn , (width, height)).convert_alpha()
            self.img_dstyd = pygame.transform.scale(self.img_dstyd , (width, height)).convert_alpha()    
            self.mask  = pygame.mask.from_surface(self.img_good)
            self.image = self.img_good
            self.rect = self.image.get_rect(topleft=(startX,startY))
    def collide(self,group):
        if pygame.sprite.spritecollide(self,group, False, collided=pygame.sprite.collide_mask):
            return True
        else:
            return False