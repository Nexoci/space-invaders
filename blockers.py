import pygame,sys


class Blockers(pygame.sprite.Sprite):
    def __init__(self,start_x,start_y,width,height,start_image,hits):
        super().__init__() 
        self.image = pygame.image.load(start_image)
        self.image = pygame.transform.scale(self.image , (width, height)).convert_alpha() 
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        self.health=hits
    def damage(self):
        self.health -= 1
        if self.health <= 0:
            self.kill()
            #self.rect.x = 9000
    def check_hit(self,group):
        if pygame.sprite.spritecollide(self,group, False, collided=pygame.sprite.collide_mask):
            return True
        else:
            return False