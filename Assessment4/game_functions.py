import sys
import pygame

pygame.font.init()
gameOverFont = pygame.font.SysFont('arial', 60)
displayFont = pygame.font.SysFont('arial', 20)

WHITE = (255, 255, 255)



def check_events(screen, ship, sprites):
    """Respond to key presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move ship right.
                ship.right()
            elif event.key == pygame.K_LEFT:
                # Move ship left.
                ship.left()
            elif event.key == pygame.K_q:
                # Move ship up.
                ship.up()
            elif event.key == pygame.K_a:
                # Move ship down.
                ship.down()
            if event.key == pygame.K_SPACE:
                # Launch bitcoin
               ship.launchBitcoin()
            # ANY OTHER KEY OPTIONS GO HERE

def update_screen(sprites, ai_settings, screen, ship):

    """Update sprites & messages on the screen.""" 
    screen.blit(ai_settings.screen_backgrnd, (0,0))
    sprites.draw(screen)
    rects = sprites.draw(screen)
    
    
    # If damage reaches 100%, display CRASHED message
    
    if ship.damage >= 100:
        crashedText = gameOverFont.render('You have crashed!', True, 'White', 'Black')
        crashedTextRect = crashedText.get_rect()
        crashedTextRect.center = (ai_settings.screen_width/2, ai_settings.screen_height/2)
        screen.blit(crashedText, crashedTextRect)
                
    # Update the instrument readings
    #Damage
    damageText = displayFont.render(str(ship.damage) + "%", True, 'White')
    damageTextRect = damageText.get_rect()
    damageTextRect.center = (ai_settings.screen_width/10, ai_settings.screen_height/35)
    screen.blit(damageText, damageTextRect)
    #Lives
    lifeText = displayFont.render(str(ai_settings.lives), True, 'White')
    lifeTextRect = lifeText.get_rect()
    lifeTextRect.center = (ai_settings.screen_width/5, ai_settings.screen_height/35)
    screen.blit(lifeText, lifeTextRect)
    #Score
    scoreText = displayFont.render(str(ai_settings.score), True, 'White')
    scoreTextRect = scoreText.get_rect()
    scoreTextRect.center = (ai_settings.screen_width/10, ai_settings.screen_height/15)
    screen.blit(scoreText, scoreTextRect)
    #Bitcoin
    bitcoinText = displayFont.render(str(ship.bitcoinMine), True, 'White')
    bitcoinTextRect = bitcoinText.get_rect()
    bitcoinTextRect.center = (ai_settings.screen_width/3.5, ai_settings.screen_height/16.5)
    screen.blit(bitcoinText, bitcoinTextRect)
    
    # Update the background region.
    pygame.display.update(rects)
    pygame.display.flip()


        