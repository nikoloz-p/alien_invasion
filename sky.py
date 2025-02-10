import random
import pygame

class StarrySky:
    def __init__(self, screen, width, height, num = 200):
        self.screen = screen
        self.width = width
        self.height = height
        self.num = num
        self.stars = [(random.randint(0, width), random.randint(0, height)) for _ in range(num)]

    def draw(self):
        for star in self.stars:
            pygame.draw.circle(self.screen, (255,255,255), star, 1)