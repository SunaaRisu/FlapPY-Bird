import pygame


class Entity:
    def __init__(self, pos: list[int, int], size: tuple[int, int], asset: str = None, velocity: list[int, int] = [0, 0]):
        self.pos = list(pos)
        self.velocity = [0, 0]
        self.size = tuple(size)
        if asset:
            self.asset = pygame.image.load(asset)

    def update(self, movement: tuple[int, int] = (0, 0), acceleration: tuple[int, int] = (0, 0), size: tuple[int, int] = (0, 0)):
        self.asset = pygame.transform.scale(self.asset, (self.size[0] + size[0], self.size[1] + size[1]))

    def render(self, surf):
        surf.blit(self.asset, self.pos)
