import pygame
from dinogame.speed_manager import SpeedManager
from dinogame.cactus import Cactus
from dinogame.constants import FPS, SCREEN_HEIGHT, SCREEN_WIDTH, WHITE
from dinogame.dino import Dino
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
score = Score(sprite)
speed_manager = SpeedManager(score)

# Group
group = pygame.sprite.Group()

# Dino
dino = Dino(sprite, speed_manager)
group.add(dino)
# Cactus
cactus = Cactus(sprite, speed_manager)
group.add(cactus)
# Ground
ground = Ground(sprite, speed_manager)
group.add(ground)
# Score
group.add(score)


# Game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chrome Dino Game")

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            dino.jump()

    # Update game
    if not game_over:
        speed_manager.update()
        group.update()

        # Collision
        if cactus.rect.colliderect(dino.rect):
            game_over = True

    # Draw everything
    screen.fill(WHITE)
    group.draw(screen)

    if game_over:
        game_over_text = sprite.get(1294, 30, 381, 21)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
        # for event in pygame.event.get():
        #     if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #         score.reset()
        #         game_over = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
