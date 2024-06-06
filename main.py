# EnergyBalanceGame
# MichaelBieri, Mai 2024

# Press ⌃F5 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pygame

pygame.init()

window_width = 1200
window_height = 1000
window = pygame.display.set_mode((window_width, window_width))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    window.fill(25, 25, 25)
    pygame.display.update()

pygame.quit()