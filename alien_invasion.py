import sys
import pygame
from settings import Settings
from ship import Ship
from sky import StarrySky

class AlienInvasion:
    """general class to manage game assests and behavior"""

    def __init__(self):
        """initialize the game"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.starry_sky = StarrySky(self.screen, self.settings.screen_width, self.settings.screen_height)

    def run_game(self):
        """run game"""
        while True:
            "keyboard/mouse events"
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                if event.key == pygame.K_UP:
                    self.ship.moving_up = True
                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.starry_sky.draw()
        self.ship.blitme()

        pygame.display.flip()

if __name__ == "__main__":

    ai = AlienInvasion()
    ai.run_game()