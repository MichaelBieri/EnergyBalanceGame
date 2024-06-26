# EnergyBalanceGame
# MichaelBieri, June 2024

import threading
from welcome_window import WelcomeWindow
from game import Game
import pygame

if __name__ == "__main__":
    welcome_window = WelcomeWindow()
    welcome_window.show_welcome_window()

    # Start the game after the welcome window is closed
    game = Game()
    game.run()
    pygame.quit()

