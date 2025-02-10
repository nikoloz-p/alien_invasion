import pygame

class Ship:
    """initialize ship"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        """load the ship, set starting position"""
        self.image = pygame.image.load("images/pngegg.png")
        self.image = pygame.transform.smoothscale(self.image, (100, 80))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)