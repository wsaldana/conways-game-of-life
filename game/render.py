import time

import pygame as pg
from pygame import surface

from game.elements.world import World


class Render:
    def __init__(self, width: int, height: int, pattern: list):
        self.width = width
        self.height = height
        self.screen = None
        self.screen = None
        self.world = None
        self.start(w=width, h=height, pattern=pattern)

    def start(self, **kargs):
        pg.init()

        self.win = pg.display.set_mode((kargs['w']*5, kargs['h']*5))
        self.screen = pg.Surface((kargs['w'], kargs['h']))

        self.world = World(
            self.screen.get_width(),
            self.screen.get_height()
        )
        for p in kargs['pattern']:
            self.world.load(*p)

    def run(self):
        clock = pg.time.Clock()

        loop = True

        while loop:
            self.draw()
            self.world.traverse()

            pg.time.delay(100)
            pg.display.flip()
            clock.tick(15)

            self.win.blit(
                pg.transform.scale(self.screen, self.win.get_rect().size),
                (0, 0)
            )
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    loop = False
                    break

    def draw(self):
        for y in range(self.height):
            for x in range(self.width):
                color = (0, 255 * self.world.get(x, y), 0)
                self.screen.set_at((x, y), color)
