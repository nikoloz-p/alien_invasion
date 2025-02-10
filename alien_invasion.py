import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """general class to manage game assests and behavior"""

    def __init__(self):
        """initialize the game"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        """set bg color"""
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """run game"""
        while True:
            "keyboard/mouse events"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            
            pygame.display.flip()

if __name__ == "__main__":

    ai = AlienInvasion()
    ai.run_game()