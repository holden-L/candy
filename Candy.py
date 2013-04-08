import pygame
from random import randrange
from main import HEIGHT, WIDTH


class Candy:
    def __init__(self, size, image):
        self.candy = pygame.Rect(randrange(WIDTH),
                                 randrange(HEIGHT),
                                 size, size)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (size, size))
        self.size = size
        self.pickup = pygame.mixer.Sound('Resources/pickup.wav')
        self.mute = False

    def move(self):
        if self.mute == False:
            self.pickup.play()
        self.candy.top = randrange(self.size, HEIGHT) - self.size
        self.candy.left = randrange(self.size, WIDTH) - self.size

    def timeout(self):
        self.candy.top = randrange(self.size, HEIGHT) - self.size
        self.candy.left = randrange(self.size, WIDTH) - self.size
