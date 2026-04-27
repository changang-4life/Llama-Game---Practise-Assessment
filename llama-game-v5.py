""" Llama Game
v5 - Running the Game
    - Obstacle movement
    - User controls
    - Ends if the llama hits an obstacle
    - Game score (time alive)
"""

import pygame
clock = pygame.time.Clock()

pygame.init()

llama = pygame.image.load("Llama.png")
llama_resized = pygame.transform.scale(llama, (70, 70))

ground = pygame.image.load("ground.png")
ground_resized = pygame.transform.scale(ground, (1100, 550))

obstacle = pygame.image.load("cactus.png")
obstacle_resized = pygame.transform.scale(obstacle, (70, 70))

screen = pygame.display.set_mode((1100, 550))
font = pygame.font.SysFont("Arial", 24)

def game_loop():
    quit_game = False

    # Llama position
    llama_x = 100
    llama_y = 355  # resting Y position

    # Jump variables
    jumping = False
    JUMP_HEIGHT = 20
    Y_GRAVITY = 1
    y_velocity = JUMP_HEIGHT

    # Obstacle variables
    obstacle_x = 1100
    OBSTACLE_SPEED = 6

    # Score
    score = 0

    speed = 60  # FPS cap

    while not quit_game:
        screen.fill("White")
        screen.blit(ground_resized, (0, 100))

        # --- Jump logic ---
        if jumping:
            llama_y -= y_velocity
            y_velocity -= Y_GRAVITY
            if y_velocity < -JUMP_HEIGHT:  # peak reached and came back down
                jumping = False
                y_velocity = JUMP_HEIGHT
                llama_y = 355  # snap back to ground level

        # --- Obstacle movement ---
        obstacle_x -= OBSTACLE_SPEED
        if obstacle_x < -70:  # fully off screen, reset to right side
            obstacle_x = 1100

        # --- Score: time alive in seconds ---
        score += clock.get_time() / 1000

        # --- Collision detection ---
        llama_rect = pygame.Rect(llama_x + 10, llama_y + 5, 50, 60)
        obstacle_rect = pygame.Rect(obstacle_x + 10, 355 + 5, 50, 60)

        if llama_rect.colliderect(obstacle_rect):
            screen.fill("White")
            game_over_text = font.render(f"Game Over! Score: {int(score)}", True, (200, 0, 0))
            screen.blit(game_over_text, (400, 260))
            pygame.display.update()
            pygame.time.wait(2500)
            quit_game = True
            continue

        # --- Draw sprites ---
        screen.blit(llama_resized, (llama_x, llama_y))
        screen.blit(obstacle_resized, (obstacle_x, 355))

        # --- HUD: Score ---
        score_text = font.render(f"Score: {int(score)}", True, (20, 20, 20))
        screen.blit(score_text, (10, 10))

        # --- Events ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_SPACE) and not jumping:
                    jumping = True
                    y_velocity = JUMP_HEIGHT  # reset velocity each jump

        pygame.display.update()
        clock.tick(speed)

game_loop()
pygame.quit()
quit()