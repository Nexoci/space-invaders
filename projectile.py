import pygame,sys

class Projectile(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,image_to_use,speed=10):
        super().__init__()
        self.image = pygame.image.load(image_to_use)
        self.image = pygame.transform.scale(self.image , (width, height)).convert_alpha() 
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.speed = speed
    def move(self):
        self.rect.y -= self.speed
    def update(self):
        self.move()
    def check_hit(self,group):
        if pygame.sprite.spritecollide(self,group, True, collided=pygame.sprite.collide_mask):
            pass