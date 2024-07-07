import pygame

from entity import player, enemy_group, window, Enemy

# Clock setting
clock = pygame.time.Clock()
timer_1 = pygame.USEREVENT + 1
pygame.time.set_timer(timer_1, 250)

# code loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == timer_1:
            for _ in range(3):
                # noinspection PyTypeChecker
                enemy_group.add(Enemy())
    # blit
    window.fill((255, 255, 255))
    window.blit(player.image, player.rect)
    player.update()

    enemy_group.update()
    enemy_group.draw(window)
    # noinspection PyTypeChecker
    if pygame.sprite.spritecollide(player, enemy_group, False):
        running = False

    clock.tick(60)
    pygame.display.update()
