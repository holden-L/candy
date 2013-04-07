import pygame
from main import HEIGHT, WIDTH
from main import SPEED
from main import UP, DOWN, LEFT, RIGHT


class Player:
    def __init__(self, size, image):
        self.player = pygame.Rect(100, 100, size, size)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (size, size))

    def update(self):
        if UP and self.player.top > 0:
            self.player.top -= SPEED
        if DOWN and self.player.bottom < HEIGHT:
            self.player.top += SPEED
        if LEFT and self.player.left > 0:
            self.player.left -= SPEED
        if RIGHT and self.player.right < WIDTH:
            self.player.left += SPEED
