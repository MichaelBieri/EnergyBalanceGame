import pygame
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