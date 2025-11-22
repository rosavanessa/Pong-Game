import pygame
import random

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pong")

    while True:
        """
        Set the back ground color to black
        needs to be called everytime the game updates
        """
        screen.fill(COLOR_BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            
