import pygame
import sys
import random

pygame.init()
wn = pygame.display.set_mode((576, 576))
clock = pygame.time.Clock()
game_font = pygame.font.Font('sounds_n_shit/04B_19.TTF', 50)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 7.5
                flap_sound.play()

    wn.blit(bg_surface, (0, 0))

    pygame.display.update()
    clock.tick(120)
