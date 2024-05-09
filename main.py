import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Define game object classes
snake_block_size = 20
snake_speed = 10

font_style = pygame.font.SysFont(None, 30)


def display_score(score):
    score_text = font_style.render("Score: " + str(score), True, black)
    game_window.blit(score_text, [10, 10])


def draw_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.circle(
            game_window, green,
            [x[0] + snake_block_size // 2, x[1] + snake_block_size // 2],
            snake_block_size // 2)


def draw_food(food_x, food_y):
    pygame.draw.circle(
        game_window, red,
        [food_x + snake_block_size // 2, food_y + snake_block_size // 2],
        snake_block_size // 2)
    pygame.draw.circle(
        game_window, white,
        [food_x + snake_block_size // 2, food_y + snake_block_size // 2],
        snake_block_size // 4)


def get_player_name():
    player_name = ""
    while not player_name:
        player_name = input("Enter your name: ")
    return player_name.capitalize()


def game_loop():
    game_over = False
    game_close = False
    game_paused = False

    x1 = window_width / 2
    y1 = window_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    food_x = round(
        random.randrange(0, window_width - snake_block_size) / 20.0) * 20.0
    food_y = round(
        random.randrange(0, window_height - snake_block_size) / 20.0) * 20.0

    player_name = get_player_name()

    while not game_over:

        while game_close:
            game_window.fill(white)
            game_over_message1 = font_style.render(
                f"Game Over {player_name}, your score is: {snake_length - 1}",
                True, red)
            game_over_message2 = font_style.render(
                "If you want to Quit; press Q. If you want to restart; press R",
                True, red)
            game_window.blit(game_over_message1,
                             [window_width / 6, window_height / 3])
            game_window.blit(game_over_message2,
                             [window_width / 6, window_height / 3 + 40])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_p:
                    game_paused = not game_paused
                elif event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                elif event.key == pygame.K_r:
                    game_loop()

        if not game_paused:
            if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
                game_close = True

            x1 += x1_change
            y1 += y1_change
            game_window.fill(white)
            draw_food(food_x, food_y)
            snake_head = []
            snake_head.append(x1)
            snake_head.append(y1)
            snake_list.append(snake_head)
            if len(snake_list) > snake_length:
                del snake_list[0]

            for x in snake_list[:-1]:
                if x == snake_head:
                    game_close = True

            draw_snake(snake_block_size, snake_list)
            display_score(snake_length - 1)

            pygame.display.update()

            if x1 == food_x and y1 == food_y:
                food_x = round(
                    random.randrange(0, window_width - snake_block_size) /
                    20.0) * 20.0
                food_y = round(
                    random.randrange(0, window_height - snake_block_size) /
                    20.0) * 20.0
                snake_length += 1

            clock = pygame.time.Clock()
            clock.tick(snake_speed)
        else:
            pause_message = font_style.render(
                "Game Paused. Press P to resume.", True, black)
            game_window.blit(pause_message,
                             [window_width / 3, window_height / 2])
            pygame.display.update()

    pygame.quit()
    quit()


game_loop()
