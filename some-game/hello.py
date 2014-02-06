__author__ = 'Laurie'

import pygame
from somegame import SomeGame

if not pygame.font: 
    print('Warning, fonts disabled')

if not pygame.mixer: 
    print('Warning, sound disabled')

MainWindow = SomeGame()
MainWindow.main_loop()
