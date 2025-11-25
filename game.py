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

    paddle_1_rect = pygame.Rect(30, 0, 7, 100)
    paddle_2_rect = pygame.Rect(SCREEN_WIDTH - 50, 0, 7, 100)
    paddle_1_move = 0
    paddle_2_move = 0

    ball_rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 25, 25)
    ball_accel_x = random.randint(2, 4) * 0.1
    ball_accel_y = random.randint(2, 4) * 0.1

    if random.randint(1, 2) == 1:
        ball_accel_x *= -1
    if random.randint(1, 2) == 1:
        ball_accel_y *= -1

    while True:
        # EVENT LOOP
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # CLEAR SCREEN
        screen.fill(COLOR_BLACK)

        # DRAW PADDLES
        pygame.draw.rect(screen, COLOR_WHITE, paddle_1_rect)
        pygame.draw.rect(screen, COLOR_WHITE, paddle_2_rect)

        # DRAW BALL
        pygame.draw.rect(screen, COLOR_WHITE, ball_rect)

        # UPDATE DISPLAY
        pygame.display.update()

if __name__ == "__main__":
    main()
