# EnergyBalanceGame
# MichaelBieri, Mai 2024
import pygame
import sys

class Icon:
    def __init__(self, image_path, relative_position, screen_width, screen_height):
        self.image = pygame.image.load(image_path)
        self.position = (
            int(screen_width * relative_position[0] - self.image.get_width() / 2),
            int(screen_height * relative_position[1] - self.image.get_height() / 2)
        )

    def draw(self, window):
        window.blit(self.image, self.position)

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 1200
        self.screen_height = 600
        self.window = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("EnergyBalanceGame")
        self.clock = pygame.time.Clock()
        self.running = True

        # Load and scale the background image
        self.background_image = pygame.image.load('Pictures/EnergyBalanceGame_background.png')
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, self.screen_height))

        # Create icons
        self.icons = [
            Icon('Pictures/EnergyBalanceGame_solar.png', (0.2, 0.8), self.screen_width, self.screen_height),
            Icon('Pictures/EnergyBalanceGame_water.png', (0.3, 0.8), self.screen_width, self.screen_height),
            Icon('Pictures/EnergyBalanceGame_wind.png', (0.4, 0.8), self.screen_width, self.screen_height),
            Icon('Pictures/EnergyBalanceGame_nuclear.png', (0.5, 0.8), self.screen_width, self.screen_height),
            Icon('Pictures/EnergyBalanceGame_storage.png', (0.6, 0.8), self.screen_width, self.screen_height),
            Icon('Pictures/EnergyBalanceGame_foreign.png', (0.7, 0.8), self.screen_width, self.screen_height)
        ]

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
        for icon in self.icons:
            icon.draw(self.window)
        pygame.display.flip()

# Main program
if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
