# Pygame template - the skeleton for a new pygame project.
import pygame
import time
import os
import random

WIDTH = 800
HEIGHT = 600
FPS = 100

# Defines colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

font_name = pygame.font.match_font('fixedsys regular')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

class Player(pygame.sprite.Sprite):
    # Sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (15, HEIGHT / 2)
        self.speedy = 0
    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.speedy = -5
        if keystate[pygame.K_s]:
            self.speedy = 5
        self.rect.y += self.speedy


class otherPlayer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH - 20, HEIGHT / 2)
        self.speedy = 0
    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy = -5
        if keystate[pygame.K_DOWN]:
            self.speedy = 5
        self.rect.y += self.speedy

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((12.5, 12.5))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedx = random.randint(1, 5)
        self.speedy = random.randint(1, 5)
    def update(self):
        if pygame.sprite.collide_rect(self, otherplayer) or pygame.sprite.collide_rect(self, player):
            self.speedx *= -1.15
        if pygame.sprite.collide_rect(self, wall) or pygame.sprite.collide_rect(self, otherwall):
            self.speedy *= -1
        self.rect.x += self.speedx
        self.rect.y += self.speedy

class Wall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((800, 7.5))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, 7)

class otherWall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((800, 7.5))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, 593)

# Initialises pygame and creates a window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
otherplayer = otherPlayer()
ball = Ball()
wall = Wall()
otherwall = otherWall()
all_sprites.add(player)
all_sprites.add(otherplayer)
all_sprites.add(ball)
all_sprites.add(wall)
all_sprites.add(otherwall)
score = 0
otherScore = 0
# Game loop
running = False
menu = True
while menu:
    clock.tick(FPS)
    for event in pygame.event.get():
        # Check for closing the window
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    draw_text(screen, "PONG", 100, WIDTH / 2, 50)
    draw_text(screen, "Play", 40, WIDTH / 2, HEIGHT / 2)

    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_SPACE]:
        menu = False
        running = True
    pygame.display.flip()

while running:
    # Keep loop running at the right speed
    clock.tick(FPS)
    # Process input(events)
    for event in pygame.event.get():
        # Check for closing the window
        if event.type == pygame.QUIT:
            running = False
    # Update
    all_sprites.update()

    if ball.rect.x > WIDTH:
        score += 1
        ball.rect.center = (WIDTH / 2, HEIGHT / 2)
        ball.speedx = -3
        ball.speedy = -3
    if ball.rect.x < 0:
        otherScore += 1
        ball.rect.center = (WIDTH / 2, HEIGHT / 2)
        ball.speedx = 3
        ball.speedy = 3

    # Render / draw
    screen.fill(BLACK)
    all_sprites.draw(screen)
    draw_text(screen, str(score) + ":" + str(otherScore), 30, WIDTH / 2, 30)
    # After drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
