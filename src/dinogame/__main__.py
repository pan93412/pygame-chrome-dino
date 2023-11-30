import pygame
from dinogame.message import Message
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
# Message
message = Message()
group.add(message)
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
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or \
           (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
            if not game_over:
                dino.jump()
            else:
                # restart game
                score.reset()
                cactus.reset()
                dino.reset()
                message.reset()
                game_over = False
        # cheat code
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            if not dino.flyover:
                message.show_message("Flyover mode activated!!")
            dino.flyover = not dino.flyover

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
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2 - 30))

        replay_button = sprite.get(151, 135, 61, 53)
        screen.blit(replay_button, (SCREEN_WIDTH // 2 - replay_button.get_width() // 2, SCREEN_HEIGHT // 2 - replay_button.get_height() // 2 + 30))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
