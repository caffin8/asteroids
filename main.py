# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()  #Create clock instance
    dt = 0
    running = True
    

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Set running to False
        
        screen.fill("black")
        pygame.display.flip()
        

        dt = clock.tick(60) / 1000.0  # Convert to seconds
    

    pygame.quit()

if __name__ == "__main__":
    main()
