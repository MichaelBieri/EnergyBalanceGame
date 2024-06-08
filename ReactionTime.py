import pygame

class ReactionTime:
    def __init__(self, game):
        self.game = game
        self.surface = game.window

    def update(self):
        pass

    def change(self):
        keys = pygame.key.get_pressed()