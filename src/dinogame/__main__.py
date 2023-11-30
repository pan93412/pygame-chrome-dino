import pygame
from dinogame.constants import BLACK, FPS, GRAVITY, JUMP_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH, WHITE
from dinogame.ground import Ground
from dinogame.score import Score
from dinogame.sprite import Sprite

# Initialize Pygame
pygame.init()

# Game Variables
clock = pygame.time.Clock()
running = True
game_over = False

# Load sprite sheet
sprite = Sprite()

# Dino sprite
dino_run_1 = sprite.get(1854, 0, 88, 94)
dino_run_2 = sprite.get(1942, 0, 88, 94)
dino_rect = dino_run_1.get_rect()
dino_rect.x = 80
dino_rect.y = SCREEN_HEIGHT - dino_rect.height - 10

# Cactus sprite
cactus = sprite.get(446, 2, 33, 70)
cactus_rect = cactus.get_rect()
cactus_rect.x = SCREEN_WIDTH
cactus_rect.y = SCREEN_HEIGHT - cactus_rect.height - 10

# Ground sprite
ground = sprite.get(2, 104, 2400, 26)
ground_x = 0

# Dino variables
dino_vel_y = 0
dino_jumping = False

# Groups
group = pygame.sprite.Group()

# Ground
ground = Ground(sprite)
ground.rect.y = SCREEN_HEIGHT - ground.rect.height

# Score
score = Score(sprite)
score.rect.x = SCREEN_WIDTH - score.rect.width - 10
score.rect.y = 10

group.add(score)
group.add(ground)

# Game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chrome Dino Game")

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not dino_jumping:
            if event.key == pygame.K_SPACE:
                dino_jumping = True
                dino_vel_y = -JUMP_SPEED

    # Update game
    if not game_over:
        group.update()

        # Dino
        dino_vel_y += GRAVITY
        dino_rect.y += dino_vel_y
        if dino_rect.y > SCREEN_HEIGHT - dino_rect.height - 10:
            dino_rect.y = SCREEN_HEIGHT - dino_rect.height - 10
            dino_jumping = False

        # Cactus
        cactus_rect.x -= 10
        if cactus_rect.x < -cactus_rect.width:
            cactus_rect.x = SCREEN_WIDTH
            cactus_rect.y = SCREEN_HEIGHT - cactus_rect.height - 10

        # Ground
        ground_x -= 10
        if ground_x <= -2400:
            ground_x = 0

        # Collision
        if dino_rect.colliderect(cactus_rect):
            game_over = True

    # Draw everything
    screen.fill(WHITE)
    screen.blit(dino_run_1 if pygame.time.get_ticks() // 200 % 2 else dino_run_2, dino_rect)
    screen.blit(cactus, cactus_rect)
    group.draw(screen)

    if game_over:
        game_over_text = sprite.get(1294, 30, 381, 21)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
