import pygame
import sys
import time
from settings import *
from level import Level
import os


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        absolute_path = os.path.dirname(__file__)
        relative_path = '../graphics/world/emoji.png'
        full_path = os.path.join(absolute_path, relative_path)
        game_icon = pygame.image.load(full_path)
        pygame.display.set_icon(game_icon)
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick(FPS) / 1000
            self.level.run(dt)
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
