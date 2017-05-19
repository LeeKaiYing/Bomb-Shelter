import pygame

pygame.init()

pygame.display.set_caption("Đẩy Hộp Mãi Không Xong")

screen = pygame.display.set_mode((600, 600))
loop = True
clock = pygame.time.Clock()

mario_image = pygame.image.load("mario.png")
square_image = pygame.image.load("square.png")
box_image = pygame.image.load("box.png")
gate_image = pygame.image.load("gate.png")
col_count = 18
row_count = 18

mario_col = 0
mario_row = 0
mario_next_x = 0
mario_next_y = 0

square_width = square_image.get_width()
square_height = square_image.get_height()


box_col = 3
box_row = 2

box_width = box_image.get_width()
box_height = box_image.get_height()

gate_col = 15
gate_row = 12
gate_width = gate_image.get_width()
gate_height = gate_image.get_height()

right_pressed = False
left_pressed = False
up_pressed = False
down_press = False

def maps(next_col, next_row):
    if next_col >= 0 and next_col < col_count and next_row >= 0 and next_row < row_count:
        return True
    return False

while loop:
    x_step = 0
    y_step = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                    y_step = 1
            elif event.key == pygame.K_LEFT:
                    y_step = -1
            elif event.key == pygame.K_UP:
                    x_step = -1
            elif event.key == pygame.K_DOWN:
                    x_step = 1
            else:
                pass

            mario_next_x = mario_col + x_step
            mario_next_y = mario_row + y_step

            if maps(mario_next_x, mario_next_y):
                if (mario_next_x, mario_next_y) != (box_col, box_row):
                    mario_row = mario_next_y
                    mario_col = mario_next_x
    screen.fill((233, 40, 40))

    for col in range(col_count):
        for row in range(row_count):
            x = row * square_width - square_width / 2 + 16
            y = col * square_height - square_height / 2 + 16

            screen.blit(square_image, (x, y))

    mario_x = (mario_row * square_width) - square_width / 2 + 16
    mario_y = (mario_col * square_height) - square_height / 2 + 16

    box_x = (box_row * square_width) - square_width / 2 + 50
    box_y = (box_col * square_height) - square_height / 2 + 50

    gate_x = (gate_row * square_width) - square_width / 2 + 50
    gate_y = (gate_col * square_height) - square_height / 2 + 50


    screen.blit(mario_image,(mario_x, mario_y))
    screen.blit(box_image, (box_x, box_y))
    screen.blit(gate_image, (gate_x, gate_y))

    pygame.display.flip()
    clock.tick(60)