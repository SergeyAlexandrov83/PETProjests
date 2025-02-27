import os
import pygame as pg
from random import choice, randrange


class Symbol:
    def __init__(self, x, y, speed):
        self.x, self.y = x, y
        self.speed = speed
        self.value = choice(green_katakana)
        self.interval = randrange(1, 25)

    def draw(self, color):
        frames = pg.time.get_ticks()
        if not frames % self.interval:
            self.value = choice(green_katakana if color == 'green' else white_katakana)
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE
        surface.blit(self.value, (self.x, self.y))


class SymbolColumn:
    def __init__(self, x, y):
        self.column_height = randrange(15, 50)
        self.speed = randrange(1, 5)
        self.symbols = [Symbol(x, i, self.speed) for i in range(y, y - FONT_SIZE * self.column_height, -FONT_SIZE)]

    def draw(self):
        [symbol.draw('green') if i else symbol.draw('red') for i, symbol in enumerate(self.symbols)]


os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = 1600, 900
FONT_SIZE = 23
alpha_value = 0

pg.init()
screen = pg.display.set_mode(RES)
surface = pg.Surface(RES)
surface.set_alpha(alpha_value)
clock = pg.time.Clock()

katakana = [chr(int('0x30a0', 16) + i) for i in range(96)]
font = pg.font.Font('font/ms mincho.ttf', FONT_SIZE)
green_katakana = [font.render(char, True, (40, randrange(0, 256), 40)) for char in katakana]
white_katakana = [font.render(char, True, (160, randrange(160, 256), 160)) for char in katakana]

symbol_columns = [SymbolColumn(x, randrange(-HEIGHT, 0)) for x in range(0, WIDTH, FONT_SIZE)]

while True:
    screen.blit(surface, (0, 0))
    surface.fill(pg.Color('black'))

    [symbol_column.draw() for symbol_column in symbol_columns]

    if not pg.time.get_ticks() % 30 and alpha_value < 80:
        alpha_value += 1
        surface.set_alpha(alpha_value)

    [exit() for i in pg.event.get() if i.type == pg.QUIT]
    pg.display.flip()
    clock.tick(120)
