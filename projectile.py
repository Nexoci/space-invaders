import pygame,sys

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y,speed=20):
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill((120, 130, 122))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed=speed
    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()
    def check_hit(self,group):
        if pygame.sprite.spritecollide(self,group, False, collided=pygame.sprite.collide_mask):
            return True
        else:
            return False