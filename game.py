import pygame
import random

# --------- CONSTANTS ---------
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
PADDLE_SPEED = 0.5
BALL_SPEED_MIN = 0.4
BALL_SPEED_MAX = 0.7

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Consolas', 30)

    # --------- GAME OBJECTS ---------
    paddle_1 = pygame.Rect(30, SCREEN_HEIGHT // 2 - 50, 7, 100)
    paddle_2 = pygame.Rect(SCREEN_WIDTH - 50, SCREEN_HEIGHT // 2 - 50, 7, 100)

    ball = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 25, 25)
    ball_vel_x = random.choice([-1, 1]) * random.uniform(BALL_SPEED_MIN, BALL_SPEED_MAX)
    ball_vel_y = random.choice([-1, 1]) * random.uniform(BALL_SPEED_MIN, BALL_SPEED_MAX)

    paddle_1_move = 0
    paddle_2_move = 0
    started = False

    # --------- GAME LOOP ---------
    while True:
        dt = clock.tick(60)

        # --- EVENT HANDLING ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if not started and event.key == pygame.K_SPACE:
                    started = True
                # Player 1
                if event.key == pygame.K_w:
                    paddle_1_move = -PADDLE_SPEED
                if event.key == pygame.K_s:
                    paddle_1_move = PADDLE_SPEED
                # Player 2
                if event.key == pygame.K_UP:
                    paddle_2_move = -PADDLE_SPEED
                if event.key == pygame.K_DOWN:
                    paddle_2_move = PADDLE_SPEED

            if event.type == pygame.KEYUP:
                # Player 1
                if event.key in (pygame.K_w, pygame.K_s):
                    paddle_1_move = 0
                # Player 2
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    paddle_2_move = 0

        # --- UPDATE GAME OBJECTS ---
        if started:
            ball.x += ball_vel_x * dt
            ball.y += ball_vel_y * dt

            # Ball collision with top/bottom
            if ball.top <= 0:
                ball.top = 0
                ball_vel_y *= -1
            if ball.bottom >= SCREEN_HEIGHT:
                ball.bottom = SCREEN_HEIGHT
                ball_vel_y *= -1

            # Ball collision with paddles
            if ball.colliderect(paddle_1) and ball_vel_x < 0:
                ball.left = paddle_1.right
                ball_vel_x *= -1
            if ball.colliderect(paddle_2) and ball_vel_x > 0:
                ball.right = paddle_2.left
                ball_vel_x *= -1

            # Ball out of bounds → end game
            if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
                started = False
                # Reset ball to center
                ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                ball_vel_x = random.choice([-1, 1]) * random.uniform(BALL_SPEED_MIN, BALL_SPEED_MAX)
                ball_vel_y = random.choice([-1, 1]) * random.uniform(BALL_SPEED_MIN, BALL_SPEED_MAX)

        # Move paddles
        paddle_1.y += paddle_1_move * dt
        paddle_2.y += paddle_2_move * dt

        # Keep paddles on screen
        if paddle_1.top < 0:
            paddle_1.top = 0
        if paddle_1.bottom > SCREEN_HEIGHT:
            paddle_1.bottom = SCREEN_HEIGHT
        if paddle_2.top < 0:
            paddle_2.top = 0
        if paddle_2.bottom > SCREEN_HEIGHT:
            paddle_2.bottom = SCREEN_HEIGHT

        # --- DRAW ---
        screen.fill(COLOR_BLACK)
        pygame.draw.rect(screen, COLOR_WHITE, paddle_1)
        pygame.draw.rect(screen, COLOR_WHITE, paddle_2)
        pygame.draw.rect(screen, COLOR_WHITE, ball)

        # Start screen
        if not started:
            text = font.render('Press SPACE to start', True, COLOR_WHITE)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text, text_rect)

        pygame.display.update()

    paddle_1_rect.top += paddle_1_move * delta_time
    paddle_2_rect.top += paddle_2_move * delta_time

if __name__ == "__main__":
    main()

