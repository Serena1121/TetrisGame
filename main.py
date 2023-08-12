import pygame
import sys
import random
from define import *
from level import *
from Score.score import draw_score, CaculateScore


clock = pygame.time.Clock()

def main():
    global score, bonus, move_direction, isRotate, board, x, y, current_shape, current_color, can_move
    score = 0
    bonus = 0
    move_direction = None
    isRotate = False
    current_shape, current_color = generate_shape()
    can_move = True
    board = [[BLACK for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
    x, y = 3, 0

    pygame.init()
    pygame.mixer.init()

    background_music = pygame.mixer.Sound('Assets/TetrisThemeSong.mp3')
    clear_music = pygame.mixer.Sound('Assets/ClearLaser.mp3')
    background_music.play(-1)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(NAME)
    running = True    
    clock = pygame.time.Clock()
    drop_counter = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_direction = -1
                elif event.key == pygame.K_RIGHT:
                    move_direction = 1
                elif event.key == pygame.K_DOWN:
                    drop_counter = (DOWN_SPEED - 2)
                elif event.key == pygame.K_UP:
                    isRotate = True

        if move_direction is not None:
            new_x = x + move_direction
            if not is_collision(board, current_shape, new_x, y):
                x = new_x
        
        if isRotate:
            rotated_shape = [list(reversed(row)) for row in zip(*current_shape)]
            if not is_collision(board, rotated_shape, x, y):
                current_shape = rotated_shape

        move_direction = None
        isRotate = False

        drop_counter = drop_counter + 1
        if drop_counter >= DOWN_SPEED:
            can_move, x, y, board, current_shape, current_color, score, bonus = shape_fall(clear_music, can_move, x, y, board, current_shape, current_color, score, bonus)

            drop_counter = 0
            
        screen.fill(BLACK)
        for row in range(len(board)):
            for col in range(len(board[row])):
                draw_block(screen, col, row, board[row][col])

        draw_shape(screen, current_shape, x, y, current_color)

        draw_score(screen, score)

        pygame.display.flip()
        clock.tick(UPDATE)

        if not can_move:
            running = False
       
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()