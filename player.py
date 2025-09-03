import pygame

from gameobject import Gameobject


class Player(Gameobject):
    def __init__(self,
                 pos: list[int, int],
                 size: tuple[int, int],
                 asset: str = None,
                 gravity: bool = False,
                 velocity: list[float, float] = [0, 0],
                 alive: bool = True):
        super().__init__(pos, size, asset, gravity, velocity)
        self.alive = alive

    def update(self,
               dt: float,
               movement: list[int, int] = [0, 0],
               size: tuple[int, int] = (0, 0)):
        super().update(dt)
        if movement[1] == 1:
            self.velocity[1] = -10.0
