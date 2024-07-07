import pygame
import random

# window setting
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()

        self.image.fill((76, 124, 150))

        self.rect.bottom = WINDOW_HEIGHT
        self.rect.centerx = WINDOW_WIDTH / 2

    def update(self):
        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 10
        if keys[pygame.K_d]:
            self.rect.x += 10
        if keys[pygame.K_w]:
            self.rect.y -= 10
        if keys[pygame.K_s]:
            self.rect.y += 10

        # limit movement system
        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.rect = self.image.get_rect()
        self.vel = random.choice(range(8, 11))

        self.image.fill((200, 0, 0))

        self.rect.centerx = random.choice(range(15, WINDOW_WIDTH - 15))

    def update(self):
        self.rect.y += self.vel

        if self.rect.bottom >= WINDOW_HEIGHT:
            # noinspection PyTypeChecker
            enemy_group.remove(self)


# entity setting
player = Player()

enemy_group = pygame.sprite.Group()
for _ in range(12):
    # noinspection PyTypeChecker
    enemy_group.add(Enemy())
