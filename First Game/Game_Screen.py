
import pygame
pygame.init()


screen = pygame.display.set_mode([1000, 300])


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (136, 8, 8), (500, 150), 75)

    pygame.display.flip()


pygame.quit()
