import pygame

import sys

from player import Player
from gameobject import Gameobject
from random import randint


class Game:
    def __init__(self, title: str, height: int, width: int):
        pygame.init()
        self.title = title
        pygame.display.set_caption(self.title)

        self.height = height
        self.width = width

        self.screen = pygame.display.set_mode((self.height, self.width))
        self.clock = pygame.time.Clock()
        self.dt = 0

        self.running = True

        self.bg = pygame.image.load("assets/background.png")

        self.player = Player((400, 400),
                             (110, 80),
                             "assets/bird.png",
                             True)
        self.gameobjects = []

        self.SPAWNPIPE = pygame.USEREVENT
        pygame.time.set_timer(self.SPAWNPIPE, 2000)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        self.running = False
                    case pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.player.update(self.dt, [0, 1])
                    case self.SPAWNPIPE:
                        self.gameobjects.append(Gameobject((1600, (-900 - randint(0, 450))), (25 * 7, 450 * 7), "assets/pipe.png", velocity=[-7, 0]))

            self.screen.blit(self.bg, (0, 0))

            self.player.update(self.dt)
            self.player.render(self.screen)

            for object in self.gameobjects:
                object.update(self.dt)
                object.render(self.screen)

            pygame.display.flip()

            self.dt = self.clock.tick(60) / 1000

        pygame.quit()
        sys.exit()
