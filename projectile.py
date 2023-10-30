import pygame,sys

class Projectile(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,image_to_use,spee=10):
        super().__init__()
        self.image = pygame.image.load(image_to_use)
        self.image = pygame.transform.scale(self.image , (width, height)).convert_alpha() 
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.spee= spee
    def speed(self):
        self.rect.y -= self.spee
    def update(self):
        if self.rect.bottom < 0:
            self.kill()
    def check_hit(self,group):
        if pygame.sprite.spritecollide(self,group, False, collided=pygame.sprite.collide_mask):
            return True
        else:
            return False