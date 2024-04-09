import pygame
from sys import exit

pygame.init() #starts the engine
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Battaglia Navale")
clock = pygame.time.Clock()


test_surface = pygame.Surface((100,200))
test_surface.fill('Red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(test_surface,(200,100)) #blit (block image transfer) -> put surface on surface

    pygame.display.update()
    clock.tick(75)

