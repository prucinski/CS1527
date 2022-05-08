import pygame
import random

class Alien(pygame.sprite.Sprite):

    #init method has a flag - when we initialize the game, not all roadsters appear in one line. They will only
    #appear off-screen after having reached left border/being destroyed
    def __init__(self, settings, spawnPosFlag ="default"):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('media/roadster.png')
        self.rect = self.image.get_rect()
        self.screenHeight = settings.screen_height
        self.screenWidth = settings.screen_width
        if spawnPosFlag == "default":
            self.spawnPos = [self.screenWidth + 20, random.randint(20, self.screenHeight - 20)]
        else:
            self.spawnPos = [random.randint(self.screenWidth/2, self.screenWidth) ,random.randint(20, self.screenHeight - 20)]
        self.rect.center = self.spawnPos
        self.velocity = random.randint(2,7)
   
    #the idea to reset the position of the roadsters instead of deleting them came from http://programarcadegames.com/index.php?chapter=introduction_to_sprites&lang=en#section_13
    def reset(self):
        self.velocity = random.randint(2, 7)
        self.spawnPos = [self.screenWidth + 20, random.randint(20, self.screenHeight - 20)]
        self.rect.center = self.spawnPos

    def update(self):
        #if gone off bounds, reset
        if self.rect.right <= 0:
            self.reset()
  
        self.rect.centerx -= self.velocity


