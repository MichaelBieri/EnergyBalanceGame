# EnergyBalanceGame
# MichaelBieri, Mai 2024

import pygame
import tkinter as tk
class Game:
    def __init__(self):
        pygame.init()
        self.window_width = 1200
        self.window_height = 600
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption(("EnergyBalanceGame"))
        self.clock = pygame.time.Clock()
        self.run()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            self.delta_time = self.clock.tick(60) / 1000
            self.window.fill((50, 50, 25)) # Farbe Hintergrund
            pygame.display.update()

        pygame.quit()

game = Game()