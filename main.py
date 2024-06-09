# EnergyBalanceGame
# MichaelBieri, Mai 2024

import pygame
import sys

relative_position = (0.2, 0.8)  # Ratio of the image position to the relative window size (x, y as a percentage)

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 1200
        self.screen_height = 600
        self.window = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("EnergyBalanceGame")
        self.clock = pygame.time.Clock()
        self.running = True
        self.background_image = pygame.image.load('Pictures/EnergyBalanceGame_background.png')
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, self.screen_height))
        self.solar_icon = pygame.image.load('Pictures/EnergyBalanceGame_solar.png')
        self.position = (
            int(self.screen_width * relative_position[0] - self.solar_icon.get_width() / 2),
            int(self.screen_height * relative_position[1] - self.solar_icon.get_height() / 2)
        )

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.render()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

    def update(self):
        self.delta_time = self.clock.tick(60) / 1000  # 60 FPS

    def render(self):
        self.window.blit(self.background_image, (0, 0))
        self.window.blit(self.solar_icon, self.position)
        pygame.display.flip()

# Main program
if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()