# EnergyBalanceGame
# MichaelBieri, Mai 2024

import pygame
import random
import sys

# Screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("EnergyBalanceGame")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            self.events()
            self.clock.tick(60)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

        self.delta_time = self.clock.tick(60) / 1000 # 60 pic/s
        self.window.fill((50, 50, 25))  # background color
        pygame.display.update()

# Main program
if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()