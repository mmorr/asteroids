import pygame
from constants import * 
from player import Player

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
    clock = pygame.time.Clock()
    FPS = 60
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for sprite in drawable:    
            sprite.draw(screen)
        for sprite in updatable:
            sprite.update(dt)
        pygame.display.flip()
        dt = clock.tick(FPS)/1000
            
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
