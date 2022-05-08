import pygame




class Ship(pygame.sprite.Sprite):

    def __init__(self, settings):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('media/starship.png')
        self.rect = self.image.get_rect()
        self.screenHeight = settings.screen_height
        self.screenWidth = settings.screen_width
        self.rect.center = (200, self.screenHeight/2)
        self.damage = 0
        self.bitcoinMine = 0
        self.bitcoinLaunched = 0
        self.velocity = 5  #move at the speed of 5 pixels per frame

    def update(self):
        #Ifs not allowing our roadster to go off bounds
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.screenWidth:
            self.rect.right = self.screenWidth
        if self.rect.top <=0:
            self.rect.top = 0
        if self.rect.bottom >= self.screenHeight:
            self.rect.bottom = self.screenHeight

        #Increment bitcoin miner every frame
        if self.bitcoinMine <100:
            self.bitcoinMine +=1

    #in order to have the bitcoin sprite be created inside the main game loop, this function
    #just returns a flag to have a bitcoin be instantiated there. 
    def launchBitcoin(self):
        if self.bitcoinMine >= 100:
            self.bitcoinMine = 0
            self.bitcoinLaunched = 1

    #steering functions
    def left(self):
        self.rect.centerx -= self.velocity
    def right(self):
        self.rect.centerx += self.velocity
    def up(self):
        self.rect.centery -= self.velocity
    def down(self):
        self.rect.centery += self.velocity


