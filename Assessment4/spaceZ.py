import pygame

# COMPLETE FILE PROVIDED IN STARTER CODE
from settings import Settings

# PARTIAL FILE PROVIDED IN STARTER CODE
import game_functions as gf
from ship import Ship
from aliens import Alien
from bitcoin import Bitcoin
# IMPORT OTHER FILES/CLASSES HERE AS REQUIRED
def run_game():
    # Initialize pygame, settings and screen object.
    pygame.init()
    
    # Set keys to repeat if held down.
    pygame.key.set_repeat(5,5)

    #create a clock for the game
    clock = pygame.time.Clock()
    
    # Create settings object containing game settings
    ai_settings = Settings()
    
    # Create the main game screen
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    screen.blit(ai_settings.screen_backgrnd, [0, 0])
    
    # Create a main window caption
    pygame.display.set_caption("Space Z - Mars Flight")

    #3 lives loop
    while ai_settings.lives > 0:

        sprites = pygame.sprite.Group()
        damageToShipSprites = pygame.sprite.Group()
        damageToAlienSprites = pygame.sprite.Group()

        ship = Ship(ai_settings)
        sprites.add(ship)

        #creating (here 20) alien sprites, and grouping them both into sprites (for updating and drawing) and a subgroup (for collision detection)
        for i in range(ai_settings.aliens):
            alien = Alien(ai_settings, "start")
            sprites.add(alien)
            damageToShipSprites.add(alien)

        # Refresh the background
        sprites.clear(screen, ai_settings.screen_backgrnd)
        
        # Start the main loop for the game.
        while ship.damage < 100:
            clock.tick(30)

            #creating a bitcoin inside the main game loop if in the previous loop spacebar was pressed
            if ship.bitcoinLaunched == 1:
                bitcoin = Bitcoin(ai_settings, ship)
                ship.bitcoinLaunched = 0
                sprites.add(bitcoin)
                damageToAlienSprites.add(bitcoin)

            # Watch for keyboard events.
            gf.check_events(screen, ship, sprites)

            # Tell all the sprites to update their status
            sprites.update()

            #Checking collisions
            shipHit = pygame.sprite.spritecollide(ship, damageToShipSprites, False)
            if shipHit:
               for roadster in shipHit:     #the list will have just one object most of the time, but spritecollide returns a list (so we iterate through list even if it has one element)
                   ship.damage += 10
                   roadster.reset()         #push back beyond right edge of the screen
               pygame.mixer.Sound.play(ai_settings.boom_sound)
    
            #checking if a bitcoin exists, and if so, detecting collisions
            if damageToAlienSprites:
                roadsterHit = pygame.sprite.spritecollide(bitcoin, damageToShipSprites, False)
                if roadsterHit:
                    for roadster in roadsterHit:
                        ai_settings.score +=10
                        roadster.reset()
                        if bitcoin.isSuper == 0:
                           bitcoin.kill()
                        else:
                            bitcoin.reset_angle()
                    pygame.mixer.Sound.play(ai_settings.boom_sound)
 
            # Now update the sprites, etc. on the screen
            gf.update_screen(sprites, ai_settings, screen, ship)

        # Wait for a keypress to continue
        null_event = pygame.event.wait() 

        # Remove a life
        ai_settings.lives -= 1

    print("your final score was", ai_settings.score) 
    # GAME ENDS 

# Call the main method to start the game        
run_game()
