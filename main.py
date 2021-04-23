import pygame
pygame.init()

frame_per_sec = pygame.time.Clock()

display_surface = pygame.display.set_mode((1440,1024))

pygame.display.set_caption("Words Legends")

backgroundmenu = pygame.image.load('assets/fond_menu.jpg')

x = True

while x:

    pygame.display.update()

    display_surface.blit(backgroundmenu,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    frame_per_sec.tick(60)