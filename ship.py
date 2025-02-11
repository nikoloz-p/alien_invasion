import pygame

class Ship:
    """initialize ship"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        """load the ship, set starting position"""
        self.image = pygame.image.load("images/pngegg.png")
        self.image = pygame.transform.smoothscale(self.image, (100, 80))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # set flag for controls
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_up and self.rect.top > 600:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)

