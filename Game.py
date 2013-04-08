import sys
import time
import pygame
import pygame.locals
from main import HEIGHT, WIDTH
import Player
import Candy


class Game:
    def __init__(self):
        pygame.init()
        self.windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
        pygame.display.set_caption("Candy")
        self.mainClock = pygame.time.Clock()
        self.player = Player.Player(size=30, image="Resources/player.png")
        self.candy = Candy.Candy(size=50, image="Resources/candy.png")
        self.score, self.lives, self.FPS = 0, 5, 60
        self.font = pygame.font.SysFont("Anoymous Pro", 48)

    def write(self, fontSurface, location):
        self.windowSurface.blit(fontSurface, location)

    def eventhandle(self, event):
        if event.type == pygame.locals.QUIT:
            print "Score: %d" % (self.score)
            pygame.quit()
            sys.exit()
        elif event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.locals.K_UP or event.key == ord('w'):
                Player.UP, Player.DOWN = True, False
            elif event.key == pygame.locals.K_DOWN or event.key == ord('s'):
                Player.DOWN, Player.UP = True, False
            elif event.key == pygame.locals.K_LEFT or event.key == ord('a'):
                Player.LEFT, Player.RIGHT = True, False
            elif event.key == pygame.locals.K_RIGHT or event.key == ord('d'):
                Player.RIGHT, Player.LEFT = True, False
        elif event.type == pygame.locals.KEYUP:
            if event.key == pygame.locals.K_UP or event.key == ord('w'):
                Player.UP = False
            elif event.key == pygame.locals.K_DOWN or event.key == ord('s'):
                Player.DOWN = False
            elif event.key == pygame.locals.K_LEFT or event.key == ord('a'):
                Player.LEFT = False
            elif event.key == pygame.locals.K_RIGHT or event.key == ord('d'):
                Player.RIGHT = False
            elif event.key == ord('m'):
                self.candy.mute = not self.candy.mute

    def mainloop(self):
        prev = time.time()
        scoreSurface = self.font.render(str(0), 1, (255, 255, 255))
        lifeSurface = self.font.render(str(self.lives), 1, (255, 0, 40))
        while 1:
            for event in pygame.event.get():
                self.eventhandle(event)
            if self.player.player.colliderect(self.candy.candy):
                self.score += 1
                prev = time.time()
                self.candy.move()
                scoreSurface = self.font.render(str(self.score), 1,
                                                (255, 255, 255))
            if time.time() - prev >= 1.75:
                self.lives -= 1
                prev = time.time()
                self.candy.timeout()
                lifeSurface = self.font.render(str(self.lives), 1,
                                               (255, 0, 40))
            if self.lives == 0:
                print "Score: %d" % (self.score)
                pygame.quit()
                sys.exit()
            self.windowSurface.fill((0, 0, 0))
            self.write(lifeSurface, (WIDTH - lifeSurface.get_width() - 5, 5))
            self.write(scoreSurface, (5, 5))
            self.player.update()
            self.windowSurface.blit(self.player.image, self.player.player)
            self.windowSurface.blit(self.candy.image, self.candy.candy)
            pygame.display.update()
            self.mainClock.tick(self.FPS)
