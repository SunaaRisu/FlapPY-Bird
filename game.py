import pygame

import sys


class Game:
    def __init__(self, title: str, height: int, width: int):
        pygame.init()
        self.title = title
        pygame.display.set_caption(self.title)

        self.height = height
        self.width = width

        self.screen = pygame.display.set_mode((self.height, self.width))
        self.clock = pygame.time.Clock()

        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill("purple")

            pygame.display.flip()

        pygame.quit()
        sys.exit()

