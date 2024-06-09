import pygame

class Icon:
    def __init__(self, icon_path, relative_position, screen_width, screen_height):
        self.icon = pygame.image.load(icon_path)
        self.position = (
            int(screen_width * relative_position[0] - self.icon.get_width() / 2),
            int(screen_height * relative_position[1] - self.icon.get_height() / 2)
        )

    def draw(self, window):
        window.blit(self.icon, self.position)
