import sys

import pygame


class SomeGame:
    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

    def main_loop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            rect = pygame.Rect(100, 100, 100, 100)
            pygame.draw.rect(self.screen, (255, 0, 0), rect, 1)
            pygame.display.update()
