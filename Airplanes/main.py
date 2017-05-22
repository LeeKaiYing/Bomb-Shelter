import pygame
from player import *
from background import *
from inputmanager import *
from gamemanager import *
from enemy import *
def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((600, 700))
    pygame.display.set_caption("1945")
    return screen

def run():
    game_manager.run()

def draw(screen):
    screen.fill((0, 0, 0))
    game_manager.draw(screen)


screen = init_pygame()
clock = pygame.time.Clock()

game_manager.add(Background())
game_manager.add(Player())
game_manager.add(EnemyPlane())

loop = True

while loop:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False

    input_manager.run(events)

    run()

    draw(screen)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()

