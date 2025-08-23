import pygame

import sys

from entity import Entity


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

        self.player = Entity((400, 400),
                             (110, 80),
                             "assets/bird.png",
                             True)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.blit(self.bg, (0, 0))

            self.player.update(self.dt)
            self.player.render(self.screen)

            pygame.display.flip()

            self.dt = self.clock.tick(60) / 1000

        pygame.quit()
        sys.exit()

