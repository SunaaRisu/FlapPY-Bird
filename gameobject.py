import pygame


class Gameobject:
    def __init__(self,
                 pos: list[int, int],
                 size: tuple[int, int],
                 asset: str = None,
                 gravity: bool = False,
                 velocity: list[float, float] = [0, 0]):
        self.pos = list(pos)
        self.velocity = list(velocity)
        self.size = tuple(size)
        if asset:
            self.asset = pygame.image.load(asset)
        self.gravity = gravity

    def update(self,
               dt: float,
               movement: tuple[bool, bool] = (False, False),
               size: tuple[int, int] = (0, 0)):
        self.asset = pygame.transform.scale(self.asset,
                                            (self.size[0] + size[0],
                                             self.size[1] + size[1]))
        if self.gravity:
            self.velocity[1] += (15.67 * dt)

        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

    def render(self, surf):
        surf.blit(self.asset, self.pos)
