import pygame
import random
import math

class Bitcoin(pygame.sprite.Sprite):
   
    def __init__(self, settings, ship):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('media/bitcoin.png')
        self.rect = self.image.get_rect()
        self.screenHeight = settings.screen_height
        self.screenWidth = settings.screen_width
        self.rect.center = ship.rect.center
        self.velocity = 10
        self.isSuper = random.randint(0,1)
        #normal bitcoin
        if self.isSuper == 0:
            self.angle = 0
        #super bitcoin
        else:
            self.angle = random.randint(0, 359)

    def update(self):
        #copied (and modified) from ship.py
        #kill() removes this sprite from any sprite groups, leading it to not being
        #drawn

        if self.rect.right <= 0:
            self.kill()
        elif self.rect.left >= self.screenWidth:
            self.kill()
        elif self.rect.bottom <=0:
            self.kill()
        elif self.rect.top >= self.screenHeight:
            self.kill()

        #normal bitcoin and super bitcoin are unified here using trig functions
        self.rect.centerx += self.velocity*math.cos(self.angle*math.pi/180)
        self.rect.centery += self.velocity*math.sin(self.angle*math.pi/180)

    def reset_angle(self):
        self.angle = self.angle = random.randint(0, 359)

